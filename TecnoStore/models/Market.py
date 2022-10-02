from controllers.MarketController import MarketController
from controllers.MarketStoreController import MarketStoreController

class Market:
    """
    Compra produtos do fornecedor
    Vende-os ao cliente
    Exibe os produtos do estoque
    do mercado
    """
    def __init__(self):
        self.controller: MarketController = MarketController()

    def buy(self, name: str) -> None:
        """
        Compra produtos do fornecedor
        :param name => nome do produto
        :return: None
        """
        return self.controller.buy(product_name=name)

    def sell(self, client: str,
             product_name: str or list,
             ) -> dict:
        """
        Vende produtos ao cliente
        :return:
        """
        return self.controller.sell(client, product_name)

    def show_items(self) -> None:
        """
        Exibe produtos do estoque
        para o usuário
        :return:
        """
        self.controller.show_items()

    def content(self) -> list[dict]:
        return MarketStoreController.content()
