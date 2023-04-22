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