from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@order_router.get("/")
async def pedidos():
    return {"Mensagem": "Voce acessou a rota de pedidos"}