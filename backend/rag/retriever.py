from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "vectorstore"


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={
            "k": 2
        }
    )

    return retriever