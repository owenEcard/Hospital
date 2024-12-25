import asyncio
import websockets
import json

PORT = 7500

async def send_test_data(websocket):
    try:
        while True:
            with open('testData.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            await websocket.send(json.dumps(data))
            print("已向客户端发送数据")
            await asyncio.sleep(30)  # 每5秒发送一次数据
    except websockets.exceptions.ConnectionClosedOK:
        print("客户端已断开连接")

async def main():
    async with websockets.serve(send_test_data, 'localhost', PORT):
        print(f"WebSocket服务器已在ws://localhost:{PORT}运行")
        await asyncio.Future()  # 保持服务器运行

if __name__ == "__main__":
    asyncio.run(main())
