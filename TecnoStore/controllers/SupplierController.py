import time
from typing import TypeVar
from models.Product import Product
from .SupplierStoreController import SupplierStoreController


T = TypeVar("T")  # tipo genérico


class SupplierController:
    """
    [O estoque do fornecedor nao será limitado]
    Classe do fornecedor
    possui metodos para venda e
    listagem dos produtos disponíveis
    para venda ao cliente

    Esta classe interage apenas com a
    loja, favorecendo, desse modo o baixo
    acoplamento
    """
    def __init__(self) -> None:
        """
        disponibiliza
        para os clientes
        os produtos advindos do estoque
        """
        self.__controller: SupplierStoreController = SupplierStoreController()
        self.__store: list[dict] = self.__controller.products
        self.__product: dict = self.__controller.content()

    # método get
    @property
    def store(self):
        return self.__store

    @staticmethod
    def __customize_msg_box(producto) -> None:
        """
        Apenas exibe na saída padrão
        uma mensagem como se estivesse carregando
        :return:
        """
        print(f"[*] Produto em falta no estoque.")
        time.sleep(1)
        print(f"[+] Buscando produto", end="")
        for n in range(1, 6):
            print('.', end='', flush=True)
            time.sleep(1)
        print()

    def sell(self, product_name: str = None) -> dict[T, T]:
        """
        Método que vende os produtos solicitados
        ao mercado
        :param product_name:
        :return: produto solicitado
        """
        for product in self.__product:
            if product_name == product["name"]:
                return product
        # se nao existir, cria o produto no estoque e retorna
        producto: dict = Product(product_name).create()
        self.__customize_msg_box(producto)
        self.store.append(producto)
        for product in self.__product:
            if product_name == product["name"]:
                return product

    def show_content(self) -> None:
        """
        Exibe os produtos disponíveis para a venda
        :return:
        """
        for product in self.store:
            print(product)


if __name__ == '__main__':
    supplier_debug = SupplierController()
    supplier_debug.show_content()
    supplier_debug.sell('Notebook1 MarcaX')
    supplier_debug.show_content()
