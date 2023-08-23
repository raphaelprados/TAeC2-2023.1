from os import write
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from pyexcel_ods import save_data
from collections import OrderedDict

df = pd.read_csv('organizacoes.csv', delimiter=",", encoding="UTF-8")
df2 = pd.read_csv('organizacoes2.csv', delimiter=",", encoding="UTF-8")
df3 = pd.read_csv('organizacoes2.csv', delimiter=",", encoding="UTF-8")

# Remove todas as colunas to tipo "Unnamed"
frames = [df, df2, df3]
df = pd.concat(frames)
df = df.loc[:, ~df.columns.str.contains('Unnamed')]
print(df)

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
plt.boxplot(df_a)
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
        return len(df.index) > 30
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


""" Calcule o valor total de funcionários agrupando por década de fundação (1970-1980, ...).
        Aplique regressão para encontrar uma função de ajuste aos dados. """


""" Interpole o valor para 1985 e extrapole para 2030 para calcular uma tendência. """

