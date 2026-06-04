#PIPELINE (RAG CORE)
from embeddings.embedder import get_embedding
from rag.generator import generate_answer

def rag_pipeline(query, vectorstore):
    query_emb = get_embedding(query)
    docs = vectorstore.search(query_emb)

    context = "\n".join(docs)
    answer = generate_answer(context, query)

    return answer, docs
