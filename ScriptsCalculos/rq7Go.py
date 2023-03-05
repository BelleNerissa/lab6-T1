import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv(
    'C:/Projects/PUC/6p/conversorDate/repositorios.csv', delimiter=';')

# Filtrando os dados para a linguagem primária TypeScript
df_go = df[df["PrimaryLanguage"] == "Go"]

# Calculando a mediana de pull requests aceitas para a linguagem TypeScript
AcceptedPullRequestsGO= df_go["AcceptedPullRequests"].median()

# Calcula a mediana de releases em TS
releasesGO = df_go["Releases"].median()

# Converte as colunas "updatedAt" para datetime
df_go['updatedAt'] = pd.to_datetime(df_go['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df_go = df_go.dropna(subset=['updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df_go['updatedTime'] = (hoje - df_go['updatedAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_updatedTimeGO = df_go['updatedTime'].median()

print("A mediana da total de pull requests é para a linguagem Go", AcceptedPullRequestsGO)
print("Mediana de releases a linguagem Go:", releasesGO)
print(f"A mediana do tempo de atualização é {mediana_updatedTimeGO} dias para a linguagem Go")

