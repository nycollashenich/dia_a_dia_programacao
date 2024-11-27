FatoresMetrosMetrico = {
    'mm' : 0.001, # 1 milimetro = 0.001m
    'cm' : 0.01, # 1 centimetro = 0.01m
    'dm' : 0.1, # 1 decímetro = 0.01m
    'm' : 1, # metro é igual a 1m
    'dam' : 10, # 1 decametro = 10m 
    'hec' : 100, # 1 hectometro = 100m
    'km' : 1000 # 1 km = 1000m
}

def MetricoConversaoMetro(valor, unidade_origem):
    if unidade_origem in FatoresMetrosMetrico: # verifica se a medida inicial está no dicionário (fatores_metros)
        return valor * FatoresMetrosMetrico[unidade_origem]

def MetricoMetroDestino(valor_em_metros, unidade_destino):
    if unidade_destino in FatoresMetrosMetrico:
        return valor_em_metros / FatoresMetrosMetrico[unidade_destino]
