# ---------------------------------------------------------------------------- #
#                             DESAFIO - FATIAMENTOS                            #
# ---------------------------------------------------------------------------- #

# ------------------------ Considere o seguinte array: ----------------------- #

import numpy as np

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteira', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casada', 'feminino']
    ]
)

#Marque a alternativa que mostra o código que permite a seleção, 
#sem utilização de operadores lógicos (and e or), 
#das informações de nome e estado civil, 
#somente das pessoas do sexo masculino.

dados[0::2, :2]
