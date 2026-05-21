from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import get_retriever
from rag.generator import generate_response
from rag.memory import save_message, get_history

router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    session_id: str


@router.post("/chat")
async def chat(request: ChatRequest):

    retriever = get_retriever()

    docs = retriever.invoke(
        request.question
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    history = get_history(request.session_id)

    history_text = ""

    for msg in history:
        history_text += f"{msg['role']}: {msg['content']}\n"

    final_context = history_text + "\n" + context

    answer = generate_response(
        final_context,
        request.question
    )

    save_message(
        request.session_id,
        "user",
        request.question
    )

    save_message(
        request.session_id,
        "assistant",
        answer
    )

    return {
        "session_id": request.session_id,
        "question": request.question,
        "answer": answer
    }