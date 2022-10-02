import datetime


class AccountancyController:
    """
    Classe responsável
    pela contabilidade e finanças
    da loja, é especialista nas informações
    de clientes e nas transações bancárias
    """
    __cash: float = 300000.00  # saldo privado do mercado (CAPITAL INICIAL)
    __clients: list = list()  # clientes q compraram

    @classmethod
    def buyed_for(cls, client_information) -> None:
        """
        Salva informações do cliente
        que realizou uma compra
        :return:
        """
        cls.__clients.append(client_information)

    @classmethod
    def manage_cash(cls, value: float, operation: bool) -> None:
        """
        Gerencia o saldo do mercado
        :param value: float
        :param operation: True (venda), false(compra)
        :return: None
        """
        if 0 < value < cls.__cash:
            if operation:
                cls.__cash += value
            else:
                cls.__cash -= value
        else:
            print("Valor inválido ou saldo insuficiente para operação")

    @classmethod
    def statement(cls) -> None:
        """
        Retorna o extrato
        com o saldo e data atuais
        :return:
        """
        print(f"Saldo disponível em {datetime.datetime.now()}: R${cls.__cash}\n")

    @classmethod
    def cupom(cls, client_name: str, products: list[dict]) -> dict:
        """
        Retorna um cupom para o cliente,
        após a compra, com o total e itens comprados
        :param client_name:
        :param products: itens comprados
        :return:
        """
        print(f"___" * 13)
        print('\t'*3 ,end='')
        print("CUPOM")
        print(f"Agradeçemos a compra, {client_name}.")
        print("Itens:")
        money_spent: float = 0
        for product in products:
            print(f"Produto: {product['name']} por R${product['price']}")
            money_spent += product['price']
        print(f"{' ' * 18} Total: R${money_spent}")
        print(f"\n{' ' * 9} TecnoStore®")
        print(f"___" * 13)
        return {
            "client_name": client_name,
            "products": products,
            "total": money_spent
        }


if __name__ == '__main__':
    acc_debug = AccountancyController()
    acc_debug.statement()
    acc_debug.manage_cash(15000, True)
    acc_debug.statement()

    acc_debug.cupom("Debug", [
                              {
                                "name": "Notebook MarcaW",
                                "price": 1000.00
                              },
                              {
                                  "name": "Desktop MarcaW",
                                  "price": 3425.44
                              }
        ,
                              {
                                  "name": "Desktop MarcaH",
                                  "price": 13425.44
                              },
                              ], 17850.88)
