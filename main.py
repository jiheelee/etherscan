import pandas as pd
from crawler import crawl_transactions
from storage import save_to_csv, save_to_db
from notifier import send_slack_message
from config import CSV_PATH
import os


def run_job():
    os.makedirs("data", exist_ok=True)
    try:
        try:
            existing = pd.read_csv(CSV_PATH)
            existing_hashes = set(existing["tx_hash"])
        except FileNotFoundError:
            existing_hashes = set()

        data = crawl_transactions(existing_hashes)
        save_to_csv(data)
        save_to_db(data)
        send_slack_message(f"✅ {len(data)}건 수집 완료")
    except Exception as e:
        send_slack_message(f"❌ 오류 발생: {str(e)}")
