from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_index(text):
    # Split teks jadi chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Buat embedding dan FAISS index
    embeddings = HuggingFaceEmbeddings()
    return FAISS.from_documents(docs, embeddings)

def query_index(query, index, k=3):
    results = index.similarity_search(query, k=k)
    return [r.page_content for r in results]