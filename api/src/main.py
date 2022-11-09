from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.api import api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

@app.get('/')
def hello():
    return 'hello from main'

app.include_router(api_router, prefix="/api")