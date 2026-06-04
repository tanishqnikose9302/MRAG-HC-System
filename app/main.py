from fastapi import FastAPI
from pydantic import BaseModel

from rag.pipeline import advanced_rag

app = FastAPI(
    title="MRAG-HC System",
    description="Multilingual RAG with Hallucination Control",
    version="1.0"
)

# -----------------------------
# Request Schema
# -----------------------------
class QueryRequest(BaseModel):
    query: str


# -----------------------------
# Health Check
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "MRAG-HC API is running"
    }


# -----------------------------
# Main RAG Endpoint
# -----------------------------
@app.post("/ask")
def ask_question(request: QueryRequest):

    result = advanced_rag(request.query)

    return {
        "query": request.query,
        "answer": result["answer"],
        "confidence": result["confidence"],
        "sources": result["sources"]
    }
