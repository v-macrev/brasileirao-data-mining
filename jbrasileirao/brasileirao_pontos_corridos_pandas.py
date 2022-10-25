#----------- CONFIGURAÇÃO DO AMBIENTE DE ANÁLISE --------------#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#CONFIG GRÁFICOS
plt.rcParams['figure.figsize'] = (15,10)
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 15

#BASE DE DADOS
df_periodo = pd.read_csv("https://github.com/v-macrev/brasileirao-data-mining/blob/main/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-periodo.csv?raw=true", delimiter=";")
df_jogos   = pd.read_csv("https://github.com/v-macrev/brasileirao-data-mining/blob/main/datasets/campeonato-brasileiro-pontos-corridos-2003-2020-jogos.csv?raw=true", delimiter=";")

#PADRONIZANDO PARA LOWER CASE
df_periodo.columns = df_periodo.columns.str.lower()
df_jogos.columns   = df_jogos.columns.str.lower()

#ALTERANDO DADOS DO TIPO CHAR PARA DATE
df_periodo['inicio'] = pd.to_datetime(df_periodo['inicio'], format="%d/%m/%Y")
df_periodo['fim'   ] = pd.to_datetime(df_periodo['fim'   ], format="%d/%m/%Y")
df_jogos['data'] = pd.to_datetime(df_jogos['data'], format="%d/%m/%Y")

#CAPTALIZANDO AS STRINGS
df_jogos['dia'      ] = df_jogos['dia'      ].str.title()
df_jogos['mandante' ] = df_jogos['mandante' ].str.title()
df_jogos['visitante'] = df_jogos['visitante'].str.title()
df_jogos['vencedor' ] = df_jogos['vencedor' ].str.title()
df_jogos['arena'    ] = df_jogos['arena'    ].apply(lambda x: x.title())

#ASSIMILANDO DATASETS
df_periodo['key'] = 1
df_jogos['key'] = 1

df = pd.merge(df_periodo, df_jogos, on ='key').drop("key", 1)
df = df.query('data >= inicio & data <= fim')

df.head(5)



#----------- INÍCIO DAS ANÁLISES --------------#