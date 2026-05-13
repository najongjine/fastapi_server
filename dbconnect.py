import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def getConnect():
    """Create a PostgreSQL connection."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def create_table():
    """Create sample memo tables if they do not exist."""
    desc_sql = """
    CREATE TABLE IF NOT EXISTS t_title (
        id SERIAL PRIMARY KEY,
        title VARCHAR NOT NULL,
        subtitle VARCHAR,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    contents_sql = """
    CREATE TABLE IF NOT EXISTS t_item (
        id SERIAL PRIMARY KEY,
        content VARCHAR NOT NULL,
        img_url TEXT,
        cnt INT4 DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    conn = getConnect()
    try:
        with conn.cursor() as cursor:
            cursor.execute(desc_sql)
            cursor.execute(contents_sql)
            conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    return {"result": "success"}
