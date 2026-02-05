from schemas.produto_schema import Produto

produtos = []

class ProdutoRepository:

    def cadastrar_produto(nome_indetificacao, preco, quantidade_estoque):
        produto = Produto(nome_indetificacao, preco, quantidade_estoque)
        produtos.append(produto)
        return produto
    