from fastapi import APIRouter, UploadFile, File
import shutil
import os

from rag.ingest import ingest_document

router = APIRouter()

UPLOAD_DIR = "data/documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process PDF into vector database
    chunks = ingest_document(file_path)

    return {
        "message": "File uploaded and processed successfully",
        "filename": file.filename,
        "chunks_created": chunks
    }