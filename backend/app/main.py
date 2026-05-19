from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import books

app = FastAPI(title="FastAPI Bookstore", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router, prefix="/api/v1")


@app.get("/health")
async def health():
    return {"status": "ok"}
