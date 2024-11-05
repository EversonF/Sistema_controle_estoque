# Sistema de Controle de Estoque

-----------------------

## Bem-vindos ao nosso primeiro projeto! 🤩

### Colaboradores:
### 💻 Everson Araujo Ferreira
### 💻 Marco Tulio da Silva Rocha
### 💻 Jessica Dasmaceno Barbosa
### 💻 Flávia Kathellen Batista Passos

-------------------------
## Documentação
#### Funções
```CMD=
lista_produtos = ['máscara faciais', 'esmaltes', 'perfumes', 'batons']

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
```
----------------------
## Função Principal (main)
### A função *main()* é onde o programa entra em um loop contínuo, permitindo ao usuário escolher ações. O loop só termina quando o usuário escolhe a opção de "Sair" (opção 5).
### Dentro desse loop, são apresentadas as opções, e o programa aguarda o usuário fazer uma escolha. Dependendo da escolha, o programa chama a função correspondente, ou exibe uma mensagem de erro em caso de entrada inválida.

```CMD=

def main():
    while True:
        print("\nEscolha uma opção: ")
        print("1. Mostrar produtos")
        print("2. Adicionar produto")
        print("3. Alterar produto")
        print("4. Excluir produto")
        print("5. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            mostrar_produtos()
        elif opcao == '2':
            novo_produto = input("Digite o nome do produto a ser adicionado: ")
            adicionar_produto(novo_produto)
        elif opcao == '3':
          while True:
              mostrar_produtos()
              try:
                  indice = int(input("Digite o número do produto que deseja alterar: ")) - 1
                  novo_produto = input("Digite o novo nome do produto: ")
                  alterar_produto(indice, novo_produto)
                  break
              except ValueError:
                  print("Por favor, insira um número válido.\n")
        elif opcao == '4':
            mostrar_produtos()
            try:
                indice = int(input("Digite o número do produto que deseja excluir: ")) - 1
                excluir_produto(indice)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

````

-------------------
## Execução
### O programa começa a execução chamando a função *main()* no final do código:

```CMD=
if __name__ == "__main__":
    main()
```
### Essa linha garante que o programa execute a função principal apenas quando o script for executado diretamente (não quando importado como módulo).



