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
