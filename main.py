import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyexcel_ods import save_data
from collections import OrderedDict

df = pd.read_csv('organizacoes.csv', delimiter=",", encoding="UTF-8")
df2 = pd.read_csv('organizacoes2.csv', delimiter=",", encoding="UTF-8")
df3 = pd.read_csv('organizacoes2.csv', delimiter=",", encoding="UTF-8")

# Remove todas as colunas to tipo "Unnamed"
frames = [df, df2, df3]
df = pd.concat(frames)
df = df.loc[:, ~df.columns.str.contains('Unnamed')]

""" Exporte o DataFrame “df” para um arquivo binário chamado “dados.od” """
df.astype(str)
whole_data_list = []
d = OrderedDict()
whole_data_list.append(list(df.columns))
for index, row in df.iterrows():
    whole_data_list.append(list(row.values))
d.update({"Moved sheet": whole_data_list})
save_data('dados.ods', d)

""" Faça um plot de caixa (Boxplot) dos números de funcionários de indústrias fundadas após o
        ano 2000; """
df_a = df[['Index', 'Founded', 'Number of employees']]
df_a = df_a[df_a['Founded'] >= 2000]
fig = plt.figure(figsize=(10, 10))
plt.boxplot(df_a['Number of employees'])
plt.ylabel('Número de Funcionários')
plt.show()

""" Faça um plot de barras dos tipos de indústrias fundadas após o ano 2000; """
df_b = df[['Index', 'Founded', 'Industry']]
df_b = df_b[df_b['Founded'] >= 2000]
tipos_count = df_b['Industry'].value_counts()

fig = plt.figure(figsize =(10, 10))
tipos_count.plot(kind = 'bar')
plt.title("tipos")
plt.xlabel("Industrias")
plt.ylabel("contagem")
#plt.tight_layout()  # Para evitar que os rótulos fiquem cortados
plt.show()

""" Crie casos de teste (asserts - unittest.TestCase) para verificar se os plots contém mais do que
        30 valores e se os dados não são valores nulos;"""
import unittest

class DF:
    def __init__(self, var):
        self.var = var
    @staticmethod
    def validate(arg):
        return len(df.index) > 30 and df.notnull()
class DFTest(unittest.TestCase):
    def test_validate_size(self):
        self.assertTrue(DF.validate(df))

""" Crie um DataFrame “df” ordenado de forma crescente pela coluna “Founded” para valores
        maiores que 2000 incluindo as colunas “Name”, “Country”, “Founded” e “Number of
        employees”; """
df_c = df[['Founded', 'Name', 'Country', 'Number of employees']]
df_c = df_c[df_c['Founded'] >= 2000]
df_c = df_c.set_index('Founded')
df_c = df_c.sort_index()

""" Atualmente as empresas fundadas mais recentemente (após o ano 2000) têm em totalidade
        mais funcionários que as empresas antigas? """
# Separe as empresas em dois grupos: as fundadas após 2000 e as fundadas antes ou em 2000
empresas_recentes = df[df['Founded'] > 2000]
empresas_antigas = df[df['Founded'] <= 2000]

# Calcule o número total de funcionários para cada grupo
total_funcionarios_recentes = empresas_recentes['Number of employees'].sum()
total_funcionarios_antigas = empresas_antigas['Number of employees'].sum()

# Compare os totais e imprima o resultado
if total_funcionarios_recentes > total_funcionarios_antigas:
    print("Empresas recentes têm mais funcionários.")
else:
    print("Empresas antigas têm mais funcionários.")

""" Calcule o valor total de funcionários agrupando por década de fundação (1970-1980, ...).
        Aplique regressão para encontrar uma função de ajuste aos dados. """
from sklearn.linear_model import LinearRegression
# Suponha que você já tenha lido seu DataFrame df como no seu código original

# Crie uma nova coluna para a década de fundação
df['Decade'] = (df['Founded'] // 10) * 10

# Agrupe por década e calcule o valor total de funcionários em cada década
funcionarios_por_decada = df.groupby('Decade')['Number of employees']\
    .sum().reset_index()

# Crie um array numpy para os anos das décadas
anos_decadas = funcionarios_por_decada['Decade'].values.reshape(-1, 1)

# Crie um array numpy para o número total de funcionários
total_funcionarios = funcionarios_por_decada['Number of employees'].values

# Crie e ajuste o modelo de regressão linear
modelo_regressao = LinearRegression()
modelo_regressao.fit(anos_decadas, total_funcionarios)

# Faça previsões para as décadas futuras (por exemplo, até 2030)
decadas_futuras = np.array(range(1970, 2031, 10)).reshape(-1, 1)
previsoes = modelo_regressao.predict(decadas_futuras)

# Plote os dados originais e a linha de regressão
plt.scatter(anos_decadas, total_funcionarios, label='Dados Originais')
plt.plot(decadas_futuras, previsoes, label='Regressão Linear', color='red')
plt.xlabel('Década de Fundação')
plt.ylabel('Total de Funcionários')
plt.title('Regressão Linear do Total de Funcionários por Década de Fundação')
plt.legend()
plt.show()

""" Interpole o valor para 1985 e extrapole para 2030 para calcular uma tendência. """

# Anos para interpolação e extrapolação
ano_interp = 1985
ano_extrap = 2030

# Use o modelo de regressão linear previamente ajustado para fazer previsões
previsao_interp = modelo_regressao.predict(np.array([[ano_interp]]))
previsao_extrap = modelo_regressao.predict(np.array([[ano_extrap]]))

print(f"Interpolação para {ano_interp}: {previsao_interp[0]:.2f} funcionários")
print(f"Extrapolação para {ano_extrap}: {previsao_extrap[0]:.2f} funcionários")