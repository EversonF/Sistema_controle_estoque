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