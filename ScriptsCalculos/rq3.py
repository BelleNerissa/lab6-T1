import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Projects/PUC/6p/conversorDate/repositorios.csv', delimiter=';')

# Calcula a mediana de releases
mediana_Releases = df['Releases'].median()

print(f"A mediana da total de Releases é {mediana_Releases}")

# cria o boxplot
plt.boxplot(df['Releases'].dropna(), showfliers=False)

# adiciona rótulos e título
plt.xlabel('Total de Releases')
plt.title('Boxplot do Total de Releases')

# salva o gráfico como uma imagem
plt.savefig('boxplot_releases_repositorios.png')

# exibe o gráfico
plt.show()