def pesquisarProduto(nomeProduto: str) -> None:
    produtosDisponiveis = [{'Nome': 'arroz', 'quantidade': 10}, {'Nome': 'feijao', 'quantidade': 2}, {'Nome': 'batata', 'quantidade': 90}]
    nomeProdutoAgora = ""

    for i in range(len(produtosDisponiveis)):
        quantidadeDisponivel = 0

        for chave, valor in produtosDisponiveis[i].items(): 
            for valores in range(2):
                if valores == 0:
                    nomeProdutoAgora = nomeProduto
                elif valores == 1:
                    if nomeProdutoAgora == nomeProduto:
                        quantidadeDisponivel = valor 

    return print(quantidadeDisponivel)

            

pesquisarProduto("arroz")