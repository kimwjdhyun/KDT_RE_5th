from fastapi import FastAPI
from app.db import get_connection
from app.routers import user

app = FastAPI()

@app.get("/")
def foot():
    return {"message": "FastAPI with MySQL"}

# 라우터 등록
app.include_router(user.router)


