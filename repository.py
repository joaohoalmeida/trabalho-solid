"""Repositórios em memória para os modelos do domínio."""

from __future__ import annotations

from interfaces import (
    CategoriaDAOInterface,
    FormaPagamentoDAOInterface,
    ProdutoDAOInterface,
    VendaDAOInterface,
    VendaProdutoDAOInterface,
)
from models import (
    CategoriaModel,
    FormaPagamentoModel,
    ProdutoModel,
    VendaModel,
    VendaProduto,
)


class CategoriaRepository(CategoriaDAOInterface):
    """Repositório em memória para `CategoriaModel`."""

    def __init__(self) -> None:
        self._categorias: dict[int, CategoriaModel] = {}
        self._proximo_id = 1

    def inserir(self, categoria: CategoriaModel) -> int:
        categoria.id = self._proximo_id
        self._categorias[categoria.id] = categoria
        self._proximo_id += 1
        return categoria.id

    def buscar_por_id(self, id: int) -> CategoriaModel | None:
        return self._categorias.get(id)

    def listar(self) -> list[CategoriaModel]:
        return list(self._categorias.values())

    def atualizar(self, categoria: CategoriaModel) -> None:
        if categoria.id not in self._categorias:
            raise KeyError(f"Categoria com id={categoria.id} não encontrada")
        self._categorias[categoria.id] = categoria

    def remover(self, id: int) -> None:
        self._categorias.pop(id, None)


class ProdutoRepository(ProdutoDAOInterface):
    """Repositório em memória para `ProdutoModel`."""

    def __init__(self) -> None:
        self._produtos: dict[int, ProdutoModel] = {}
        self._proximo_id = 1

    def inserir(self, produto: ProdutoModel) -> int:
        produto.id = self._proximo_id
        self._produtos[produto.id] = produto
        self._proximo_id += 1
        return produto.id

    def buscar_por_id(self, id: int) -> ProdutoModel | None:
        return self._produtos.get(id)

    def listar(self) -> list[ProdutoModel]:
        return list(self._produtos.values())

    def atualizar(self, produto: ProdutoModel) -> None:
        if produto.id not in self._produtos:
            raise KeyError(f"Produto com id={produto.id} não encontrado")
        self._produtos[produto.id] = produto

    def remover(self, id: int) -> None:
        self._produtos.pop(id, None)


class VendaRepository(VendaDAOInterface):
    """Repositório em memória para `VendaModel`."""

    def __init__(self) -> None:
        self._vendas: dict[int, VendaModel] = {}
        self._proximo_id = 1

    def inserir(self, venda: VendaModel) -> int:
        venda.id = self._proximo_id
        self._vendas[venda.id] = venda
        self._proximo_id += 1
        return venda.id

    def buscar_por_id(self, id: int) -> VendaModel | None:
        return self._vendas.get(id)

    def listar(self) -> list[VendaModel]:
        return list(self._vendas.values())

    def atualizar(self, venda: VendaModel) -> None:
        if venda.id not in self._vendas:
            raise KeyError(f"Venda com id={venda.id} não encontrada")
        self._vendas[venda.id] = venda

    def remover(self, id: int) -> None:
        self._vendas.pop(id, None)


class FormaPagamentoRepository(FormaPagamentoDAOInterface):
    """Repositório em memória para `FormaPagamentoModel`."""

    def __init__(self) -> None:
        self._formas: dict[int, FormaPagamentoModel] = {}
        self._proximo_id = 1

    def inserir(self, forma_pagamento: FormaPagamentoModel) -> int:
        forma_pagamento.id = self._proximo_id
        self._formas[forma_pagamento.id] = forma_pagamento
        self._proximo_id += 1
        return forma_pagamento.id

    def buscar_por_id(self, id: int) -> FormaPagamentoModel | None:
        return self._formas.get(id)

    def listar(self) -> list[FormaPagamentoModel]:
        return list(self._formas.values())

    def atualizar(self, forma_pagamento: FormaPagamentoModel) -> None:
        if forma_pagamento.id not in self._formas:
            raise KeyError(
                f"Forma de pagamento com id={forma_pagamento.id} não encontrada"
            )
        self._formas[forma_pagamento.id] = forma_pagamento

    def remover(self, id: int) -> None:
        self._formas.pop(id, None)


class VendaProdutoRepository(VendaProdutoDAOInterface):
    """Repositório em memória para `VendaProduto` (chave composta)."""

    def __init__(self) -> None:
        self._itens: dict[tuple[int, int], VendaProduto] = {}

    @staticmethod
    def _chave(item: VendaProduto) -> tuple[int, int]:
        return (item.venda.id, item.produto.id)

    def inserir(self, item: VendaProduto) -> None:
        self._itens[self._chave(item)] = item

    def listar(self) -> list[VendaProduto]:
        return list(self._itens.values())

    def listar_por_venda(self, id_venda: int) -> list[VendaProduto]:
        return [item for item in self._itens.values() if item.venda.id == id_venda]

    def buscar_por_venda_e_produto(self, id_venda: int, id_produto: int) -> VendaProduto | None:
        return self._itens.get((id_venda, id_produto))

    def atualizar(self, item: VendaProduto) -> None:
        chave = self._chave(item)
        if chave not in self._itens:
            raise KeyError(f"Item de venda {chave} não encontrado")
        self._itens[chave] = item

    def remover(self, id_venda: int, id_produto: int) -> None:
        self._itens.pop((id_venda, id_produto), None)
