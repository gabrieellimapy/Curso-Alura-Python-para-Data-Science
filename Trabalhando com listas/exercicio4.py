# ---------------------------------------------------------------------------- #
#                       DESAFIO - ELABORAÇÕES COM LISTAS                       #
# ---------------------------------------------------------------------------- #
#Considere a seguinte lista do Python e o resultado obtido após um conjunto de manipulações:

#In [1]:

#Acessorios = [
    #'Rodas de liga', 
    #'Travas elétricas', 
    #'Piloto automático',
    #'Bancos de couro',
    #'Ar condicionado'
#]

#In [2]: Qual código?

#Out [2]:

#['Airbag',
 #'Ar condicionado',
 #'Bancos de couro',
 #Piloto automático',
 #'Rodas de liga',
 #'Vidros elétricos']
 
#Assinale a alternativa que apresenta o código executado na célula In [2].

Acessorios = [
    'Rodas de liga', 
    'Travas elétricas', 
    'Piloto automático',
    'Bancos de couro',
    'Ar condicionado'
]

Acessorios.append('Airbag')
Acessorios.sort()
Acessorios.pop()
Acessorios.append('Vidros Elétricos')
Acessorios