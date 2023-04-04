# ---------------------------------------------------------------------------- #
#                                 ARRAYS NUMPY                                 #
# ---------------------------------------------------------------------------- #
# ---------------------------- IMPORTANDO O NUMPY ---------------------------- #
# ----------- Calculo da quilometragem media por ano de cada carro ----------- #
import numpy as np
km_media = np.loadtxt('Linguagem e Numpy/dados/carros-km.txt')
km_media
ano_fabricacao = np.loadtxt('Linguagem e Numpy/dados/carros-anos.txt', dtype = int)
ano_fabricacao
km_media_ano = km_media / (2023 - ano_fabricacao)
km_media_ano
# ------ Quando usamos loadtxt ele irá carregar os dados de texto salvos ----- #
# ----- Quando usado dtype, estamos transformando os dados em int ---- #
