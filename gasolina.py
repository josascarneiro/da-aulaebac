# código de geração do gráfico

# Importando bibliotecas.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura de dados e criação de um dataframe
df = pd.read_csv('gasolina.csv')

# Cria um gráfico de linha com Seaborn.
sns.lineplot(x='dia', y='venda', data=df)

# Define o rótulo do eixo horizontal.
plt.xlabel('Dia')
# Define o rótulo do eixo vertical.
plt.ylabel('Preço da Gasolina')
# Define o título do gráfico.
plt.title('Preço Médio da Gasolina em São Paulo (10 primeiros dias de Julho de 2021)')

# Salva o gráfico como um arquivo PNG chamado 'gasolina.png'.
plt.savefig('gasolina.png')