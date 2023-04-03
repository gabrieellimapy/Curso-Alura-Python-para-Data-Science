# ---------------------------------------------------------------------------- #
#                               TIPOS DE IF ELSE                               #
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

carrozero, carrousado = [], []
for lista in dados:
    if (lista[2] == True):
        carrozero.append(lista)
    else:
        carrousado.append(lista)
        
carrozero

carrousado


# ---------------------------------------------------------------------------- #
#                                     ELIF                                     #
# ---------------------------------------------------------------------------- #

# ----------------------------- Formatação Padrão ---------------------------- #

#if <condição 1>:
    #<instruções caso a condição 1 seja verdadeira>
#elif <condição 2>:
    #<instruções caso a condição 2 seja verdadeira>
#elif <condição 3>:
    #<instruções caso a condição 3 seja verdadeira>
   #                     .
   #                     .
   #                     .
#else:
    #<instruções caso as condições anteriores não sejam verdadeiras>
    
dados

# ------------------------- Separar veículos por anos ------------------------ #

A, B, C = [], [], []
for lista in dados:
    if(lista[1] <= 2000):
        A.append(lista)
    elif(lista[1] > 2000 and lista[1]<= 2010):
        B.append(lista)
    else:
        C.append(lista)
        
A
B
C

# ---------------------------------------------------------------------------- #
#                      Maneira mais simples de usar o elif                     #
# ---------------------------------------------------------------------------- #

A, B, C = [], [], []
for lista in dados:
    if(lista[1] <= 2000):
        A.append(lista)
    elif(2000 < lista[1]<= 2010):
        B.append(lista)
    else:
        C.append(lista)

A
B
C


# ---------------------------------------------------------------------------- #
#                                 OPERADOR AND                                 #
# ---------------------------------------------------------------------------- #

print('AND')
print(f'(True and True) o resultado é: {True and True}')
# -------------------------------- Saída= True ------------------------------- #
print(f'(True and False) o resultado é: {True and False}')
# ------------------------------- Saída= False ------------------------------- #
print(f'(False and True) o resultado é: {False and True}')
# ------------------------------- Saída= False ------------------------------- #
print(f'(False and False) o resultado é: {False and False}')
# ------------------------------- Saída: False ------------------------------- #


# ---------------------------------------------------------------------------- #
#                                  OPERADOR OR                                 #
# ---------------------------------------------------------------------------- #

print('OR')
print(f'(True or True) o resultado é: {True or True}')
# ------------------------------- Saída = True ------------------------------- #
print(f'(True or False) o resultado é: {True or False}')
# ------------------------------- Saída = True ------------------------------- #
print(f'(False or True) o resultado é: {False or True}')
# ------------------------------- Saída = True ------------------------------- #
print(f'(False or False) o resultado é: {False or False}')
# ------------------------------- Saída = False ------------------------------ #