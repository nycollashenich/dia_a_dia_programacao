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

        if sistema_origem == 'imperial':
            unidades_origem = FatoresMetrosImperial
        else:
            unidades_origem = FatoresMetrosMetrico
        
        sistema_destino = input('Agora, informe o sistema de destino | Imperial / Métrico: ').lower()
        if sistema_destino not in ['métrico', 'imperial']:
            print('Sistema de destino desconhecido.')
            continue

        if sistema_destino == 'imperial':
            unidades_destino = FatoresMetrosImperial
        else:
            unidades_destino = FatoresMetrosMetrico

        
        unidade_origem = input(f'Digite a unidade de origem: \n{unidades_origem}: ')
        if unidade_origem not in unidades_origem:
            print(f'Unidade de origem {unidades_origem} não é válida no sistema {sistema_origem}.')
            continue
        
        unidade_destino = input(f'Digite a unidade de destino: \n{unidades_destino} ')
        if unidade_destino not in unidades_destino:
            print(f'Unidade de destino {unidades_origem} não é válida no sistema {sistema_destino}.')
            continue

        
        try:
            valor = float(input(f'Digite o valor a ser convertido de {unidade_origem} | {unidade_destino}: '))
            print(f'Entrada: {valor} | {unidade_origem} | {unidade_destino}')

            
            resultado = ConverterEntreSistemas(
                valor=valor, 
                unidade_origem=unidade_origem,
                unidade_destino=unidade_destino,
                sistema_origem=sistema_origem,
                sistema_destino=sistema_destino
            )
            
            print(f"Debug: {valor}, {unidade_origem}, {unidade_destino}, {sistema_origem}, {sistema_destino}")
            print(f'\nResultado = {valor} {unidade_origem} é igual a | {resultado} | {unidade_destino}.\n')
    
        except ValueError:
            print('Valor inválido.')
            continue

        except Exception as e:
            print(f'Erro: {e}')
            continue


        continuar = input('Deseja fazer mais algum calculo? \n| Sim | Não: \n').lower()
        if continuar != 'sim':
            print('Programa encerrado!')
            break


if __name__ == '__main__':
    InterfaceUsuario()
