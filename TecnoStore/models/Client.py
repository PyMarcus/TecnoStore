from controllers.ClientController import ClientController


class Client:
    """
    Classe que cria o cliente
    Ele é capaz de adicionar ou
    remover itens do carrinho
    além de comprar os produtos
    """
    def __init__(self,
                 name: str,
                 cpf: str,
                 birth: str,
                 cash: float,
                 email: str
                 ) -> None:
        self.__name = name   # atributos privados garantem o encapsulamento
        self.__cpf = cpf
        self.__birth = birth
        self.__cash = cash
        self.__email = email
        self.__controller = ClientController(name, cpf, birth, cash, email)

    def buy(self):
        """
        Compra itens, de fato
        :return:
        """
        self.__controller.buy()

    def add_to_card(self, product) -> None:
        """
        Adiciona produto ao carrinho de compra
        :param product:
        :return:
        """
        self.__controller.add_to_card(product)

    def remove_from_card(self, name) -> None:
        """
        Remove item do carrinho de compra
        :param name
        :return:
        """
        self.__controller.remove_from_card(name_of_product=name)

    def show_card(self) -> None:
        """
        Exibe itens do carrinho do cliente
        :return:
        """
        self.__controller.show_card()

    def __repr__(self):
        return f"Client:{self.__name}"

    def __str__(self):
        return f"Client:{self.__name}"
