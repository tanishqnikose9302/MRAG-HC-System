#FINAL ENHANCED PIPELINE (PHASE 2)
from hallucination.verifier import verify_answer
from hallucination.scorer import confidence_score

def advanced_rag(query, vectorstore):
    query_emb = get_embedding(query)
    docs = vectorstore.search(query_emb)

    context = "\n".join(docs)
    answer = generate_answer(context, query)

    verified = verify_answer(answer, context)
    confidence = confidence_score(query, docs)

    return {
        "answer": answer if verified else "Low confidence answer blocked",
        "confidence": confidence,
        "sources": docs
    }
