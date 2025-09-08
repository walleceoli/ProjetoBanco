# Lista de Clientes.
listaClientes = [{'Nome': 'Jõao', 'id': 123},
                 {'Nome': 'Maria', 'id': 456},
                 {'Nome': 'Carlos', 'id': 789}]

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
                for cliente in listaClientes:
                    if cliente['id'] == idNovo:
                        idExistente = True
                        break
                if idExistente:
                    print('ID já existente!')
                    continue
                else:
                    print('Id valido!')
                    break
            #Cliente sendo adcionado a lista
            listaClientes.append({'Nome': nomeNovo, 'id': idNovo})
            print('Cliente adcionado com sucesso!\n')
        else:
            print('Opção invalida\n, Saindo...')
            break

