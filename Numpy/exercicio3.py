# ---------------------------------------------------------------------------- #
#                     DESAFIO - OBTENDO A MÉDIA ARITIMETICA                    #
# ---------------------------------------------------------------------------- #

# ----------------------- Considerando o array idades: ----------------------- #

import numpy as np

idades = np.array([10, 23, 45, 34, 25])

#Dentre as alternativas abaixo,
#quais são formas corretas de se obter a média aritmética das idades?

np.mean(idades, axis = 0)
