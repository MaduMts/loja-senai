from schemas.vendedor_schema import Vendedor

vendedores = []

class VendedorRepository:

    def cadastrar_vendedor(pessoa_id, data_cadastro):
        vendedor = Vendedor(pessoa_id, data_cadastro)
        vendedores.append(vendedor)
        return vendedor
    