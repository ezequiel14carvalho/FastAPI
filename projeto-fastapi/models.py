from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

# cria a conexão do seu banco
db = create_engine("sqlite:///banco.db")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    #STATUS_PEDIDOS = (("PENDENTE", "PENDENTE"), ("CANCELADO", "CANCELADO"), ("FINALIZADO", "FINALIZADO"))

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    usuario = Column("usuario", ForeignKey(Usuario.id))
    status = Column("status", String)
    preco = Column("preco", Float)

    def __unit__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco


class ItemPedido(Base):
    __tablename__ = "itens_pedidos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    pedido = Column("pedido", ForeignKey(Pedido.id))
    tamanho = Column("tamanho", String)
    sabor = Column("sabor", String)
    preco_unitario = Column("preco_unitario", Float)

    def __unit__(self, pedido, tamanho, sabor, preco_unitario):
        self.pedido = pedido
        self.tamanho = tamanho
        self.sabor = sabor
        self.preco_unitario = preco_unitario