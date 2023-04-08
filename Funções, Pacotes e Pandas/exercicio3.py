# ---------------------------------------------------------------------------- #
#                                DESAFIO - ZIP()                               #
# ---------------------------------------------------------------------------- #

# --- Duas ferramentas bastante utilizadas quando iteramos com tuplas são o -- #
# ---------- desempacotamento de tuplas e a built-in function zip(). --------- #

# --------------------- Com o desempacotamento de tuplas, -------------------- #
# ------------ é possível fazer declarações conjuntas de variáveis ----------- #
# ---------- e utilizar cada variável individualmente. Por exemplo: ---------- #

nome, valor = ('Passat', 100000.0)

# ------------ A função zip() permite gerar um iterador de tuplas, ----------- #
# -------------------------- como no exemplo abaixo: ------------------------- #

nomes = ['Passat', 'Crossfox']
valores = [100000.0, 75000.0]
list(zip(nomes, valores))

# ----------------------------------- OUT: ----------------------------------- #
# --------------- [('Passat', 100000.0), ('Crossfox', 75000.0)] -------------- #


# -------------------- Considerando as duas listas abaixo: ------------------- #
nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]

# --------------- E utilizando o ferramental apresentado acima, -------------- #
# ------------ marque a alternativa com o código que possibilita a ----------- #
# -- impressão dos nomes dos veículos com quilometragem abaixo de 20.000 km. - #

list(zip(nomes,kms))

for nomes, kms in zip(nomes,kms):
    if (kms < 20000):
        print(nomes,kms)