import pandas as pd
import sqlite3
from config import CSV_PATH, DB_PATH

def save_to_csv(data):
    df = pd.DataFrame(data)
    try:
        old = pd.read_csv(CSV_PATH)
        df = pd.concat([old, df]).drop_duplicates(subset=["tx_hash"])
    except FileNotFoundError:
        pass
    df.to_csv(CSV_PATH, index=False)

def save_to_db(data):
    conn = sqlite3.connect(DB_PATH)
    df = pd.DataFrame(data)
    df.to_sql("transactions", conn, if_exists="append", index=False)
    conn.close()
