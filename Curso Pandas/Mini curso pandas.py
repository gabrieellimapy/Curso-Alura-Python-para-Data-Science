# ---------------------------------------------------------------------------- #
#                                 PANDAS BÁSICO                                #
# ---------------------------------------------------------------------------- #

# ---------------------------- Estrutura de dados ---------------------------- #

# ---------------------------------------------------------------------------- #
#                                    SERIES                                    #
# ---------------------------------------------------------------------------- #

# -- São arrays unidimensionais rotulados que podem armazenar qualquer dado -- #

#s = pd.Series(dados, index = index)

# ---------------------------------------------------------------------------- #
#                                  Data Frames                                 #
# ---------------------------------------------------------------------------- #

# ----------- Array bidimensional com rótulos nas linhas e colunas, ---------- #
# ---------------------- armazenam qualquer tipo de dado --------------------- #

#df = pd.DataFrame(dados, index = index, columns = columns)

# ---------------------------------------------------------------------------- #
#                              ESTRUTURAS DE DADOS                             #
# ---------------------------------------------------------------------------- #

import pandas as pd

# ----------------- Criando uma Series a partir de uma lista ----------------- #

carros = ['Jetta Variant', 'Passat', 'Crossfox']

pd.Series(carros)

# --------- Criando um DataFrame a partir de uma lista de dicionários -------- #

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

dataset = pd.DataFrame(dados)
dataset

# -------------- Criando um DataFrame a partir de um dicionário -------------- #

dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'], 
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

dataset2 = pd.DataFrame(dados)

# ------------ Criando um DataFrame a partir de um arquivo externo ----------- #

dataset3 = pd.read_csv('Curso Pandas/data/db.csv', sep=';')
dataset3


# ---------------------------------------------------------------------------- #
#                            SELEÇÕES COM DATAFRAMES                           #
# ---------------------------------------------------------------------------- #

# --------------------------- Selecionando Colunas --------------------------- #

dataset3['valor']

type(dataset3['valor'])

# ---------- Cada coluna de um DataFrame pode ser tatada como Series --------- #

dataset3[['Valor']]  # Retorna uma única coluna, como um Dataframe

type(dataset3[['Valor']])


# ---------------------------------------------------------------------------- #
#                          Selecionando linhas [i : j]                         #
# ---------------------------------------------------------------------------- #


# -------- A indexação tem origem no zero e nos fatiamentos (*slices*) ------- #
# -------- a linha com índice i é **incluída** e a linha com índice j -------- #
# --------------------- **não é incluída** no resultado. --------------------- #

dataset3[0 : 3] # De zero ao terceiro item

# ---------------------------------------------------------------------------- #
#                                     .LOC                                     #
# ---------------------------------------------------------------------------- #

# ------------------ Seleciona um grupo de linhas e colunas ------------------ #
# ---------------- seguindo os rótulos ou uma matriz booleana ---------------- #

dataset3.loc['Passat']

# ----------- Retorna uma series com todas as informações do Passat ---------- #

dataset3.loc[['Passat','DS5']]

# -------- Retorna duas linhas sobre o Passat e DS5 como um DataFrame -------- #

dataset3.loc[['Passat', 'DS5'], ['Motor', 'Valor']]

# ----------- Retorna o mesmo DataFrame, com informações filtradas ----------- #

dataset3.loc[:, ['Motor', 'Valor']]

# ------- Retorna o valor das duas colunas para todo o DataFrame gerado ------ #

# ---------------------------------------------------------------------------- #
#                                     .ILOC                                    #
# ---------------------------------------------------------------------------- #

# ----------------- Seleciona com base nos índices, ou seja, ----------------- #
# -------------------- se baseia na posição da informação -------------------- #

dataset3.iloc[1]

# --------------------- Seleciona a informação do carro 1 -------------------- #
# ----------------------------- Retorna em Series ---------------------------- #

dataset3.iloc[[1]]

# --------------------------- Retorna em DataFrame --------------------------- #

dataset3.iloc[1:4]

# -------------- Busca do primeiro índice até o terceiro índice -------------- #
# -------- Seguindo o conceito de inclui um e diminui o valor do final ------- #
# --------------------------- Retorna em DataFrame --------------------------- #

dataset3.iloc[1:4. [0, 5, 2]]

dataset3.iloc[1:4, [0, 32, 52]]

# -- Retorna um DataFrame com as informações dos carros e colunas filtradas -- #


