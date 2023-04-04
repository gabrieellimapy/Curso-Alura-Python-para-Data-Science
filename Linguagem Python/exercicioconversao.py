# ---------------------------------------------------------------------------- #
#                          DESAFIO - CONCATENE A FRASE                         #
# ---------------------------------------------------------------------------- #

text = 'A quilometragem média do veículo é '
Km = 100000
Ano_atual = 2019
Ano_fabricacao = 1999

text + str( int( Km / (Ano_atual - Ano_fabricacao) ) ) + ' km'
#km estava em float, então usou-se int para converter a equação