from dataclasses import dataclass
from enum import Enum


@dataclass
class CategoriaModel:
    id: int
    tipo_categoria: str
    descricao: str
    margem_lucro: float


@dataclass
class VendaModel:
    id: int
    datahora_venda: str
    desconto: float


class TipoPagamento(Enum):
    PIX = 1
    CREDITO = 2
    DEBITO = 3
    ESPECIE = 4


@dataclass
class FormaPagamentoModel:
    id: int
    tipo_pagamento: TipoPagamento
    valor_pago: float
    venda: VendaModel


@dataclass
class ProdutoModel:
    id: int
    nome: str
    descricao: str
    preco: float
    quantidade_estoque: int
    alerta_estoque_baixo: int
    codigo_interno: int
    margem_lucro: float
    categoria: CategoriaModel


@dataclass
class VendaProduto:
    quantidade_vendida: int
    preco_momento_venda: float
    venda: VendaModel
    produto: ProdutoModel
