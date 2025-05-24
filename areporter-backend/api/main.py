from fastapi import FastAPI
from .routes import reports

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 Add this CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
