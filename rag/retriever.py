def retrieve(query_embedding, vectorstore, k=5):
    return vectorstore.search(query_embedding, k)
