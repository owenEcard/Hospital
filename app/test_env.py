import psycopg2

DATABASE_URL = "postgresql+psycopg2://postgres:Qwer1234@localhost:5432/hospital"

try:
    conn = psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="Qwer1234",
        host="localhost",
        port="5432"
    )
    print("Database connection successful")
    conn.close()
except Exception as e:
    print(f"Database connection failed: {e}")
