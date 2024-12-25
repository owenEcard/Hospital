from fastapi import FastAPI
from app.routes import router as api_router
from app.websocket import router as ws_router
from app.database import Base, engine

# 初始化資料庫
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 註冊路由
app.include_router(api_router, prefix="/api")
# app.include_router(ws_router, prefix="/ws")
