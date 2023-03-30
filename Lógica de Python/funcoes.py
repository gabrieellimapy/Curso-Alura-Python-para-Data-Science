# ---------------------------------------------------------------------------- #
#                         COMO CRIAR FUNÇÕES EM PYTHON                         #
# ---------------------------------------------------------------------------- #
def hello(): #def é o comando que abre a função
    nome = input('Qual seu nome? ') #input faz com que o usuário possa definir o nome
    print(f'Olá {nome}')
hello() #sempre fecha-se uma função chamando o nome da mesma com ()