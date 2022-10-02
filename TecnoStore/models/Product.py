from controllers.ProductController import ProductController


class Product:
    """
    Os produtos da TecnoStore são,
    majoritariamente, notebooks e desktops
    Esta classe segue o padrão criador e ela retorna um
    produto do nicho
    [Atendendo ao padrão criador(CREATOR), essencialmente]
    """
    def __init__(self, name: str = None, price: float = None):
        self.product: ProductController = ProductController(name, price)  # acoplamento

    def create(self) -> dict[str, float]:
        """
        Cria um novo produto
        :return: dicionario com informacoes do produto criado
        """
        return self.product.create()

    def show_product(self) -> str:
        return self.product.name

    def show_price(self) -> float:
        return self.product.price


if __name__ == '__main__':
    debug = Product('Notebook', 123.22)
    print(debug.create())
