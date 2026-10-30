from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import exercicios
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gym Progress API")

@app.get("/")
def root():
    return {"status": "ok"}
app.include_router(exercicios.router)
app.mount("/app", StaticFiles(directory="frontend", html=True), name="frontend")


