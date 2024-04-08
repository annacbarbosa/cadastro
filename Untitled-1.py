cadastros = []

def incluir(cadastros):
    novo_cadastro = {}
    print("\nIncluir novo Cadastro:")

    novo_cadastro['nome'] = input("Nome: ")
    novo_cadastro['telefone'] = input("Telefone: ")
    novo_cadastro['email'] = input("Email: ")
    novo_cadastro['endereco'] = input("Endereço: ")
    novo_cadastro['sexo'] = input("Sexo: ")
    novo_cadastro['pix'] = input("PIX: ")
    novo_cadastro['hora_entrada'] = input("Hora de entrada: ")
    novo_cadastro['hora_saida'] = input("Hora de saída: ")
    novo_cadastro['cpf'] = input("CPF: ")
    novo_cadastro['data_nascimento'] = input("Data de Nascimento: ")
    novo_cadastro['cartao'] = input("Cartão: ")

    cadastros.append(novo_cadastro)
    print("Cadastro adicionado com sucesso!")

def listar(cadastros):
    print("\nLista de Cadastros:")
    for cadastro in cadastros:
        print(cadastro)

def excluir(cadastros):
    print("\nExcluir cadastro:")
    cpf = input("Digite o CPF do cadastro que deseja excluir: ")
    encontrado = False
    for cadastro in cadastros:
        if cadastro['cpf'] == cpf:
            encontrado = True
            cadastros.remove(cadastro)
            print("Cadastro excluído com sucesso!")
            break
    if not encontrado:
        print("Cadastro não encontrado.")

def atualizar(cadastros):
    print("\nAtualizar cadastro:")
    cpf = input("Digite o CPF do cadastro que deseja atualizar: ")
    encontrado = False
    for cadastro in cadastros:
        if cadastro['cpf'] == cpf:
            encontrado = True
            print("\nDigite os novos dados para atualizar o cadastro:")
            cadastro['nome'] = input("Nome: ")
            cadastro['telefone'] = input("Telefone: ")
            cadastro['email'] = input("Email: ")
            cadastro['endereco'] = input("Endereço: ")
            cadastro['sexo'] = input("Sexo: ")
            cadastro['pix'] = input("PIX: ")
            cadastro['hora_entrada'] = input("Hora de entrada: ")
            cadastro['hora_saida'] = input("Hora de saída: ")
            cadastro['cpf'] = input("CPF: ")
            cadastro['data_nascimento'] = input("Data de Nascimento: ")
            cadastro['cartao'] = input("Cartão: ")
            print("Cadastro atualizado com sucesso!")
            break
    if not encontrado:
        print("Cadastro não encontrado.")

while True:
    print("\nMenu:\n")
    print("1. Incluir")
    print("2. Listar")
    print("3. Excluir")
    print("4. Atualizar")
    print("5. Sair\n")

    opcao = input("Por favor, selecione uma opção digitando o número correspondente: ")

    if opcao == '1':
        incluir(cadastros)
    elif opcao == '2':
        listar(cadastros)
    elif opcao == '3':
        excluir(cadastros)
    elif opcao == '4':
        atualizar(cadastros)
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
