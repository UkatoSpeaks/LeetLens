from fastapi import FastAPI

from app.api.submission import router as submission_router
from app.api.auth import router as auth_router
from app.api.problems import router as problem_router
from app.api.leetcode import router as leetcode_router

app = FastAPI(
    title="LeetLens API",
    description="AI-powered DSA weakness analyzer",
    version="0.1.0",
)


app.include_router(auth_router)
app.include_router(problem_router)
app.include_router(submission_router)
app.include_router(leetcode_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to LeetLens API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }