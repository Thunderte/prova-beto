def juncaoProdutos(produto1: str, quantidade1: int, produto2: str, quantidade2: int, produto3: str, quantidade3: int) -> None:

    estoqueProduto1 = dict({"Nome": produto1, "quantidade": quantidade1})
    estoqueProduto2 = dict({"Nome": produto2, "quantidade": quantidade2})
    estoqueProduto3 = dict({"Nome": produto3, "quantidade": quantidade3})

    estoque = [estoqueProduto1, estoqueProduto2, estoqueProduto3]

    return estoque

def main():
    nomeProduto1 = str(input("Digite a nome do 1 produto: \n"))
    valorProduto1 = int(input("Agora digite o valor do 1 produto: \n"))

    nomeProduto2 = str(input("Digite a nome do 2 produto: \n"))
    valorProduto2 = int(input("Agora digite o valor do 2 produto: \n"))

    nomeProduto3 = str(input("Digite a nome do 3 produto: \n"))
    valorProduto3 = int(input("Agora digite o valor do 3 produto: \n"))

    estoqueRetornado = juncaoProdutos(nomeProduto1, valorProduto1, nomeProduto2, valorProduto2, nomeProduto3, valorProduto3)

    return print(f"O novo estoque é {estoqueRetornado}")

main()
