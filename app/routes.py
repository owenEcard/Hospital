from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import MockData
from .llama_client import llama_query

router = APIRouter()

@router.get("/mockdata")
def read_mock_data(db: Session = Depends(get_db)):
    return db.query(MockData).all()

@router.post("/llama")
def call_llama(prompt: str):
    result = llama_query(prompt)
    return {"response": result}
