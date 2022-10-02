class SupplierStoreController:
    def __init__(self):
        self.__products: list[dict] = [
            {
                "name": "Notebook MarcaX",
                "price": 3405.40
            },
            {
                "name": "Notebook MarcaY",
                "price": 2405.40
            },
            {
                "name": "Notebook Marcaz",
                "price": 1425.44
            },
            {
                "name": "Desktop MarcaA",
                "price": 8425.44
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
            {
                "name": "Notebook MarcaU",
                "price": 23405.40
            },
            {
                "name": "Notebook MarcaM",
                "price": 9999.99
            },
            {
                "name": "Notebook MarcaV",
                "price": 1929.69
            },
        ]

    # get method
    @property
    def products(self) -> list[dict]:
        return self.__products

    def content(self) -> dict:
        """
        retorna cada produto
        como um generator
        para otimizar memória e processamento
        :return: dict
        """
        for item in self.products:
            yield item

    # methods
    def add_item(self, item: dict) -> None:
        """
        adiciona item ao array
        do fornecedor, se o item
        nao existir
        :param: item {"name": string, "price": float}
        :return: None
        """
        assert type(item) == dict
        try:
            if item["name"] and item["price"]:
                if item not in self.products:
                    self.products.append(item)
                    print("Produto adquirido!")
                else:
                    print("Este produto já se encontra no estoque")
        except KeyError:
            print("O Produto não atende ao padrão \n"
                  "{'name': string, 'price': float}")


if __name__ == '__main__':
    debug = SupplierStoreController()
    for n in debug.content():   # conteúdos
        print(n)
    debug.add_item(
        {
            "name": "Desktop ultimate",
            "price": 10000.00
        }
    )  # adiciona ao estoque
