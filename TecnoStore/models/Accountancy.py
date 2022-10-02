from controllers.AccountancyController import AccountancyController


class Accountancy:
    """
    Classe responsável
    por modelar o setor
    de contabilidade, de forma simples
    """

    __acc = AccountancyController()

    @classmethod
    def buyed_for(cls, client_information) -> None:
        """
        Salva informações do cliente
        que realizou uma compra
        :return:
        """
        cls.__acc.buyed_for(client_information)

    @classmethod
    def manage_cash(cls, value: float, operation: bool) -> None:
        """
        Gerencia o saldo do mercado
        :param value: float
        :param operation: True (venda), false(compra)
        :return: None
        """
        cls.__acc.manage_cash(value, operation)

    @classmethod
    def statement(cls) -> None:
        """
        Retorna o extrato
        com o saldo e data atuais
        :return:
        """
        cls.__acc.statement()

    @classmethod
    def cupom(cls, client_name: str, products) -> dict:
        """
        Retorna um cupom para o cliente,
        após a compra, com o total e itens comprados
        :param client_name:
        :param products:
        :return: dict (cupom)
        """
        return cls.__acc.cupom(client_name, products)


if __name__ == '__main__':
    acc_debug = Accountancy()
    acc_debug.statement()
    acc_debug.manage_cash(15000, True)
    acc_debug.statement()
