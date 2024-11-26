from sistema_imperial.imperial import FatoresMetrosImperial
from sistema_metrico.metrico import FatoresMetrosMetrico
from conversao_cruzada import ConverterEntreSistemas


def InterfaceUsuario():
    print('Bem vindo a interface do conversor de unidades!')

    while True:
        sistema_origem = input(f'Informe o seu sistema de origem | Imperial / Métrico: ').lower()
        if sistema_origem not in ['métrico', 'imperial']:
            print('Sistema de origem não reconhecido.')
            continue
        
        sistema_destino = input('Agora, informe o sistema de destino | Imperial / Métrico: ').lower()
        if sistema_destino not in ['métrico', 'imperial']:
            print('Sistema de destino desconhecido.')
            continue

        unidade_origem = input(f'Digite a unidade de origem: \n{FatoresMetrosImperial} | \n{FatoresMetrosMetrico}: ')
        unidade_destino = input(f'Digite a unidade de destino: \n{FatoresMetrosImperial} | \n{FatoresMetrosMetrico}: ')

        

        try:
            valor = float(input(f'Digite o valor a ser convertido de {unidade_origem} | {unidade_destino}: '))
            print(f'Entrada: {valor} {unidade_origem} | {unidade_destino}')

            resultado = ConverterEntreSistemas(valor, unidade_origem, unidade_destino, sistema_origem, sistema_destino)
            print(f'\nResultado = {valor}{unidade_origem} é igual a {resultado}{unidade_destino}.\n')
        
    
        except ValueError:
            print('Valor inválido.')
            continue

        except ValueError as e:
            print(f'Erro: {e}')
            continue


        continuar = input('Deseja fazer mais algum calculo? \n| Sim | Não: \n').lower()
        if continuar != 'sim':
            print('Programa encerrado!')
            break

if __name__ == '__main__':
    InterfaceUsuario()
