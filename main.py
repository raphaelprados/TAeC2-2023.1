import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.read_csv('organizacoes.csv')
# Remove todas as colunas to tipo "Unnamed"
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

df2 = pd.read_csv('organizacoes2.csv')
# Remove todas as colunas to tipo "Unnamed"
df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]

df3 = pd.read_csv('organizacoes2.csv')
# Remove todas as colunas to tipo "Unnamed"
df3 = df3.loc[:, ~df3.columns.str.contains('^Unnamed')]

df += df2 + df3

# Faça um plot de caixa (Boxplot) dos números de funcionários de indústrias fundadas após o
#   ano 2000;
df_a = df[['Index', 'Founded', 'Number of employees']]
df_a = df_a[df_a['Founded'] >= 2000]

# Faça um plot de barras dos tipos de indústrias fundadas após o ano 2000;
df_b = df[['Index', 'Founded', 'Industry']]
df_b = df_b[df_b['Founded'] >= 2000]

# Crie casos de teste (asserts - unittest.TestCase) para verificar se os plots contém mais do que
#   30 valores e se os dados não são valores nulos;



# Crie um DataFrame “df” ordenado de forma crescente pela coluna “Founded” para valores
#   maiores que 2000 incluindo as colunas “Name”, “Country”, “Founded” e “Number of
#   employees”;
df_c = df[['Founded', 'Name', 'Country', 'Number of employees']]
df_c = df_c[df_c['Founded'] >= 2000]

# Exporte o DataFrame “df” para um arquivo binário chamado “dados.od”


# Atualmente as empresas fundadas mais recentemente (após o ano 2000) têm em totalidade
# mais funcionários que as empresas antigas?


# Calcule o valor total de funcionários agrupando por década de fundação (1970-1980, ...).
# Aplique regressão para encontrar uma função de ajuste aos dados.


# Interpole o valor para 1985 e extrapole para 2030 para calcular uma tendência.

