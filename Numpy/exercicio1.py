# ---------------------------------------------------------------------------- #
#                             DESAFIO - CÁLCULO IMC                            #
# ---------------------------------------------------------------------------- #

#O IMC (índice de massa corporal) é um indicador utilizado para detectar situações de obesidade ou desnutrição.
#Para obter o IMC, basta calcular a razão entre o peso de um indivíduo (kg) e sua altura elevada ao quadrado, conforme mostra a fórmula abaixo:

# ------------------------------------ IMC ----------------------------------- #
# ----------------------------------- Peso ----------------------------------- #
# ----------------------------------- ---- ----------------------------------- #
# ---------------------------------- Altura ---------------------------------- #


import numpy as np

peso = np.array([106.0, 65.5, 75.0])
altura = np.array([1.9, 1.53, 1.75])

IMC = peso / altura ** 2
IMC

