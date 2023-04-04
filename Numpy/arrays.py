# ---------------------------------------------------------------------------- #
#                             CRIANDO ARRAYS NUMPY                             #
# ---------------------------------------------------------------------------- #

# ---------------------------- A partir de listas ---------------------------- #
import numpy as np
km = np.array ([3000, 2400, 4987, 1500])
km
# ------------------------ A partir de dados externos ------------------------ #
km = np.loadtxt(fname='Numpy/dados/carros-km.txt', dtype=int)
km
# ------------------------- Arrays com duas dimensões ------------------------ #
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
Acessorios = np.array(dados)
# --------------------- Comparando desempenho com listas --------------------- #
np_array = np.arange(1000000)
py_list = list(range(1000000))
np_array
py_list
#vê o desempenho da linha de código que estamos utilizando

# ---------------------------------------------------------------------------- #
#                        Operações Aritiméticas no Numpy                       #
# ---------------------------------------------------------------------------- #

# -------------------- Operações entre Arrays e Constantes ------------------- #

km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]

#idade = 2023 - anos
# --------------- Out: Erro de tipos, int não interage com list -------------- #

# ------------------- No Numpy, funciona da seguinte forma: ------------------- #

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2023 - anos
idade

# ---------------------------------------------------------------------------- #
#                            Operações entre Arrays                            #
# ---------------------------------------------------------------------------- #

km_media = km / idade
km_media

# ---------------------------------------------------------------------------- #
#                    Operações com Arrays de duas dimensões                    #
# ---------------------------------------------------------------------------- #

dados = np.array([km, anos]) #Matriz onde agrupa os arrays e contabiliza os dados da melhor forma possível
dados.shape #Duas linhas e cinco colunas

# ------------------------- Como acessar estes dados? ------------------------ #

km_media = dados[0] / (2023 - dados[1])
km_media

# ---------------------------------------------------------------------------- #
#                           Seleções com Arrays Numpy                          #
# ---------------------------------------------------------------------------- #

contador = np.arange(10)
contador

contador[0]

item = 6
index = item - 1
contador[index]

contador = -1
# ------------ Acima, uma criação de contador para buscar indíces ------------ #

# ---------------------- Como buscar valores nos arrays ---------------------- #

dados[0] [1]
dados[1,1]

# ---------------------------------------------------------------------------- #
#                              FATIAMENTOS - SLICE                             #
# ---------------------------------------------------------------------------- #

#A sintaxe para realizar fatiamento em um array Numpy é i:j:k onde i é o índice inicial, j é o índice de parada, e k é o indicador de passo (k≠0)

#Observação: Nos fatiamentos (slices) o item com índice i é incluído e o item com índice j não é incluído no resultado.

contador = np.arange(10)
contador

contador[1:4]

# ------------------------------- Out: 1, 2 e 3 ------------------------------ #

contador[1:8:2]

# ------------------------------- Out: 1,3,5,7 ------------------------------- #

contador[::2]

# -------------------------- Out: ([0, 2, 4, 6, 8]) -------------------------- #

contador[1::2]

# -------------------------- Out: ([1, 3, 5, 7, 9]) -------------------------- #

dados[:, 1:4]

# ---------------------- Out: [[ 5712., 37123.,     0.], --------------------- #
# ------------------------ [ 1991.,  1990.,  2019.]]) ------------------------ #

dados[:, 1:3]

# ------------------------- out: ([[ 5712., 37123.], ------------------------- #
# ---------------------------- [ 1991.,  1990.]]) ---------------------------- #

dados [:, 1:3][0] / (2023 - dados[:, 1:3][1])

# ------------------- Out: ([ 178.5       , 1124.93939394]) ------------------ #

# ---------------------------------------------------------------------------- #
#                        Indexação por arrays booleanos                        #
# ---------------------------------------------------------------------------- #

contador = np.arange(10)
contador
