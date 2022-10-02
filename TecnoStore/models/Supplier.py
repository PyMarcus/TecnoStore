from typing import TypeVar
from controllers.SupplierController import SupplierController


T = TypeVar("T")  # tipo genérico


class Supplier:
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
        self.__controller: SupplierController = SupplierController()

    def sell(self, product_name: str = None) -> dict[T, T]:
        """
        Método que vende os produtos solicitados
        ao mercado
        :param product_name:
        :return: produto solicitado
        """
        return self.__controller.sell(product_name=product_name)

    def show_content(self) -> None:
        """
        Exibe os produtos disponíveis para a venda
        :return:
        """
        self.__controller.show_content()


if __name__ == '__main__':
    supplier_debug = Supplier()
    supplier_debug.show_content()
    supplier_debug.sell('Notebook1 MarcaX')
    supplier_debug.show_content()
