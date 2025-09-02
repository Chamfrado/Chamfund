import os

from fastapi import APIRouter, Request, Response

from .utils import log

router = APIRouter()
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "")


@router.get("/webhook")
async def verify(
    hub_mode: str | None = None,
    hub_challenge: str | None = None,
    hub_verify_token: str | None = None,
):
    """Rota de verificação do WhatsApp (GET)."""
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return Response(content=hub_challenge or "", media_type="text/plain")
    return Response(status_code=403)


@router.post("/webhook")
async def webhook(req: Request):
    """Recebe eventos do WhatsApp (mensagens, status etc.)."""
    body = await req.json()
    log.info(f"Webhook recebido: {body}")

    # Aqui no futuro vamos tratar mensagens de texto e imagem.
    # Por enquanto, só loga e devolve 200.

    return Response(status_code=200)
