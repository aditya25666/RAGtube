from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="YouTube RAG",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "YouTube RAG API is running."
    }

app = FastAPI(
    title="YouTube RAG"
)

app.include_router(router)