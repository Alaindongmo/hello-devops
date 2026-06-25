from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello DevOps v2!", "status": "running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
