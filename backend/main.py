
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HeritageLens AI API",
    description="API for exploring and searching cultural heritage archives.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to HeritageLens AI API",
        "status": "running",
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "project": "HeritageLens AI",
    }
