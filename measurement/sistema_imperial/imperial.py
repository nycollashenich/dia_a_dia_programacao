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



# def main_imperial():
#     while True:
#         print('\nConvertedor de medidas Imperiais')
#         print('Digite [sair] a qualquer momento para encerrar.')

#         source_unit = input('Digite a unidade de origem [Polegada, Pés, Jarda, Milha, Metro]: ').lower()
#         if source_unit == 'sair':
#             print('Programa encerrado.')
#             break

#         destination_unit = input('Digite a unidade de destino [Polegada, Pés, Jarda, Milha, Metro]: ').lower()
#         if destination_unit == 'sair':
#             print('Programa encerrado.')
#             break

#         try:
#             value_initial = float(input('Informe o valor que será convertido: '))
#             value_metro = ImperialConversaoMetro(value_initial, source_unit)
#             value_final = ImperialMetroDestino(value_metro, destination_unit)
        
#             print(f'Unidade de origem | {value_initial}{source_unit}')
#             print(f'Unidade de destino | {value_final}{destination_unit}')

#         except ValueError as e:
#             print(f'Erro: {e}')
#         except Exception:
#             print('Entrada inválida. Tente novamente.')

# if __name__ == '__main__':
#     main_imperial()