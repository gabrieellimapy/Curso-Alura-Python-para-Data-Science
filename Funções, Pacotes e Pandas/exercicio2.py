# ---------------------------------------------------------------------------- #
#                        DESAFIO - LAÇOS FOR COM TUPULAS                       #
# ---------------------------------------------------------------------------- #

# - O procedimento de iteração em tuplas é o mesmo que aprendemos com listas - #
# ---------------- no treinamento anterior. Utilizamos a tupla --------------- #
# ------------------- como iterador de um laço for simples ------------------- #
# ------ ou alinhado, e conseguimos acesso a cada item individualmente. ------ #
# ------------------------ Para responder esta questão ----------------------- #
# --------------- considere a mesma tupla da atividade anterior -------------- #

carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)

# ------- Observe que se trata de uma tupla (1º nível) com duas tuplas, ------ #
# ----- que representam um conjunto de dados de dois veículos (2º nível), ---- #
# ----------------- e que uma destas informações (acessórios) ---------------- #
# ---------------- vêm também dentro de uma tupla (3º nível). ---------------- #
# ----------------- O que precisamos é iterar na tupla carros ---------------- #
# --------------- e imprimir todos os acessórios que aparecem. --------------- #
# -------------------- O resultado desejado é o seguinte: -------------------- #

for tupula in carros:
    for item in tupula[-1]:
        print(item)