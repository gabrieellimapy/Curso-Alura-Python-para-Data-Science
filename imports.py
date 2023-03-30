# ---------------------------------------------------------------------------- #
#                         COMO IMPORTAR LIBS NO PYTHON                         #
# ---------------------------------------------------------------------------- #
from random import randrange, seed
seed(11)
# ------ Criando uma lista com valores aleatórios definidos no randrange ----- #
notas_matematica = []
notas_matematica.append(randrange(0,11))
notas_matematica

# -------------------- Gerando uma lista com oito valrores ------------------- #
notas_matematica2 = []
for nota in range(8):
    notas_matematica2.append(randrange(0,11))
notas_matematica2;

# ---------------------- Consultando o tamanho da lista ---------------------- #
len (notas_matematica)
len (notas_matematica2)

