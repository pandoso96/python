menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

= > '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor que deseja depositar: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print('O valor informado é inválido.')

    elif opcao == 's':
        valor = (float(input('Digite o valor que deseja sacar: ')))

        ultrapassou_saldo = valor > saldo

        ultrapassou_limite = valor > limite 

        ultrapassou_saques = numero_saques >= LIMITE_SAQUES
            
        if ultrapassou_saldo: 
            print('Operação falhou! Saldo insuficiente')
        
        elif ultrapassou_limite:
            print('Operação falhou! Valor de saque excede o limite máximo')
        
        elif ultrapassou_saques:
            print('Operação falhou! Limite de saques excedidos')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')


    elif opcao == 'e':
        print('\n=========== EXTRATO ==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('================================')

    elif opcao == 'q':
        break

    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')