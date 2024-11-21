FatoresMetrosMetrico = {
    'mm' : 0.001, # 1 milimetro = 0.001m
    'cm' : 0.01, # 1 centimetro = 0.01m
    'dm' : 0.1, # 1 decímetro = 0.01m
    'm' : 1, # metro é igual a 1m
    'dam' : 10, # 1 decametro = 10m 
    'hec' : 100, # 1 hectometro = 100m
    'km' : 1000 # 1 km = 1000m
}


# converte para a medida padrão = metros
def ConversaoMetros(value_initial, source_unit):
    if source_unit in FatoresMetrosMetrico: # verifica se a medida inicial está no dicionário (fatores_metros)
        return value_initial * FatoresMetrosMetrico[source_unit]
    else:
        raise ValueError(f'Unidade de medida desconhecida: {source_unit}')

def MetrosDestino(value_metros, destination_unit):
    if destination_unit in FatoresMetrosMetrico:
        return value_metros / FatoresMetrosMetrico[destination_unit]
    else:
        raise ValueError(f'Unidade de medida desconhecida: {destination_unit}')


def main_metrico():

    while True:
        print('\nConvertedor de Unidades Métricas.')
        print('Digite [sair] a qualquer momento para encerrar.')

        source_unit = input('Digite a unidade de origem [mm, cm, dm, m, dam, hec, km]: ').lower()
        if source_unit == 'sair':
            print('Programa encerrado')
            break

        destination_unit = input('Digite a unidade de destino [mm, cm, dm, m, dam, hec, km]: ').lower()
        if destination_unit == 'sair':
            print('Programa encerrado')

        try:
            value_initial = float(input('Informe o valor que será convertido: '))
            value_metro = ConversaoMetros(value_initial, source_unit)
            value_final = MetrosDestino(value_metro, destination_unit)

            print(f'\nUnidade de origem | {value_initial}{source_unit}')
            print(f'Unidade de destino | {value_final}{destination_unit}')

        except ValueError as e:
            print(f'Erro {e}')
        except Exception:
            print('Entrada inválida. Tente novamente.')

if __name__ == '__main__':
    main_metrico()