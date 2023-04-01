# ---------------------------------------------------------------------------- #
#                               MÉTODOS DE LISTAS                              #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                   A.sort()                                   #
# ---------------------------------------------------------------------------- #
Acessorios = ['Rodas de Liga','Travas Eletricas','Piloto automático', 'Bancos de couro', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

# ----------------------------- Ordena a lista A ----------------------------- #
Acessorios.sort()
Acessorios

# ---------------------------------------------------------------------------- #
#                                  A.append(x)                                 #
# ---------------------------------------------------------------------------- #

# ----------------- Adiciona o elemento x no final da lista A ---------------- #
Acessorios.append('4 X 4')
Acessorios

# ---------------------------------------------------------------------------- #
#                                   A.pop(i)                                   #
# ---------------------------------------------------------------------------- #

# --------- Se não definido argumento no final, exclui o último item --------- #
Acessorios.pop(2)
Acessorios

# ---------------------------------------------------------------------------- #
#                           Gerando cópias das listas                          #
# ---------------------------------------------------------------------------- #

Acessorios_2 = Acessorios.copy()
Acessorios_2

# ---------------------------- O mesmo acontece em --------------------------- #
Acessorios_3 = Acessorios[:]
Acessorios_3