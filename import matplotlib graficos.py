# ---------------------------------------------------------------------------- #
#                       IMPORTANDO O MATPLOTLIB NO PYTHON                      #
# ---------------------------------------------------------------------------- #

# --- É possível criar gráficos com diversas libs utilizaremos a matplotlib -- #
import matplotlib.pyplot as plt #definindo apelidos para libs
x = list(range(1,9))
y = nota_matematica
plt.plot(x,y, marker = 'o')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()