# ---------------------------------------------------------------------------- #
#                        Trabalhando com dados em Python                       #
# ---------------------------------------------------------------------------- #

# ----------------------------- Importando pandas ---------------------------- #
import pandas as pd
pd.set_option('display.max_rows', 1000) #mostra o máximo de informações na tela
# ------------------- Para ver todas as linhas do database ------------------- #
pd.set_option('display.max_columns', 1000) #mostra o máximo de colunas na tela
# ------------------- Para ver todas as colunas do database ------------------ #
database = pd.read_csv('Funções, Pacotes e Pandas\data\db.csv', sep = ';') # ; separador usado no dataset
database
# --------------- Comando de leitura de arquivos CSV em pandas --------------- #
database.dtypes
# ------------------ Demonstra os tipos de dados da database ----------------- #

database[['Quilometragem', 'Valor']].describe()
# --------------- Gera um conjunto de estatísticas descritivas --------------- #
database.info()
# -------------- Demonstra as informações sobre a base de dados -------------- #

# ---------------------------------------------------------------------------- #
#                                CRIANDO TUPULAS                               #
# ---------------------------------------------------------------------------- #

# ----- Tupulas são sequencias imutáveis para armazenar coleções de itens ---- #
# ------ geralmente heterogeneos podem ser constituídas de várias formas ----- #
# ------------------------- Utilizando paranteses () ------------------------- #
# -------------------- Utilizando uma vírgula a direita x, ------------------- #
# - Utilizando um par de parenteses e itens separados por virgulas (x, y, z) - #
# ------------------ Utilizando: tuple() ou tuple(iterador) ------------------ #

# --------------------- Criando uma tupula com variáveis --------------------- #
nome = 'Passat'
valor = 153000
(nome, valor)

# --------------- Criando uma tupula com valores pré definidos --------------- #

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox,', 'DSS'])

# ----------- Como ver o tipo de um dado no python (retorna tuple) ----------- #
type(nomes_carros)


# ---------------------------------------------------------------------------- #
#                              Seleções em Tupulas                             #
# ---------------------------------------------------------------------------- #

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox,', 'DS5'])
nomes_carros

# ----------------- Indexação começa em zero igual os arrays ----------------- #

# ----------------------- Para acessar o primeiro item ----------------------- #
nomes_carros[0]
# ------------------------------- Segundo Item ------------------------------- #
nomes_carros[1]
# ---------------------- Como acessar o último elemento ---------------------- #
nomes_carros[-1]
# -------------------------- Como fazer indice slice ------------------------- #
nomes_carros[1:3]
# ------------------------- Tupula com tupula dentro ------------------------- #
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
# ----------------------- Acessando itens de uma tupula ---------------------- #
nomes_carros[-1][0]

# ---------------------------------------------------------------------------- #
#                             ITERAÇÕES COM TUPULAS                            #
# ---------------------------------------------------------------------------- #

nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
for item in nomes_carros:
    print(item)
# --------- Atribuindo valores de variáveis a tupula respectivamente --------- #
# -------------------------- Desempacotando tupulas -------------------------- #
carro_1, carro_2, carro_3, carro_4 = nomes_carros
carro_1
# ---------------------------- Out: Jetta Variant ---------------------------- #

# ------ Especificando valores de variáveis conforme sequencia de lista ------ #
_, A, _, B, = nomes_carros
A

# ----------------------- Especificando um único valor ----------------------- #
_, C,*_ = nomes_carros
C

# ---------------------------------------------------------------------------- #
#                                     ZIP()                                    #
# ---------------------------------------------------------------------------- #

# ----------------------- Cria um iterador com tupulas ----------------------- #
carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
carros

valores = [88078.64, 106161.94, 72832.16, 124549.07]
valores

list(zip(carros, valores))

# --- A iteração junta os valores das túpulas com seus respectivos indices --- #

# -------------------- Out: [('Jetta Variant', 88078.64), -------------------- #
# -------------------------- ('Passat', 106161.94), -------------------------- #
# -------------------------- ('Crossfox', 72832.16), ------------------------- #
# ---------------------------- ('DS5', 124549.07)] --------------------------- #

for item in zip(carros, valores):
    print(item)

for carro, valor in zip(carros, valores):
  print(carro, valor)
  
# ---------------------- Usando operadores condicionais ---------------------- #

for carro, valor in zip(carros, valores):
    if (valor >= 100000):
        print(carro, valor)
        

# ---------------------------------------------------------------------------- #
#                              CRIANDO DICIONÁRIOS                             #
# ---------------------------------------------------------------------------- #

# ----------------- Listas são coleções sequenciais, isto é, ----------------- #
# ---------------- os itens destas sequências estão ordenados ---------------- #
# ------ e utilizam índices (números inteiros) para acessar os valores. ------ #
# ------------- Os dicionários são coleções um pouco diferentes. ------------- #
# ------ São estruturas de dados que representam um tipo de mapeamento. ------ #
# ---- Mapeamentos são coleções de associações entre pares de valores onde --- #
# ---------- o primeiro elemento do par é conhecido como chave (key) --------- #
# ---------------------- e o segundo como valor (value). --------------------- #

# ---- dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n} ---- #

carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros

valores = [88078.64, 106161.94, 72832.16]
valores

carros.index('Passat')
valores[carros.index('Passat')]

# ----------------- Criar uma estrutura que faz os mapeamentos ---------------- #

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

type(dados)

# ---------------------------------------------------------------------------- #
#                         Criando dicionários com ZIP()                        #
# ---------------------------------------------------------------------------- #

list(zip(carros, valores))
dados = dict(zip(carros, valores)) #Built Function DICT


# ---------------------------------------------------------------------------- #
#                           OPERAÇÕES COM DICIONÁRIOS                          #
# ---------------------------------------------------------------------------- #

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

# ---------------------------------------------------------------------------- #
#                                   Dict[key]                                  #
# ---------------------------------------------------------------------------- #
# -------- Retorna o valor correspondente a chave (key) no dicionário -------- #

dados['Passat']

# ------------------------------ Out: 106161.94 ------------------------------ #

# ---------------------------------------------------------------------------- #
#                                  Key in dict                                 #
# ---------------------------------------------------------------------------- #
# -------- Retorna True se a chave (key) for encontrada no dicionário -------- #

'Passat' in dados

'Fusca' in dados
 
'Fusca' not in dados

# ---------------------------------------------------------------------------- #
#                                   len(dict)                                  #
# ---------------------------------------------------------------------------- #

# ----------------------- Número de itens no dicionário ---------------------- #

len(dados)

# ---------------------------------------------------------------------------- #
#                               dict[key] = value                              #
# ---------------------------------------------------------------------------- #

# ------------------ retorna o número de itens do dicionário ----------------- #

dados['DS5'] = 124549.07

# ---------------------------------------------------------------------------- #
#                                 del dict[key]                                #
# ---------------------------------------------------------------------------- #

# ------------------- remove o item de chave do dicionário ------------------- #

del dados['Passat']
