from sistema_metrico import metrico
from sistema_imperial import imperial

def conversao_medida(value, SistemaOrigem, SistemaDestino):
    if SistemaOrigem == 'métrico' and SistemaDestino == 'imperial':
        return metrico(value)
    elif SistemaOrigem == 'imperial' and SistemaDestino == 'métrico':
        return imperial(value)
    else:
        return 'Conversão não suportada'

value = 100
print(conversao_medida(value, 'métrico', 'imperial'))