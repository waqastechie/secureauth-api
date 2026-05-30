from fastapi import FastAPI

app = FastAPI(title="SecureAuth API")

@app.get("/")
def root():
    return {"message": "SecureAuth API is running"}