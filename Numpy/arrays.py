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


# ---------------------------------------------------------------------------- #
#                      Atributos e métodos de Arrays Numpy                     #
# ---------------------------------------------------------------------------- #

dados = np.array([44410, 5712, 37123, 0., 25757],
                 [2003, 1991, 1990, 2019, 2006])


# ---------------------------------------------------------------------------- #
#                                     Shape                                    #
# ---------------------------------------------------------------------------- #
# --------------- Retorna uma tupula com as dimensões do array --------------- #

dados.shape

# -------------------------------- Out: (4, 3) ------------------------------- #
# --------------------- Quantas linhas e quantas colunas --------------------- #


# ---------------------------------------------------------------------------- #
#                                     Ndim                                     #
# ---------------------------------------------------------------------------- #
# ------------------ Retorna o número de dimensões do array ------------------ #

dados.ndim

# --------------------------------- Out: (2) --------------------------------- #
# ------------------------------ Duas dimensões ------------------------------ #


# ---------------------------------------------------------------------------- #
#                                     Size                                     #
# ---------------------------------------------------------------------------- #
# ------------------ Números de elementos que temos no array ----------------- #

dados.size

# --------------------------------- Out: (12) -------------------------------- #
# ---------------------- Número de dados dentro do array --------------------- #

# ---------------------------------------------------------------------------- #
#                                     Dtype                                    #
# ---------------------------------------------------------------------------- #
# ------------------- Retorna o tipo dos elementos do array ------------------ #

dados.dtype

# ----------------------------- Out: dtype('<U9') ---------------------------- #
# ----------------- Retorna tipo float para os dados do array ---------------- #

# ---------------------------------------------------------------------------- #
#                                       T                                      #
# ---------------------------------------------------------------------------- #
# ------------------ Converte linhas em colunas e vice-versa ----------------- #

dados.T

# ------------------------------- Out: dados.T ------------------------------- #
#array([['Roberto', 'Sheila', 'Bruno', 'Rita'],
       #['casado', 'solteira', 'solteiro', 'casada'],
       #['masculino', 'feminino', 'masculino', 'feminino']], dtype='<U9')
       
# -------------------- Equivalente ao Transpose do Python -------------------- #


# ---------------------------------------------------------------------------- #
#                               Métodos em Python                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                   To List()                                  #
# ---------------------------------------------------------------------------- #

# ------------- Transforma um array Numpy em uma lista do Python ------------- #

dados.tolist()

# ----------------------------------- Out: ----------------------------------- #
# ------------------------------ dados.tolist() ------------------------------ #
# ------------------- [['Roberto', 'casado', 'masculino'], ------------------- #
# -------------------- ['Sheila', 'solteira', 'feminino'], ------------------- #
# -------------------- ['Bruno', 'solteiro', 'masculino'], ------------------- #
# ---------------------- ['Rita', 'casada', 'feminino']] --------------------- #

# ---------------------------------------------------------------------------- #
#                            Reshape (shape[order])                            #
# ---------------------------------------------------------------------------- #

# ------ Retorna um array que contém os mesmos dados, com uma nova forma ----- #

contadore = np.arange(10)
contadore

contadore.reshape(5, 2)

# ------------- É possível usar formatações de outras linguagens ------------- #

# -------------------- Formatador linguagem C para reshape ------------------- #

contadore.reshape((5,2), order='C')

# ---------------------------- Out: array([[0, 1], --------------------------- #
# ---------------------------------- [2, 3], --------------------------------- #
# ---------------------------------- [4, 5], --------------------------------- #
# ---------------------------------- [6, 7], --------------------------------- #
# --------------------------------- [8, 9]]) --------------------------------- #


# -------------------- Formatador linguagem F para reshape ------------------- #

contadore.reshape((5,2), order='F')

# ------------------------------ Concatenando.. ------------------------------ #

km = [44410, 5712, 37123, 0, 25757]
anos = [2003, 1991, 1990, 2019, 2006]

info_carros = km + anos
info_carros

np.array(info_carros).reshape((2, 5))

# ----------------------------------- Out: ----------------------------------- #
# ----------------------------------- array ---------------------------------- #
# ------------------ ([[44410,  5712, 37123,     0, 25757], ------------------ #
# ------------------- [ 2003,  1991,  1990,  2019,  2006]]) ------------------ #

np.array(info_carros).reshape((5, 2), order = 'F')

# -------------------------------- Out: array -------------------------------- #
# ----------------------------- ([[44410,  2003], ---------------------------- #
# ------------------------------ [ 5712,  1991], ----------------------------- #
# ------------------------------ [37123,  1990], ----------------------------- #
# ------------------------------ [    0,  2019], ----------------------------- #
# ----------------------------- [25757,  2006]]) ----------------------------- #

# ---------------------------------------------------------------------------- #
#                                    Rezise                                    #
# ---------------------------------------------------------------------------- #

# -------------------- Altera a forma e o tamanho do array ------------------- #

dados_new = dados.copy()
dados_new

# ------------------------- Adicionar mais uma linha ------------------------- #

dados_new.resize((3, 5), refcheck=False) #ignorando checkagem de referência
dados_new

# ------------ Adicionando elementos na nova linha dentro da lista ----------- #
# ------------- Adicionando valor de km_ano dentro da nova linha ------------- #

dados_new[2] = dados_new[0] / (2019 - dados_new[1])
dados_new


# ---------------------------------------------------------------------------- #
#                         Estatísticas com Arrays Numpy                        #
# ---------------------------------------------------------------------------- #

anos = np.loadtxt(fname = "Numpy/dados/carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "Numpy/dados/carros-km.txt")
valor = np.loadtxt(fname = "Numpy/dados/carros-valor.txt")

# ------------------------- Medindo tamanho de array ------------------------- #
anos.shape

# ---------------------------------------------------------------------------- #
#                              Uso de Column Stack                             #
# ---------------------------------------------------------------------------- #

# --- Transforma arrays unidimensionais em colunas de array bidimensionais --- #

dataset = np.column_stack((anos, km, valor))
dataset
dataset.shape

# ---------------------------------------------------------------------------- #
#                                    Np.mean                                   #
# ---------------------------------------------------------------------------- #

# --------- Retorna uma média dos elementos do array ao longo do eixo -------- #

np.mean(dataset, axis = 0) #tira a média de cada uma das colunas

np.mean(dataset, axis = 1) #tira a média por linha

np.mean(dataset[:, 1]) #Usando um slice

np.mean(dataset[:, 2])

# ---------------------------------------------------------------------------- #
#                                   np.std()                                   #
# ---------------------------------------------------------------------------- #

# ----- Retorna o desvio padrão dos elementos do array dentro de um eixo ----- #

np.std(dataset[:, 1])

# ---------------------------------------------------------------------------- #
#                                 ndarray.sum()                                #
# ---------------------------------------------------------------------------- #

# ---- Retorna a soma dos elementos do array ao longo do eixo especificado --- #

dataset.sum(axis = 0)

dataset[:, 1].sum()

# ---------------------------------------------------------------------------- #
#                                   np.sum()                                   #
# ---------------------------------------------------------------------------- #

# -- Retorna a soma dos elementos de um array ao longo do eixo especificado -- #

np.sum(dataset, axis=0)

np.sum(dataset[:, 1])