from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import get_retriever
from rag.generator import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    retriever = get_retriever()

    docs = retriever.invoke(request.question)

    answer = generate_response(
        request.question,
        docs
    )

    return {
        "question": request.question,
        "answer": answer
    }