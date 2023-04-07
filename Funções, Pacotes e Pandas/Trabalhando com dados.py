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

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox,', 'Dss'])

# ----------- Como ver o tipo de um dado no python (retorna tuple) ----------- #
type(nomes_carros)
