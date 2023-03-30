# ---------------------------------------------------------------------------- #
#                       COMO FAZER FUNÇÕES COM PARÂMETROS                      #
# ---------------------------------------------------------------------------- #
# -------- Normalmente é definido o parâmetro da função fora da função ------- #
nomefunction = 'luisa'
def funcaonome():
    print(f'Olá {nomefunction}!')
funcaonome()
# ---------- Porém é possível definir os parâmetros dentro da função --------- #
def funcaodentroparam(nomefuncao):
    print(f'olá {nomefuncao}')
funcaodentroparam(nomefunction)
