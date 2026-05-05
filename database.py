```python name=database.py
import aiosqlite
import os

DB_PATH = os.getenv("DB_PATH", "data/db.sqlite")

TABLES = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance INTEGER DEFAULT 100,
    farm_img_url TEXT
);
"""

async def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(TABLES)
        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT user_id, username, balance, farm_img_url FROM users WHERE user_id=?", (user_id,))
        return await cur.fetchone()

async def create_user(user_id, username, farm_img_url):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username, balance, farm_img_url) VALUES (?, ?, ?, ?)",
            (user_id, username, 100, farm_img_url)
        )
        await db.commit()
```
