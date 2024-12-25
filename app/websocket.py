from fastapi import APIRouter, WebSocket
from sqlalchemy.orm import Session
from app.models import MockData
from app.database import SessionLocal

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 手動建立資料庫連接
    db: Session = SessionLocal()
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            # 將接收到的資料存入資料庫
            new_data = MockData(content=data)
            db.add(new_data)
            db.commit()
            # 回傳處理結果
            await websocket.send_text(f"Data received: {data}")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        # 確保資料庫會話被正確關閉
        db.close()
        await websocket.close()
