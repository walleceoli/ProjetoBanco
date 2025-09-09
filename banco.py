# Lista de Clientes.
listaClientes = [{'Nome': 'Jõao', 'id': 123, 'Saldo': 1000},
                 {'Nome': 'Maria', 'id': 456, 'Saldo': 1500},
                 {'Nome': 'Carlos', 'id': 789, 'Saldo': 0}]

# loop onde o cliente da entrada no sistema e caso o id do cliente não exista
# pedimos para rescrever o id ou adcionar um cliente caso desejado.
while True:
    try:
        entradaClientes = int(input('Digite seu id para entrar.'))
    except ValueError:
        print('Digite apenas numeros')
        continue
    clienteEncontrado = None
    for cliente in listaClientes:
        if cliente['id'] == entradaClientes:
            clienteEncontrado = cliente
            break

    if clienteEncontrado:
        print(f"Seja bem vindo {clienteEncontrado['Nome']}!")
        # Adcionando opções de saque, saldo e extrato
        while True:
            opcaoCliente = int(input('1 para ver extratato\n2 para sacar\n3 para depositar\n4 para sair\nDigite:'))
            if opcaoCliente == 1:
                print(f'Seu saldo é de R${clienteEncontrado['Saldo']}')

            elif opcaoCliente == 2:
                saque = int(input('Quanto deseja sacar? R$'))
                if saque > clienteEncontrado['Saldo']:
                    print('Saldo insuficiente!')
                else:
                    clienteEncontrado['Saldo'] -= saque
                    print(f'Valor do saque R${saque}')

            elif opcaoCliente == 3:
                valorDeposito = int(input(f'Quanto deseja depositar? R$'))
                clienteEncontrado['Saldo'] += valorDeposito
                print(f'Você depositou R${valorDeposito}')

            elif opcaoCliente == 4:
                break
            else:
                print('Opção invalida!')
                break
    else:
        print('Cliente não encontrado!')
        adcionarReiniciar = int(input('Digite 1 para tentar novamente e 2 para adcionar cliente.'))
        if adcionarReiniciar == 1:
            continue
        elif adcionarReiniciar == 2:
            nomeNovo = input('Qual o seu nome?')
            # loop para impedir que o mesmo id seja adcionado.
            while True:
                idNovo = int(input('Qual o id desejado?'))
                idExistente = False
                for clienteEncontrado in listaClientes:
                    if clienteEncontrado['id'] == idNovo:
                        idExistente = True
                        break
                if idExistente:
                    print('ID já existente!')
                    continue
                else:
                    print('Id valido!')
                    break
            # Cliente sendo adcionado a lista
            listaClientes.append({'Nome': nomeNovo, 'id': idNovo, 'Saldo': 0})
            print('Cliente adcionado com sucesso!\n')
        else:
            print('Opção invalida\n, Saindo...')
            break
