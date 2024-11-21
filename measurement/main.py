from measurement.conversores.metrico import main_metrico
from measurement.conversores.imperial import main_imperial

def conversao_medida(SistemaOrigem, SistemaDestino):
    if SistemaOrigem == 'métrico' and SistemaDestino == 'imperial':
        return main_metrico()
    elif SistemaOrigem == 'imperial' and SistemaDestino == 'métrico':
        return main_imperial()
    else:
        return 'Conversão não suportada'


print(conversao_medida('métrico', 'imperial'))