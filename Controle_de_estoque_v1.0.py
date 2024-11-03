lista_produtos = ['máscara faciais' , 'esmaltes' , 'perfumes' , 'batons']

def mostrar_produtos():
    print("\nLista de produtos: ")
    for i, produto in enumerate(lista_produtos):
        print(f"{i + 1}: {produto}")