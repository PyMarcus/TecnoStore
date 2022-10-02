from models.Market import Market
from MarketStoreController import MarketStoreController


class Client:
    """
    Classe Controladora do cliente
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
        self.__name = name  # atributos privados garantem o encapsulamento
        self.__cpf = cpf
        self.__birth = birth
        self.__cash = cash
        self.__email = email
        self.__card = []  # carrinho
        self.market: Market = Market()
        self.market_products: MarketStoreController = MarketStoreController()

    # get method
    @property
    def cash(self) -> float:
        return self.__cash

    def buy(self):
        """
        Compra itens do mercado
        :param product_name
        :return:
        """
        names: list = list()
        if len(self.__card) > 0:
            for items in self.__card:
                names.append(items['name'])
                self.__cash -= items['price']  # deduz da carteira do cliente
            self.market.sell(self.__name, names)
        else:
            print("Por favor, adicione itens ao seu carrinho, antes de efetuar a compra!")

    def add_to_card(self, product: str) -> None:
        """
        Adiciona produto ao carrinho de compra
        :param product:
        :return:
        """
        content: list[dict] = [self.market_products.select(product)]
        if "desculpe-nos" in content[0].keys():
            print(f"[-]{content[0].get('desculpe-nos')}")
        else:
            for items in content:
                if items["name"] == product:
                    self.__card.append(items)
                    print(f"[+]{items['name']} foi adicionado ao seu carrinho")
                    break

    def remove_from_card(self, name_of_product: str) -> None:
        """
        Remove item do carrinho de compra
        :return:
        """
        if len(self.__card) > 0:
            for index, items in enumerate(self.__card):
                if items['name'] == name_of_product:
                    print(f"[+]{items['name']} foi removido do seu carrinho de compras")
                    del self.__card[index]
                    break
        else:
            print("Carrinho vazio!")

    def show_card(self) -> None:
        """
        Exibe itens do carrinho do cliente
        :return:
        """
        print(f"___" * 13)
        print("\t\t[+] Seu carrinho:")
        if len(self.__card) > 0:
            total = 0
            for itens in self.__card:
                print(f"\t{itens['name']} - R${itens['price']}")
                total += itens['price']
            print(f"\nTOTAL: R${total:.2f}")
            print(f"\n{' ' * 9} TecnoStore®")
            print(f"___" * 13)
        else:
            print("Carrinho vazio!")

    def show_items_from_market(self):
        self.market.show_items()


if __name__ == '__main__':
    client = Client("Marcus", "111.111.111-11", "XX/XX", 10000.00, "marcus@email.com")
    print(client.cash)
    client.add_to_card("Notebook MarcaXX")
    client.add_to_card("Notebook MarcaY2Y")
    client.add_to_card("Notebook MarcaYY")
    client.show_card()
    client.buy()
