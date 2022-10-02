class MarketStoreController:
    """
    Estoque do mercado
    Esta classe simula um banco de dados
    para controlar o estoque
    """
    __store = [
        {
            "name": "Notebook MarcaXX",
            "price": 3405.40
        },
        {
            "name": "Notebook MarcaYY",
            "price": 2405.40
        },
    ]

    @classmethod
    def add(cls, product) -> None:
        """
        Compra do fornecedor e
        adiciona produto ao estoque
        :return:
        """
        cls.__store.append(product)

    @classmethod
    def remove(cls, product_name: str) -> bool or dict:
        """
        remove produto do estoque, após
        a compra
        :param product_name:
        :return: bool True , se remover, false se nao
        """
        prod = dict()
        for index, products in enumerate(cls.__store):
            if products["name"] == product_name:
                prod = products
                del cls.__store[index]
                return products
        return False

    @classmethod
    def list(cls) -> None:
        """
        Lista o estoque
        do mercado
        :return:
        """
        for product in cls.__store:
            print(f"Produto: {product['name']} | Preço R${product['price']}")

    @classmethod
    def select(cls, name: str) -> dict:
        for product in cls.__store:
            if product["name"] == name:
                return product
        return {"desculpe-nos": "Produto indisponível"}


if __name__ == '__main__':
    MarketStoreController.list()
    #MarketStoreController.remove("Notebook MarcaXX")
    MarketStoreController.list()
    x = MarketStoreController.select('Notebook MarcaXX')
    print(x)
