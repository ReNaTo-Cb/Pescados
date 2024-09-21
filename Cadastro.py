import pandas as pd

# Verifica se o arquivo existe para carregar os dados existentes
try:
    clientes_df = pd.read_csv('clientes.csv')
except FileNotFoundError:
    # Cria um DataFrame vazio caso o arquivo não exista
    clientes_df = pd.DataFrame(columns=['ID', 'Nome', 'Email', 'Telefone'])

# Função para cadastrar um cliente
def cadastrar_cliente():
    global clientes_df
    id_cliente = input("Digite o ID do cliente: ")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    # Adiciona o novo cliente ao DataFrame
    novo_cliente = pd.DataFrame([[id_cliente, nome, email, telefone]], columns=clientes_df.columns)
    clientes_df = pd.concat([clientes_df, novo_cliente], ignore_index=True)

    # Salva o DataFrame atualizado em um arquivo CSV
    clientes_df.to_csv('clientes.csv', index=False)
    print("Cliente cadastrado com sucesso!")

# Função para visualizar todos os clientes cadastrados
def visualizar_clientes():
    print("\nClientes Cadastrados:")
    print(clientes_df)

# Menu de opções
def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Cliente")
        print("2. Visualizar Clientes")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            visualizar_clientes()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
