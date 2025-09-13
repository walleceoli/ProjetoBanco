import psycopg2
import random

# Conexão ao banco
conexao = psycopg2.connect(
    host="localhost",
    database="banco_clientes",
    user="postgres",
    password="Eusougamer1?"
)
cursor = conexao.cursor()

# Listas de primeiros nomes e sobrenomes
primeiros_nomes = [
    "Ana", "Bruno", "Carla", "Diego", "Eduarda", "Felipe", "Gabriela", "Henrique",
    "Isabela", "João", "Karina", "Lucas", "Mariana", "Nathan", "Olívia", "Paulo",
    "Quésia", "Rafael", "Sofia", "Thiago", "Ursula", "Victor", "William", "Yasmin", "Zé"
]

sobrenomes = [
    "Almeida", "Barbosa", "Cardoso", "Dias", "Esteves", "Ferreira", "Gomes", "Henriques",
    "Inácio", "Jardim", "Klein", "Lopes", "Moura", "Nascimento", "Oliveira", "Pereira",
    "Queiroz", "Ribeiro", "Silva", "Teixeira", "Uchoa", "Vasconcelos", "Werneck", "Xavier", "Zanetti"
]

# Gerar 100 clientes com nome completo e saldo aleatório
clientes = []
for i in range(100):
    nome = f"{random.choice(primeiros_nomes)} {random.choice(sobrenomes)}"
    saldo = round(random.uniform(0, 10000), 2)  # saldo entre 0 e 10.000
    clientes.append((nome, saldo))

# Inserir no banco
cursor.executemany(
    "INSERT INTO clientes (nome, saldo) VALUES (%s, %s)",
    clientes
)
conexao.commit()

print("✅ 100 clientes reais adicionados com sucesso!")

# Fechar conexão
cursor.close()
conexao.close()
