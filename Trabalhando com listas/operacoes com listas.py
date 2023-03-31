# ---------------------------------------------------------------------------- #
#                             OPERAÇÕES COM LISTAS                             #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#                                    X IN A                                    #
# ---------------------------------------------------------------------------- #
# ---------- Retorna True quando os itens da lista A são iguais a X ---------- #
Acessorios = ['Rodas de Liga','Travas Eletricas','Piloto automático', 'Bancos de couro', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
Acessorios
"Rodas de Liga" in Acessorios #Retorna true pois o item existe na lista
'4 X 4' in Acessorios #Retorna false pois o item não existe na lista
'Rodas de Liga' not in Acessorios #Retorna false pois o item está dentro da lista
'4 x 4' not in Acessorios #Retorna true pois o item realmente não está dentro da lista 


# ---------------------------------------------------------------------------- #
#                               CONCATENAR LISTAS                              #
# ---------------------------------------------------------------------------- #

A = ['Rodas de Liga','Travas Eletricas','Piloto automático', 'Bancos de couro']
B = ['Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
A + B
len(Acessorios)