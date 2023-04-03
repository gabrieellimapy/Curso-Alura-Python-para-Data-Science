# ---------------------------------------------------------------------------- #
#                                 IF EM PYTHON                                 #
# ---------------------------------------------------------------------------- #

# ------------------------------ formato padrão ------------------------------ #

#if <condicao>
    #<instruções> caso acondicao for verdadeira
    
# ------------------------- Operadores de comparação ------------------------- #
# ---------------------------- == Exatamente igual --------------------------- #
# ------------------------------- != Diferente ------------------------------- #
# -------------------------------- > Maior que ------------------------------- #
# -------------------------------- < Menor que ------------------------------- #
# ----------------------------- >= Maior ou Igual ---------------------------- #
# ---------------------------- <=  Menor ou igual ---------------------------- #

# ---------------------------------------------------------------------------- #
#                       Operadores lógicos: And, Or e Not                      #
# ---------------------------------------------------------------------------- #

# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
dados

# ------ Varredura da lista, no índice para verificar se o veículo é 0km ----- #
# ---------- Depois, insere os veículos 0km dentro de uma nova lista --------- #
zerokm_y = []
for lista in dados:
    if (list[2] == True) :
        zerokm_y.append(lista)
zerokm_y

# -------------- Varredura na lista para carros que não são 0km -------------- #
# ---------- Depois, inserção dos veículos que não são 0km na lista ---------- #
zerokm_n = []
for lista in dados:
    if (list[2] == False):
        zerokm_n.append(lista)
zerokm_n

# ---------------------------------------------------------------------------- #
#                            Comprimindo a listagem                            #
# ---------------------------------------------------------------------------- #

[lista for lista in dados (lista[2] == True)]