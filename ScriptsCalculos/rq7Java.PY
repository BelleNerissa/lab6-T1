import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv(
    'C:/Projects/PUC/6p/LAB6-T1/ScriptsCalculos/repositorios.csv', delimiter=';')

# Filtrando os dados para a linguagem primária TypeScript
df_java = df[df["PrimaryLanguage"] == "Java"]

# Calculando a mediana de pull requests aceitas para a linguagem TypeScript
AcceptedPullRequestsJava= df_java["AcceptedPullRequests"].median()
PullRequestsJava= df_java["PullRequests"].median()

# Calcula a mediana de releases em TS
releasesJava = df_java["Releases"].median()


# Converte as colunas "updatedAt" para datetime
df_java['updatedAt'] = pd.to_datetime(df_java['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df_java = df_java.dropna(subset=['updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df_java['updatedTime'] = (hoje - df_java['updatedAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_updatedTimeJava = df_java['updatedTime'].median()

print("A mediana da total de pull requests aceitas é para a linguagem Java", AcceptedPullRequestsJava)
print("A mediana da total de pull requests é para a linguagem Java", PullRequestsJava)
print("Mediana de releases a linguagem Java:", releasesJava)
print(f"A mediana do tempo de atualização é {mediana_updatedTimeJava} dias para a linguagem Java")

