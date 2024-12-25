# from flask import Flask, request, jsonify
# from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import asyncio
import websockets



# 初始化模型與模板
template = """
Answer the question below.

Here is the conversation history:{context}

Question:{question}

Ansewr:
"""
model = OllamaLLM(model = "llama3.1")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# 初始上下文
about_ecard = """Ecard Technology Consultant Co., Ltd., established in 2002, is a Gold-Level Professional Partner of Dassault Systèmes. In recent years, numerous enterprises have actively undertaken extensive reforms to integrate CAD (Computer-Aided Design), CAM (Computer-Aided Manufacturing), CAE (Computer-Aided Engineering), PDM (Product Data Management), and PLM (Product Lifecycle Management) into their corporate culture.
Ecard Technology positions itself as an engineering consultancy, offering tailored solutions to meet the needs of various industries. With a comprehensive suite of CAD, CAM, CAE, PDM systems, and reverse engineering equipment, we are equipped to address all challenges related to product design and development.
From 2007 to 2022, Ecard Technology was honored with the DS Greater China VAR Award for “Top Sales Contribution in Taiwan” for 14 consecutive years. Our professional technical expertise has consistently earned customer satisfaction and recognition. For inquiries regarding technical support or software-related needs, please do not hesitate to contact us. We are committed to providing you with sincere and professional service.

誼卡科技顧問股份有限公司，成立於2002年，為達梭系統黃金級的專業代理商。近幾年來，許多企業積極投入整合CAD、CAM、CAE以及PDM(產品資料管理，Product Data Management)，及PLM(產品生命週期管理，Product Life Management)企業整體文化大改革之工作。誼卡科技以工程顧問公司自許，我們針對企業界的需求，提出各種解決方案。本公司擁有一系列完整的CAD、CAM、CAE、PDM及逆向設備，可以為您解決關於產品設計、開發的各項問題。誼卡科技(2007~2022)連續14年獲得DS Great China VAR Award “Top Sales Contribution in Taiwan”，專業的技術能力獲得客戶的滿意與認同，不論是技術或是有關軟體的疑問和需求皆可來電洽詢，我們將誠摯為你服務。
"""

# 全域變數存儲上下文
connected_clients = []
# 處理客戶端連接
async def handle_client(websocket):
    """
    處理 WebSocket 客戶端連接
    """
    context = about_ecard  # 每個客戶端有自己的上下文
    try:
        async for message in websocket:
            # print(message)
            question = message.strip()
            if not question:
                await websocket.send("Error: No question provided")
                continue

            # 生成回答
            result = chain.invoke({"context": context, "question": question})
            context += f"\nUser: {question}\nAI: {result}"

            # 將回答發送回用戶
            await websocket.send(result)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected: {e}")

# 啟動 WebSocket 伺服器
async def main():
    """
    啟動 WebSocket 伺服器
    """
    server = await websockets.serve(handle_client, "0.0.0.0", 7800)
    print("WebSocket server started on ws://0.0.0.0:7600")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())