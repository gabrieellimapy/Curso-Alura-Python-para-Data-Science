dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        result.update({ item[0]: media })
    return result      
    

km_media(dados, 2019)

#out:

#{'Crossfox': 2500.0,
# 'DS5': 4250.0,
# 'Fusca': 3250.0,
#'Jetta': 7000.0,
# 'Passat': 3100.0}