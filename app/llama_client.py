import requests
import os
from dotenv import load_dotenv

load_dotenv()

LLAMA_API_URL = os.getenv("LLAMA_API_URL")

def llama_query(prompt: str):
    payload = {
        "model": "Llama3.2:latest",
        "messages": [{"role": "user", "content": prompt}]
    }
    try:
        response = requests.post(LLAMA_API_URL, json=payload)
        response.raise_for_status()  # 確保 HTTP 狀態碼是 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# 測試函數
if __name__ == "__main__":
    prompt = "請說明Llama模型的應用場景。"
    print(f"Testing connection to Llama API at {LLAMA_API_URL}")
    result = llama_query(prompt)
    if result:
        print("Response from Llama API:", result)
    else:
        print("Failed to get a response from Llama API.")
