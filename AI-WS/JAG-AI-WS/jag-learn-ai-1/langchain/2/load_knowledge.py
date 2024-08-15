import ai_utils
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.vectorstores import Chroma


# Convert PDF file into Embeddings and Store the Embeddings into Chroma DB (Vector DB)
def load_knowledge(file_name):

    # 1. Load PDF file
    loader = PDFPlumberLoader(file_name)

    # 1. Split PDF file into Chunks
    docs = loader.load_and_split()
    chunks = ai_utils.text_splitter.split_documents(docs)

    print(f"docs len={len(docs)}")
    print(f"chunks len={len(chunks)}")

    # 2. Store PDF chunks into Vector DB (Chroma) as Embeddings using 'embedding_fn' and storage location is './db/...'
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=ai_utils.embedding_fn,
        persist_directory=ai_utils.chroma_db_storage_path,
    )
    vector_store.persist()

    response = {
        "status": "Successfully Uploaded",
        "filename": file_name,
        "doc_len": len(docs),
        "chunks": len(chunks),
    }

    return response
