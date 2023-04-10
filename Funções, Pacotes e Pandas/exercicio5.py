# ---------------------------------------------------------------------------- #
#                  DESAFIO - OPERAÇÕES BÁSICAS COM DICIONÁRIOS                 #
# ---------------------------------------------------------------------------- #

# ----------- Utilize o dicionário dados para responder a questão: ----------- #

dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    }, 
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

# --- Note que dados tem dois itens, onde a chave (key) é o nome do veículo -- #
# --- e o valor (value) é um dicionário com informações sobre este veículo --- #
# ----------------- (ano, quilometragem, valor e acessórios). ---------------- #
# ---------------------- Nossa tarefa nesta atividade é ---------------------- #
# ----------- aprender como acessar as informações de um dicionário ---------- #
# ------------------------ dentro de outro dicionário. ----------------------- #
# --------------------------- Queremos o seguinte: --------------------------- #

# ------------------ 1) Testar se a chave acessorios existe ------------------ #
# ----- no dicionário de informações do carro Crossfox (Resposta: False) ----- #

# ----------------- 2) Testar se a chave acessorios existe no ---------------- #
# -------- dicionário de informações do carro Passat (Resposta: True) -------- #

# ----------- 3) Obter o valor do carro Crossfox (Resposta: 25000) ----------- #

# ------ 4) Acessar o último acessório do carro Passat (Resposta: 'ABS') ----- #

# ---- Assinale a alternativa que mostra os códigos corretos para retornar --- #
# - e acessar as informações acima (Dica: utilize um notebook para verificar - #
# ----------------------- os códigos desta atividade): ----------------------- #

'acessorios' in dados['Crossfox'] #Out: False

'acessorios' in dados['Passat'] #Out: True

dados['Crossfox']['valor'] #Out: 25000

'acessorios' in dados['Passat']['Acessorios'][-1] #Out: ABS