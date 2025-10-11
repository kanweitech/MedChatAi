from fastapi import FastAPI
from app.routers.chat import router as chat_router
from app.middleware.request_logger import log_requests

app = FastAPI(title="MedChatBot", version="0.1.0")

# Register middleware
app.middleware("http")(log_requests)


app.include_router(chat_router)

@app.get("/")
async def health():
    return {"message": "MedChat AI backend is running successfully. 🚀"}
