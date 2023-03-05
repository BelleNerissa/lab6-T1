import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv(
    'C:/Projects/PUC/6p/conversorDate/repositorios.csv', delimiter=';')

# Filtrando os dados para a linguagem primária TypeScript
df_python = df[df["PrimaryLanguage"] == "Python"]

# Calculando a mediana de pull requests aceitas para a linguagem TypeScript
AcceptedPullRequestsPY = df_python["AcceptedPullRequests"].median()

# Calcula a mediana de releases em TS
releasesPY = df_python["Releases"].median()

# Converte as colunas "updatedAt" para datetime
df_python['updatedAt'] = pd.to_datetime(df_python['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df_python = df_python.dropna(subset=['updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df_python['updatedTime'] = (hoje - df_python['updatedAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_updatedTimePY = df_python['updatedTime'].median()

print("A mediana da total de pull requests é para a linguagem Python", AcceptedPullRequestsPY)
print("Mediana de releases a linguagem Python:", releasesPY)
print(f"A mediana do tempo de atualização é {mediana_updatedTimePY} dias para a linguagem Python")

