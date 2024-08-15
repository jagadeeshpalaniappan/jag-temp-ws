import ai_utils
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma

raw_prompt = PromptTemplate.from_template(
    """ 
    <s>[INST] You are a technical assistant good at searching docuemnts. If you do not have an answer from the provided information say so. [/INST] </s>
    [INST] {input}
           Context: {context}
           Answer:
    [/INST]
    """
)


def ask_ai_with_knowledge(query):
    # 1. Loading Vector DB (Chroma)
    vector_store = Chroma(
        persist_directory=ai_utils.chroma_db_storage_path,
        embedding_function=ai_utils.embedding_fn,
    )

    # 2. Getting Vector DB (Chroma) - retriever
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 20, "score_threshold": 0.1},
    )

    # 2. Creating Doc Chain
    document_chain = create_stuff_documents_chain(ai_utils.llm, raw_prompt)

    # 3. Creating Retrieval Chain
    chain = create_retrieval_chain(retriever, document_chain)

    # 4. Invoke query using that chain
    result = chain.invoke({"input": query})
    # print(result)

    # 5. Print only the answer
    # print(result["answer"])

    # 6. Print answer and sources
    sources = []
    for doc in result["context"]:
        sources.append(
            {"source": doc.metadata["source"], "page_content": doc.page_content}
        )

    response_answer = {"answer": result["answer"], "sources": sources}
    # print(response_answer)

    return result["answer"]
