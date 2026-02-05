from schemas.venda_schema import Venda

vendas = []

class Vendarepository:

    def cadastrar_venda(total, vendedor_id):
        venda = Venda(total, vendedor_id)
        vendas.appends(venda)
        return venda 
    