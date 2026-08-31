from fastapi import FastAPI

app=FastAPI(
    title="LeetLens API",
    description="AI-powered DSA weakness analyzer",
    version="0.1.0"
)


@app.get("/")
def root():
    return{
        "message":"Welcome to LeetLens API",
        "status":"running"
    }


@app.get("/health")
def health_check():
    return{
        "status":"healthy"
    }