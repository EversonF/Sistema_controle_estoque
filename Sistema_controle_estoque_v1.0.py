lista_produtos = ['máscara faciais' , 'esmaltes' , 'perfumes' , 'batons']

def mostrar_produtos():
    print("\nLista de produtos: ")
    for i, produto in enumerate(lista_produtos):
        print(f"{i + 1}: {produto}")

def adicionar_produto(produto):
    lista_produtos.append(produto)
    print(f"{produto} adicionado à lista.")

def alterar_produto(indice, novo_produto):
    if 0 <= indice < len(lista_produtos):
        lista_produtos[indice] = novo_produto
        print(f"Produto na posição {indice + 1} alterado para {novo_produto}.")
    else:
        print("Índice inválido.")

def excluir_produto(indice):
    if 0 <= indice < len(lista_produtos):
        excluido = lista_produtos.pop(indice)
        print(f"{excluido} excluído da lista.")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\nEscolha uma opção: ")
        print("1. Mostrar produtos ")
        print("2. Adicionar produto ")
        print("3. Alterar produto ")
        print("4. Excluir produto ")
        print("5. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            mostrar_produtos()
        elif opcao == '2':
            novo_produto = input("Digite o nome do produto a ser adicionado: ")
            adicionar_produto(novo_produto)
        elif opcao == '3':
            mostrar_produtos()
            indice = int(input("Digite o número do porduto que deseja alterar: ")) - 1
            novo_produto = input("Digite o novo nome do produto: ")
            alterar_produto(indice, novo_produto)
        elif opcao == '4':
            mostrar_produtos()
            indice = int(input("Digite o número do produto que deseja excluir: ")) - 1
            excluir_produto(indice)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
      main()