# ---------------------------------------------------------------------------- #
#                                Loops aninhados                               #
# ---------------------------------------------------------------------------- #
# ---------------- Instruçaõ for dentro de outra instrução for --------------- #
dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados

# ----------- Identificar quais acessórios temos dentro do data set ---------- #

for lista in dados:
    print(lista)
    
# Para varrer as três listas
for lista in dados:
    for item in lista:
        print(item)

# pegar apenas os itens individualmenmte

Acessorios = []
for lista in dados:
    for item in lista:
        Acessorios.append(item)
Acessorios

# ---------------------------------------------------------------------------- #
#                                     SET()                                    #
# ---------------------------------------------------------------------------- #

set(Acessorios) 

list (set(Acessorios))
# ---------------------------------------------------------------------------- #
#                              List Compehensions                              #
# ---------------------------------------------------------------------------- #
list(set([item for lista in dados for item in lista]))