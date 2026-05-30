from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SecureAuth API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "SecureAuth API is running"}