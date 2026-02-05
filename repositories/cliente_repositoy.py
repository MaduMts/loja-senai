from schemas.cliente_schema import Cliente

clientes = []

class ClienteRepository:

    def Cadastrar_cliente(id_pessoa, data_cadastro):
      cliente = Cliente(id_pessoa, data_cadastro)
      clientes.append(clientes)
      return cliente 
    