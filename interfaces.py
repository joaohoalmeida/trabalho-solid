from abc import ABC, abstractmethod

from models import (
    CategoriaModel,
    FormaPagamentoModel,
    ProdutoModel,
    VendaModel,
    VendaProduto,
)


class CategoriaDAOInterface(ABC):
    """Contrato de persistência para `CategoriaModel`."""

    @abstractmethod
    def inserir(self, categoria: CategoriaModel) -> int:
        """Persiste uma nova categoria e retorna o id gerado."""

    @abstractmethod
    def buscar_por_id(self, id: int) -> CategoriaModel | None:
        """Retorna a categoria do id informado, ou `None` se não existir."""

    @abstractmethod
    def listar(self) -> list[CategoriaModel]:
        """Retorna todas as categorias persistidas."""

    @abstractmethod
    def atualizar(self, categoria: CategoriaModel) -> None:
        """Atualiza os dados de uma categoria existente."""

    @abstractmethod
    def remover(self, id: int) -> None:
        """Remove a categoria do id informado."""


class ProdutoDAOInterface(ABC):
    """Contrato de persistência para `ProdutoModel`."""

    @abstractmethod
    def inserir(self, produto: ProdutoModel) -> int:
        """Persiste um novo produto e retorna o id gerado."""

    @abstractmethod
    def buscar_por_id(self, id: int) -> ProdutoModel | None:
        """Retorna o produto do id informado, ou `None` se não existir."""

    @abstractmethod
    def listar(self) -> list[ProdutoModel]:
        """Retorna todos os produtos persistidos."""

    @abstractmethod
    def atualizar(self, produto: ProdutoModel) -> None:
        """Atualiza os dados de um produto existente."""

    @abstractmethod
    def remover(self, id: int) -> None:
        """Remove o produto do id informado."""


class VendaDAOInterface(ABC):
    """Contrato de persistência para `VendaModel`."""

    @abstractmethod
    def inserir(self, venda: VendaModel) -> int:
        """Persiste uma nova venda e retorna o id gerado."""

    @abstractmethod
    def buscar_por_id(self, id: int) -> VendaModel | None:
        """Retorna a venda do id informado, ou `None` se não existir."""

    @abstractmethod
    def listar(self) -> list[VendaModel]:
        """Retorna todas as vendas persistidas."""

    @abstractmethod
    def atualizar(self, venda: VendaModel) -> None:
        """Atualiza os dados de uma venda existente."""

    @abstractmethod
    def remover(self, id: int) -> None:
        """Remove a venda do id informado."""


class FormaPagamentoDAOInterface(ABC):

    @abstractmethod
    def inserir(self, forma_pagamento: FormaPagamentoModel) -> int:
        """Persiste uma nova forma de pagamento e retorna o id gerado."""

    @abstractmethod
    def buscar_por_id(self, id: int) -> FormaPagamentoModel | None:
        """Retorna a forma de pagamento do id informado, ou `None`."""

    @abstractmethod
    def listar(self) -> list[FormaPagamentoModel]:
        """Retorna todas as formas de pagamento persistidas."""

    @abstractmethod
    def atualizar(self, forma_pagamento: FormaPagamentoModel) -> None:
        """Atualiza os dados de uma forma de pagamento existente."""

    @abstractmethod
    def remover(self, id: int) -> None:
        """Remove a forma de pagamento do id informado."""


class VendaProdutoDAOInterface(ABC):

    @abstractmethod
    def inserir(self, item: VendaProduto) -> None:
        """Persiste um novo item de venda."""

    @abstractmethod
    def listar(self) -> list[VendaProduto]:
        """Retorna todos os itens de venda persistidos."""

    @abstractmethod
    def listar_por_venda(self, id_venda: int) -> list[VendaProduto]:
        """Retorna todos os itens pertencentes à venda informada."""

    @abstractmethod
    def buscar_por_venda_e_produto(
        self, id_venda: int, id_produto: int
    ) -> VendaProduto | None:
        """Retorna o item da venda/produto informados, ou `None`."""

    @abstractmethod
    def atualizar(self, item: VendaProduto) -> None:
        """Atualiza um item de venda existente."""

    @abstractmethod
    def remover(self, id_venda: int, id_produto: int) -> None:
        """Remove o item da venda/produto informados."""
