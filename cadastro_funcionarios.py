funcionarios = []

while True:
    print("\n=== CADASTRO DE FUNCIONÁRIOS ===")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cargo = input("Cargo: ")

        funcionarios.append({
            "nome": nome,
            "cargo": cargo
        })

        print("Funcionário cadastrado!")

    elif opcao == "2":
        print("\n=== FUNCIONÁRIOS CADASTRADOS ===")

        for funcionario in funcionarios:
            print(
                f"Nome: {funcionario['nome']} | Cargo: {funcionario['cargo']}"
            )

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
