from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.upload import router as upload_router
from routes.chat import router as chat_router
from routes.health import router as health_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(health_router)

@app.get("/")
def home():
    return {"message": "Banking RAG Chatbot Backend Running"}