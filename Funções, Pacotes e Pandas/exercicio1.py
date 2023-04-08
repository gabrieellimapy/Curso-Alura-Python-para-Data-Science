# ---------------------------------------------------------------------------- #
#                    DESAFIO - SELECIONANDO ITENS EM TUPULAS                   #
# ---------------------------------------------------------------------------- #

# -------- Em nosso primeiro treinamento de Python para Data Science, -------- #
# - nós aprendemos como fazer seleções de itens em listas e em arrays Numpy. - #
# ------ O procedimento para seleções em tuplas funciona da mesma forma. ----- #
# ------------------------ Considere a seguinte tupla: ----------------------- #

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

# ------------- Considere também os seguintes códigos de seleção: ------------ #

# ------------------------------ 1) carros[0][3] ----------------------------- #

# --------------------------- 2) carros[-1][-1][-1] -------------------------- #

# --------------------------- 3) carros[0][-1][:2] --------------------------- #

# -- Assinale a alternativa que mostra o resultado obtido com os códigos de -- #
# ------------------------------ seleção acima. ------------------------------ #

carros[0][3]
# -------------------------------- Out: False -------------------------------- #
carros[-1][-1][-1]
# ------------------------------ Out: Freios ABS ----------------------------- #
carros[0][-1][:2]
# ---------------- Out: ('Rodas de liga', 'Travas elétricas') ---------------- #