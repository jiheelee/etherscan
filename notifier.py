import requests
import time
from config import SLACK_WEBHOOK_URL, MAX_SLACK_RETRIES

def send_slack_message(message):
    for attempt in range(MAX_SLACK_RETRIES):
        try:
            res = requests.post(SLACK_WEBHOOK_URL, json={"text": message})
            if res.status_code == 200:
                return
        except Exception as e:
            time.sleep(2)
    print("Slack 알림 실패:", message)
