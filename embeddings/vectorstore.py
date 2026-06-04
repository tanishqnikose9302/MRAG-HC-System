import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []

    def add(self, embeddings, texts):
        self.index.add(np.array(embeddings))
        self.docs.extend(texts)

    def search(self, query_embedding, k=5):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [self.docs[i] for i in indices[0]]
