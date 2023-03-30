# ---------------------------------------------------------------------------- #
#                       COMO CRIAR CONDICIONAIS NO PYTHON                      #
# ---------------------------------------------------------------------------- #

# ----------- Verifica se o usuário pode ou não dirigir pela idade ----------- #

idade_cpf = 19
def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')
verifica_se_pode_dirigir(idade_cpf)


# ---------------------------------------------------------------------------- #
#                   CRIAR CONDICIONAIS COM CONVERSÃO DE TIPO                   #
# ---------------------------------------------------------------------------- #

def vrfyyrs():
    yrold = input('Qual sua idade?')
    yrold = int(yrold)
    if yrold >= 18:
        print('Tem permissão para dirigir')
    else:
        print(f'Não tem permissão para dirigir, aguarde {18 - yrold} para habilitar-se')
vrfyyrs()