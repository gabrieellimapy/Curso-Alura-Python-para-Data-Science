# ---------------------------------------------------------------------------- #
#                      COMO CRIAR LAÇOS E LOOPS NO PYTHON                      #
# ---------------------------------------------------------------------------- #
idades = [10,20,63,95,12,11]
# ------------------------------ Fora da função ------------------------------ #
def habilita_direcao(idade):
    if idade >= 18:
        print(f'{idade} anos de idade, tem permissão para dirigir')
    else:
        print(f'{idade} anos de idade, NÃO tem permissão para dirigir')
for idade in idades:
    habilita_direcao(idade)

# ----------------------------- Dentro da função ----------------------------- #
def habilita_direcao(idades):
    for idade in idades:
        if idade >= 18:
            print(f'{idade} anos de idade, tem permissão para dirigir')
        else:
            print(f'{idade} anos de idade, não tem permissão para dirigir')
habilita_direcao(idades)