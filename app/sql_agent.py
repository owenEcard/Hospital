import os
from langchain_ollama import OllamaLLM
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType
from langchain_community.utilities import SQLDatabase



# 初始化 LLM
llm = OllamaLLM(model="llama3.1")

# 確認資料庫檔案是否存在
if not os.path.exists("chinook.db"):
    print("Database file chinook.db not found in the project folder")
    exit()
 
# 初始化資料庫
try:
    db = SQLDatabase.from_uri("sqlite:///chinook.db", sample_rows_in_table_info=3)
    usable_tables = db.get_usable_table_names()
    # print("Tables:", usable_tables)

    if not usable_tables:
        print("No usable tables found. Please check the database file.")
        exit()
except Exception as e:
    print(f"Error loading database: {e}")
    exit()

# 初始化 SQL 代理
try:
    agent_executor = create_sql_agent(
        llm,
        db=db,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False  
    )
except Exception as e:
    print(f"Error initializing SQL agent: {e}")
    exit()




# 測試查詢功能
try:
    # query = "How many different Artists are in the database?"
    query = "How many unique tracks are in the database?"
    result = agent_executor.invoke(query)
    # 只打印輸出的結果
    print("Query result:", result['output'].strip())
    # print("Query result:", result)
except Exception as e:
    print(f"Error executing query: {e}")

