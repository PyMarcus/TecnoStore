from models.Supplier import Supplier
from models.Accountancy import Accountancy
from MarketStoreController import MarketStoreController


class MarketController:
    """
    Controladora do mercado
    """

    __accountancy: Accountancy = Accountancy()
    __supplier: Supplier = Supplier()
    __store: MarketStoreController = MarketStoreController()

    @classmethod
    def buy(cls, product_name: str) -> None:
        """
        Compra produtos do fornecedor
        e os armazena no estoque
        :return: None
        """
        product: dict = cls.__supplier.sell(product_name)
        price: float = product["price"]
        cls.__accountancy.manage_cash(price, False)
        cls.__accountancy.statement()
        cls.__store.add(product)

    @classmethod
    def sell(cls, client_name: str,
             product_name: str or dict,
             ) -> dict:
        """
        Vende produtos ao cliente
        Remove do estoque
        e aumenta saldo da vendas
        na classe responsável pelas finanças
        Por fim, retorna um cupom
        :return: cupom (dict)
        """
        product: list = []
        for name in product_name:
            cost: float = cls.__store.select(name)['price']
            product.append(cls.__store.remove(name))
            cls.__accountancy.manage_cash(cost, True)
        return cls.__accountancy.cupom(client_name, product)

    @classmethod
    def show_items(cls) -> None:
        """
        Exibe produtos do estoque
        para o usuário
        :return:
        """
        cls.__store.list()


if __name__ == '__main__':
    mc_debug = MarketController()
    mc_debug.show_items()
    mc_debug.sell("Marcus", [
            "Notebook MarcaXX",
            "Notebook MarcaYY"
    ])
    print("Pós compra")
    mc_debug.show_items()
