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

    def buy(self):
        """
        Compra itens, de fato
        :return:
        """
        pass

    def add_to_card(self, product) -> None:
        """
        Adiciona produto ao carrinho de compra
        :param product:
        :return:
        """
        pass

    def remove_from_card(self) -> None:
        """
        Remove item do carrinho de compra
        :return:
        """
        pass

    def show_card(self) -> None:
        """
        Exibe itens do carrinho do cliente
        :return:
        """
