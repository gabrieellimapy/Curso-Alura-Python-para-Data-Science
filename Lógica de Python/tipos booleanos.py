# ---------------------------------------------------------------------------- #
#                     LISTAS COM TIPOS BOOLEANOS EM PYTHON                     #
# ---------------------------------------------------------------------------- #

# ------- Criando uma lista vazia que receberá as validações em boolean ------ #
permissoes = [] # Criando uma lista vazia para quando for feita a verificação, adicione dentro desta mesma lista
idades = [20, 14, 40]

def verifica_se_pode_dirigir(idades, permissoes):
    for idade in idades:
      if idade >= 18:
        permissoes.append(True) # Append é um método que adiciona os itens que passarem pela filtragem dentro da lista
      else:
        permissoes.append(False)

verifica_se_pode_dirigir(idades, permissoes)