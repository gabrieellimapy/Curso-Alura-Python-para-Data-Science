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