# ---------------------------------------------------------------------------- #
#                         DESAFIO - LIST COMPREHENSIONS                        #
# ---------------------------------------------------------------------------- #

# -------------------------- Observe o código abaixo ------------------------- #
quadrado = []
for i in range(10):
  quadrado.append(i ** 2)

quadrado

# --------------- Saída = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] --------------- #

# Selecione a alternatia que representa a forma correta de criar
# de forma concisa a mesma lista do código acima

[i ** 2 for i in range(10)]