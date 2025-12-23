from fastapi import FastAPI

app = FastAPI(title="Market Analysis API")

@app.get("/")
def root():
    return {"message": "API is running"}
