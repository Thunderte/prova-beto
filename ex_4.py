def analiseDeVendas():
    todasVendas = []
    totalArrecadado = []

    quantidadeItemMaisVendido = 0
    itemMaisVendido = ""

    nomeProduto = ""
    quantidade = int(0)
    totalArrecadoProduto = float(0)

    for i in range(10):
       nomeProduto = str(input(f'Digite o nome do produto {i + 1}: \n'))
       quantidadeVendida = int(input(f'Digite a quantidade vendida do produto {nomeProduto}: \n'))
       preco = float(input(f'Digite o preço unitário do produto {nomeProduto}: \n'))

       if quantidadeVendida > quantidadeItemMaisVendido:
           quantidadeItemMaisVendido = quantidadeVendida
           itemMaisVendido = nomeProduto

       venda = {"produto": nomeProduto, "quantidade": quantidadeVendida, "preco_unitario": preco}

       todasVendas.append(venda)
    return f'Essas são todas as vendas {todasVendas} \n \n e o item mais vendido é {itemMaisVendido} com {quantidadeItemMaisVendido} vendidos'


def main():

    print(analiseDeVendas())


main()

