# importando a biblioteca psycopg2 para faser a integração dos dados com o postegreSQL
import psycopg2
conexao = psycopg2.connect(
    host="localhost",
    database="banco_clientes",
    user="postgres",
    password="Eusougamer1?"
)
cursor = conexao.cursor()

#Função para buscar o cliente no banco de dados
def buscar_cliente(id_cliente):
    cursor.execute("SELECT * FROM clientes WHERE id = %s",(id_cliente,))
    cliente = cursor.fetchone()
    if cliente:
        return {"ID": cliente[0], "Nome": cliente[1],"Saldo": float(cliente[2])}
    else:
        return None

#função para adcionar o cliente ao banco de dados
def adicionar_cliente(nome, id_cliente):
    cursor.execute("INSERT INTO clientes (id, nome, saldo) VALUES (%s, %s, %s)", (id_cliente, nome, 0))
    conexao.commit()
    print('Cliente adcionado com sucesso.')

#função para atualizar o saldo no banco de dados
def atualizar_saldo(id_cliente, novo_saldo):
    cursor.execute(
        "UPDATE clientes SET saldo = %s WHERE id = %s",
        (novo_saldo, id_cliente)
    )
    conexao.commit()
    print("✅ Saldo atualizado!")


#Função para registrar as operações realizadas
def registrar_operacao(id_cliente, operacao, valor):
    cursor.execute(
        "INSERT INTO extrato (cliente_id, operacao, valor) VALUES (%s, %s, %s)",
        (id_cliente, operacao, valor)
    )
    conexao.commit()

def buscar_extrato(id_cliente):
    cursor.execute("SELECT operacao, valor, data FROM extrato WHERE cliente_id = %s ORDER BY data", (id_cliente,))
    return cursor.fetchall()

# loop onde o cliente da entrada no sistema e caso o id do cliente não exista
# pedimos para rescrever o id ou adcionar um cliente caso desejado.
while True:
    id_digitado = int(input("Digite seu id para entrar."))
    clienteEncontrado = buscar_cliente(id_digitado)

    if clienteEncontrado:
        print(f"Seja bem vindo {clienteEncontrado['Nome']}!")
        # Adcionando opções de saque, saldo e extrato
        while True:
            opcaoCliente = int(input("1 para ver extratato\n2 para sacar\n3 para depositar\n4 para sair\nDigite:"))
            if opcaoCliente == 1:
                print(f"Saldo\nR${clienteEncontrado['Saldo']}")
                extrato = buscar_extrato(clienteEncontrado['ID'])
                if extrato:
                    print('Histórico')
                    for op in extrato:
                        print(f"{op[2]} - {op[0]} R${float(op[1])}")
                else:
                    print('Sem movimentações')

            elif opcaoCliente == 2:
                saque = float(input("Quanto deseja sacar? R$"))
                if saque <= 0:
                    print("Valor invalido para saque")
                elif saque > clienteEncontrado['Saldo']:
                    print("Saldo insuficiente!")
                else:
                    clienteEncontrado['Saldo'] -= saque
                    atualizar_saldo(clienteEncontrado['ID'], clienteEncontrado['Saldo'])
                    registrar_operacao(clienteEncontrado['ID'], "Saque", saque)
                    print(f"Valor do saque R${saque}")

            elif opcaoCliente == 3:
                valorDeposito = float(input(f"Quanto deseja depositar? R$"))
                if valorDeposito <= 0:
                    print("Valor invalido para deposito")
                else:
                    clienteEncontrado['Saldo'] += valorDeposito
                    atualizar_saldo(clienteEncontrado['ID'], clienteEncontrado['Saldo'])
                    registrar_operacao(clienteEncontrado['ID'], "Deposito", valorDeposito)
                    print(f"Você depositou R${valorDeposito}")

            elif opcaoCliente == 4:
                validarSaida = int(input('1 = Confirmar saida.\n2 = Continuar programa.\n'))
                if validarSaida == 1:
                    print('Obrigado por utilizar o programa.')
                    break
                elif validarSaida == 2:
                    print('...')
                else:
                    print('Digite um numero valido')
            else:
                print("Opção invalida!")
                break
    else:
        print("Cliente não encontrado!")
        adcionarReiniciar = int(input("Digite 1 para tentar novamente e 2 para adcionar cliente."))
        if adcionarReiniciar == 1:
            continue
        elif adcionarReiniciar == 2:
            nomeNovo = input("Qual o seu nome?")
            # loop para impedir que o mesmo id seja adcionado.
            while True:
                idNovo = int(input("Qual o id desejado?"))
                if buscar_cliente(idNovo):
                    print('id já existente')
                else:
                    adicionar_cliente(nomeNovo, idNovo)
                    break
        else:
            print("Opção invalida\n, Saindo...")
            break


# Fechar conexão
cursor.close()
conexao.close()
