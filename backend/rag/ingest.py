import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "vectorstore"

# Create vectorstore folder automatically
os.makedirs(CHROMA_PATH, exist_ok=True)


def ingest_document(file_path):

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    # Lightweight embeddings
    embeddings = FakeEmbeddings(size=384)

    # Store in ChromaDB
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    vectordb.persist()

    return len(chunks)