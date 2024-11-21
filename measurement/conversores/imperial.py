FatoresMetrosImperial = {
    'polegada' : 0.0254, # 1 polegada = 0.0254m
    'pés' : 0.3048,
    'jarda' : 0.9144,
    'milha' : 1609.34,
    'metro' : 1
}

def ImperialConversaoMetro(value_initial, source_unit):
    if source_unit in FatoresMetrosImperial:
        return value_initial * FatoresMetrosImperial[source_unit]
    else:
        raise ValueError('Unidade de medida desconhecida.')

def ImperialMetroDestino(valor_metros, destination_unit):
    if destination_unit in FatoresMetrosImperial:
        return valor_metros / FatoresMetrosImperial[destination_unit]
    else:
        raise ValueError('Unidade de medida desconhecida.')


def main_imperial():
    while True:
        print('\nConvertedor de medidas Imperiais')
        print('Digite [sair] a qualquer momento para encerrar.')

        source_unit = input('Digite a unidade de origem [Polegada, Pés, Jarda, Milha, Metro]: ').lower()
        if source_unit == 'sair':
            print('Programa encerrado.')
            break

        destination_unit = input('Digite a unidade de destino [Polegada, Pés, Jarda, Milha, Metro]: ').lower()
        if destination_unit == 'sair':
            print('Programa encerrado.')
            break

        try:
            value_initial = float(input('Informe o valor que será convertido: '))
            value_metro = ImperialConversaoMetro(value_initial, source_unit)
            value_final = ImperialMetroDestino(value_metro, destination_unit)
        
            print(f'Unidade de origem | {value_initial}{source_unit}')
            print(f'Unidade de destino | {value_final}{destination_unit}')

        except ValueError as e:
            print(f'Erro: {e}')
        except Exception:
            print('Entrada inválida. Tente novamente.')

if __name__ == '__main__':
    main_imperial()