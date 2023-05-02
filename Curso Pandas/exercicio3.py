import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor Diesel', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])

# --------------------------------- Método 1 --------------------------------- #

dataset.query('Motor == "Motor Diesel" or Zero_km == True')

# --------------------------------- Método 2 --------------------------------- #

dataset[(dataset.Motor == 'Motor Diesel') | (dataset.Zero_KM == True)]

# --------------------------------- Método 3 --------------------------------- #

dataset.query('Motor == "Motor Diesel" | Zero_km == True')
