import requests
import pandas as pd
from datetime import datetime

# Define a string de consulta GraphQL
query = '''
query ($cursor: String) {
  search(query: "stars:>100", type: REPOSITORY, first: 1, after: $cursor) {
              pageInfo {
                  hasPreviousPage
                  hasNextPage
                  startCursor
                  endCursor
            }
            edges {
                node {
                    ... on Repository {
                        id
                        url
                        name
                        nameWithOwner
                        stargazers {totalCount}
                        pullRequests {totalCount}
                        acceptedPullRequests: pullRequests(states: MERGED) { totalCount }
                        releases{totalCount}
                        primaryLanguage {name}
                        createdAt
                        updatedAt: defaultBranchRef {
                            target {
                                ... on Commit {
                                    history(first: 1) {
                                    edges {
                                        node {
                                        ... on Commit {
                                            committedDate
                                        }
                                        }
                                    }
                            }
                }
              }
            }
                        closedIssues: issues(first:1,states:CLOSED){totalCount}
                        totalIssues: issues(first:1){totalCount}
                    }
                }
            }
  }
}
'''

# Define o cabeçalho da requisição com o token de acesso à API do GitHub
headers = {
    'Authorization': 'Bearer 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'
}

# Cria um dataframe vazio para armazenar as informações dos repositórios
df = pd.DataFrame()

# Faz as requisições à API do GitHub em GraphQL para obter todos os repositórios
end_cursor = None
while True:
    # Define o valor do argumento "after" com o valor do cursor da página anterior, se houver
    variables = {'cursor': end_cursor} if end_cursor else {}

    # Faz a requisição à API do GitHub em GraphQL com a string de consulta e os argumentos
    response = requests.post('https://api.github.com/graphql',
                             json={'query': query, 'variables': variables}, headers=headers)

    # Extrai os dados JSON da resposta
    data = response.json()['data']['search']

    # Adiciona os itens da página atual ao dataframe existente
    df = pd.concat([df, pd.json_normalize(data['edges'])], ignore_index=True) 

    # Define o cursor da próxima página, se houver
    end_cursor = data['pageInfo']['endCursor']
    has_next_page = data['pageInfo']['hasNextPage']
    if not has_next_page:
        break

# Renomeia as colunas do dataframe
df.columns = ['ID',
              'URL',
              'Name',
              'NameWithOwner',
              'Stargazers',
              'PullRequests',
              'AcceptedPullRequests',
              'Releases',
              'PrimaryLanguage',
              'createdAt',
              'updatedAt',
              'closedIssues',
              'totalIssues',
              '']

# Extrai a data na coluna updatedAt
def extract_date(updatedAt):
    return updatedAt[0]['node']['committedDate']

df['updatedAt'] = df['updatedAt'].apply(extract_date)

df = df.drop(df.columns[-1], axis=1)

# Carrega o arquivo CSV com os dados dos repositórios
df.to_csv('repositorios.csv', sep=';', index=False)