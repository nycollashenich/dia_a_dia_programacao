FatoresMetrosMetrico = {
    'mm' : 0.001, # 1 milimetro = 0.001m
    'cm' : 0.01, # 1 centimetro = 0.01m
    'dm' : 0.1, # 1 decímetro = 0.01m
    'm' : 1, # metro é igual a 1m
    'dam' : 10, # 1 decametro = 10m 
    'hm' : 100, # 1 hectometro = 100m
    'km' : 1000 # 1 km = 1000m
}


# converte para a medida padrão = metros
def ConversaoMetros(value_initial, source_unit):
    if source_unit in FatoresMetrosMetrico: # verifica se a medida inicial está no dicionário (fatores_metros)
        return value_initial * FatoresMetrosMetrico[source_unit]
    else:
        raise ValueError(f'Unidade de medida desconhecida: {source_unit}')

def metros_destination(value_metros, destination_unit):
    if destination_unit in FatoresMetrosMetrico:
        return value_metros / FatoresMetrosMetrico[destination_unit]
    else:
        raise ValueError(f'Unidade de medida desconhecida: {destination_unit}')



def main():
    print('Conversor de unidades métricas - Imperial')

    source_unit = input('Digite a unidade de origem:\n[mm] - [cm] - [dm] - [m] - [dam] - [hec] - [km]\n').lower()
    destination_unit = input('Digite a unidade de distino:\n[mm] - [cm] - [dm] - [m] - [dam] - [hec] - [km]\n').lower()
    value_initial = float(input('Insira o valor que será convertido: '))

    value_metros = ConversaoMetros(value_initial, source_unit)
    result_final = metros_destination(value_metros, destination_unit)

    print(f'Unidade de origem: {value_initial}\nUnidade de destino: {destination_unit}\nResultado final: {result_final}{destination_unit}')
    

main()