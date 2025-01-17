"""from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
{"conversationId":"b0066ee6-d0e3-4cdc-80b0-ad5b121cbd0a","source":"instruct"}  # Import BaseModel for request validation
from openai_service import generate_response
from db import get_relevant_context
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
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Define the QueryRequest model
class QueryRequest(BaseModel):
    user_query: str

@app.post("/query")
async def query_chatbot(request: QueryRequest):
    # Extract the user_query from the request
    user_query = request.user_query

    # Retrieve relevant context from the knowledge base
    context = get_relevant_context(user_query)

    # Generate a response using OpenAI
    try:
        response = generate_response(user_query, context)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"response": response} """




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
