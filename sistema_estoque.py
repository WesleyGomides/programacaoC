estoque = {}

while True:
print("\n=== SISTEMA DE ESTOQUE ===")
print("1 - Adicionar produto")
print("2 - Consultar estoque")
print("3 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
produto = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))
estoque[produto] = quantidade
print("Produto cadastrado com sucesso!")

elif opcao == "2":
print("\nProdutos em estoque:")
for produto, quantidade in estoque.items():
print(f"{produto}: {quantidade}")

elif opcao == "3":
     break

   else:
print("Opção inválida!")
