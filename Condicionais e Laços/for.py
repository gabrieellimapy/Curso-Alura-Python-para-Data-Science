# ---------------------------------------------------------------------------- #
#                                 FOR EM PYTHON                                #
# ---------------------------------------------------------------------------- #|

# ---- Instrução que permite que façamos iterações em instruções no python --- #

# ---------------------------------------------------------------------------- #
#                                    Formato                                   #
# ---------------------------------------------------------------------------- #
# ----------------------- for <variável> in <coleção>: ----------------------- #
# ------------------------------- <instruções> ------------------------------- #

Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios

# ------------- Vamos fazer uma varredura na lista, separadamente ------------ #

for item in Acessorios:
    print(item)
    

range(10) #gerar iterador de temanho 10
list(range(10))

for i in range(10): #faz a verredura, executa a iteração e mostra resultados
    print(i ** 2)
    
quadrado = [] #Gravando o valor de uma lista vazia e gerando um laço com 10 valores que serão impressos ao quadrado
for i in range(10):
    quadrado.append(1** 2)
    
quadrado

[1** 2 for i in range(10)]  #Maneira simples de fazer a lista com range