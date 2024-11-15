fatores_metros = {
    'mm' : 0.001, # 1 milimetro = 0.001 m
    'cm' : 0.01, # 1 centimetro = 0.01 m
    'm' : 1, # metro é igual a 1
    'km' : 1000 # 1 km = 1000 m
}


# converte para a medida padrão = metros
def converter_metros(value_initial, source_unit):
    if source_unit in fatores_metros: # verifica se a medida inicial está no dicionário (fatores_metros)
        return value_initial * fatores_metros[source_unit]
    else:
        raise ValueError(f'Unidade de medida desconhecida: {source_unit}')


# def metros_destination():
    #pass

def main():
    print('Conversor de unidades métricas - Imperial')

    source_unit = input('Digite a unidade de origem:\n[mm] - [cm] - [m] - [km]\n').lower()
    # destination_unit = input('Digite a unidade de distino:\n[mm] - [cm] - [m] - [km]\n').lower()
    value_initial = float(input('Insira o valor que será convertido: '))
    
    print(converter_metros(value_initial, source_unit))

main()