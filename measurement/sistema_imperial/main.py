FatoresMetrosImperial = {
    'polegada' : 0.0254, # 1 polegada = 0.0254m
    'pés' : 0.3048,
    'jarda' : 0.9144,
    'milha' : 1609.34,
    'metro' : 1
}

def ConversaoMetros(value_initial, source_unit):
    if source_unit in FatoresMetrosImperial:
        return value_initial * FatoresMetrosImperial[source_unit]
    else:
        raise ValueError('Unidade de medida desconhecida.')

def MetrosDestination(valor_metros, destination_unit):
    if destination_unit in FatoresMetrosImperial:
        return valor_metros / FatoresMetrosImperial[destination_unit]
    else:
        raise ValueError('Unidade de medida desconhecida.')


def main():
    
    print('Conversão Medidas Imperiais')

    source_unit = input('Informe a medida de ORIGEM: \n[Polegada] - [Pés] - [Jarda] - [Milha] - [Metro]\n').lower()
    destination_unit = input('Informe a medida de DESTINO: \n[Polegada] - [Pés] - [Jarda] - [Milha] - [Metro]\n').lower()
    value_initial = float(input('Insira o valor que será convertido: '))

    valor_metros = ConversaoMetros(value_initial, source_unit)
    result_final = MetrosDestination(valor_metros, destination_unit)

    print(f'Unidade de origem: {value_initial}\nUnidade de destino: {destination_unit}\nResultado final: {result_final} {destination_unit}')
    

main()

