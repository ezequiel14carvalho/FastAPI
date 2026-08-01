from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido


order_router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@order_router.get("/")
async def pedidos():
    return {"Mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedidos(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    # use the request instance fields (pedido_schema) not the class
    novo_pedido = Pedido(usuario=pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"Mensagem": f"Pedido criado com sucesso. ID {novo_pedido.id}"}