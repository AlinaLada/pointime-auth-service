from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Pointime Auth Service"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Pointime Auth Service"
    }