from fastapi import FastAPI
import redis
import psycopg2
import os

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"message": "Production-Ready Containerized App"}

@app.get("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host="db"
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"db_status": "connected" if result[0] == 1 else "error"}
    except Exception as e:
        return {"db_status": f"error - {str(e)}"}

@app.get("/redis")
def redis_check():
    try:
        r.ping()
        return {"redis_status": "connected"}
    except redis.exceptions.ConnectionError:
        return {"redis_status": "not connected"}

