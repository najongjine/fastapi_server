import asyncio
from datetime import datetime

from dbconnect import getConnect

# 데이터베이스 연결 확인. x 초마다 실행
async def batch_job():
    """Run a periodic job without a user request."""
    while True:
        try:
            conn = getConnect()
            try:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT NOW()")
                    total = cursor.fetchone()[0]
            finally:
                conn.close()

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[batch] {total}")
        except Exception as error:
            print(f"[batch error] {error}")

        await asyncio.sleep(30)
