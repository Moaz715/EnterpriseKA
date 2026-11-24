from fastapi import FastAPI
from app.apis.router import api_router

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Enterprise Knowledge Assistant API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}