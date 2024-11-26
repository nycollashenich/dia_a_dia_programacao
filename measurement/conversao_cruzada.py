from sistema_metrico.metrico import MetricoConversaoMetro, MetricoMetroDestino # 1º conversao para m, 2º conversao do metro para o destino
from sistema_imperial.imperial import ImperialConversaoMetro, ImperialMetroDestino # 1º conversao para m 2º conversao do metro para o destino


def ConverterEntreSistemas(sistema_origem, sistema_destino, unidade_origem, unidade_destino, valor):
    if sistema_origem == 'métrico' and sistema_destino == 'imperial':
        valor_em_metros = MetricoConversaoMetro(valor, unidade_origem)
        return ImperialMetroDestino(valor_em_metros, unidade_destino)
    
    elif sistema_origem == 'imperial' and sistema_destino == 'métrico':
        valor_em_metros = ImperialConversaoMetro(valor, unidade_origem)
        return MetricoMetroDestino(valor_em_metros, unidade_destino)
    
    elif sistema_origem == sistema_destino:
        return valor
    
    else:
        raise ValueError('Conversão entre sistemas não suportada.')