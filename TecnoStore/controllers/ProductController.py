import string
from random import choice


class ProductController:
    """
    Os produtos da TecnoStore são,
    majoritariamente, notebooks e desktops
    Esta classe segue o padrão criador e ela retorna um
    produto do nicho
    [Atendendo ao padrão controller, essencialmente]
    """

    letters_up: str = string.ascii_uppercase
    nicho: tuple[str] = (f"Notebook modelo{choice(letters_up)}",
                         f"Desktop modelo{choice(letters_up)}")
    value: list[float] = list(range(2000, 10000))  # embora ocupe memória, é mais prático

    def __init__(self, name: str = None, price: float = None):
        if name is None:
            self.__name = choice(self.nicho)
        else:
            self.__name = name
        if price is None:
            self.__price = choice(self.value)
        else:
            self.__price = price

    # get methods
    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    # methods
    def create(self) -> dict[str, float]:
        """
        Cria um novo produto
        :return: dicionario com informacoes do produto criado
        """
        return {"name": self.name, "price": self.price}
