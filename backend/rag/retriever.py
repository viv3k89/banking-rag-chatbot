from langchain_community.embeddings import FakeEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "vectorstore"


def get_retriever():

    embeddings = FakeEmbeddings(size=384)

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