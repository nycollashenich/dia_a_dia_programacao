FatoresMetrosImperial = {
    'polegada' : 0.0254,
    'pés' : 0.3048,
    'jarda' : 0.9144,
    'milha' : 1609.34,
    'metro' : 1
}

def ImperialConversaoMetro(valor, unidade_origem):
    if unidade_origem in FatoresMetrosImperial:
        return valor * FatoresMetrosImperial[unidade_origem]

def ImperialMetroDestino(valor_em_metros, unidade_destino):
    if unidade_destino in FatoresMetrosImperial:
        return valor_em_metros / FatoresMetrosImperial[unidade_destino]
