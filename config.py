TOKEN_ADDRESS = "0xdac17f958d2ee523a2206206994597c13d831ec7"  # USDT
BASE_URL = f"https://etherscan.io/dex?q={TOKEN_ADDRESS}#transactions"
CSV_PATH = "data/transactions.csv"
DB_PATH = "data/transactions.db"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"
MAX_SLACK_RETRIES = 3
