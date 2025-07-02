from fastapi import FastAPI, Depends
from app.security import get_current_user
from app.rag_pipeline import generate_answer
from app.mlflow_tracker import track_query

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "🚀 HealthMLOpsX API up and running!"}

@app.get("/rag/")
async def rag_endpoint(query: str, user=Depends(get_current_user)):
    result = generate_answer(query)
    track_query(query, result["answer"])
    return result


@app.get("/secure-endpoint")
async def secure_endpoint(user: dict = Depends(get_current_user)):
    return {"message": f"Hello, {user['username']}!"}
