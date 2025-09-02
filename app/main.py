import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from .routes import router as whatsapp_router

load_dotenv()

app = FastAPI(title="WhatsApp Bot (Python)")


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "BOT WhatsApp: online ✅"


app.include_router(whatsapp_router)

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
