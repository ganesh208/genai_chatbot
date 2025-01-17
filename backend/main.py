from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai_service import generate_response
from pinecone_db import get_relevant_context
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Replace with your frontend URL
    # Add other allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    user_query: str

@app.post("/query")
async def query_chatbot(request: QueryRequest):
    user_query = request.user_query
    try:
        context = get_relevant_context(user_query)
        response = generate_response(user_query, context)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"response": response}
