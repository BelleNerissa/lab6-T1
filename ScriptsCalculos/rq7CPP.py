import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv(
    'C:/Projects/PUC/6p/conversorDate/repositorios.csv', delimiter=';')

# Filtrando os dados para a linguagem primária TypeScript
df_CPP = df[df["PrimaryLanguage"] == "C++"]

# Calculando a mediana de pull requests aceitas para a linguagem TypeScript
AcceptedPullRequestsCPP= df_CPP["AcceptedPullRequests"].median()

# Calcula a mediana de releases em TS
releasesCPP = df_CPP["Releases"].median()

# Converte as colunas "updatedAt" para datetime
df_CPP['updatedAt'] = pd.to_datetime(df_CPP['updatedAt'], format='%Y-%m-%d')

# Remove as linhas com valores ausentes
df_CPP = df_CPP.dropna(subset=['updatedAt'])

# Calcula a idade de cada linha e adiciona a uma nova coluna "idade"
hoje = datetime.today().date()
df_CPP['updatedTime'] = (hoje - df_CPP['updatedAt'].dt.date).dt.days

# Calcula a mediana da idade e da idade de atualização de todas as linhas
mediana_updatedTimeCPP = df_CPP['updatedTime'].median()

print("A mediana da total de pull requests é para a linguagem C++", AcceptedPullRequestsCPP)
print("Mediana de releases a linguagem C++:", releasesCPP)
print(f"A mediana do tempo de atualização é {mediana_updatedTimeCPP} dias para a linguagem C++")

