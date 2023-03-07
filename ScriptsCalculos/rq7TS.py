import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv(
    'C:/Projects/PUC/6p/LAB6-T1/ScriptsCalculos/repositorios.csv', delimiter=';')

# Filtrando os dados para a linguagem primária TypeScript
df_typescript = df[df["PrimaryLanguage"] == "TypeScript"]

# Calculando a mediana de pull requests aceitas para a linguagem TypeScript
AcceptedPullRequestsTS = df_typescript["AcceptedPullRequests"].median()
PullRequestsTS = df_typescript["PullRequests"].median()

# Calcula a mediana de releases em TS
releasesTS = df_typescript["Releases"].median()

# Converte as colunas "updatedAt" para datetime
df_typescript['updatedAt'] = pd.to_datetime(df_typescript['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df_typescript = df_typescript.dropna(subset=['updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df_typescript['updatedTime'] = (hoje - df_typescript['updatedAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_updatedTimeTS = df_typescript['updatedTime'].median()

print("A mediana da total de pull requests aceitas é para a linguagem TypeScript", AcceptedPullRequestsTS)
print("A mediana da total de pull requests é para a linguagem TypeScript", PullRequestsTS)
print("Mediana de releases para a linguagem TypeScript:", releasesTS)
print(f"A mediana do tempo de atualização é {mediana_updatedTimeTS} dias")

