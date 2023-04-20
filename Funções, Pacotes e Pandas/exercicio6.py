dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    for item in dataset.itens():
        result = item[1]['km'] / (ano_atual - item[1]['ano'])
        print(result)

km_media(dados, 2019)


