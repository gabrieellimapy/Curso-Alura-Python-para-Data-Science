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