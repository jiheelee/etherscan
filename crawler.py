from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from utils import safe_get_text

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)

def crawl_transactions(existing_hashes=set()):
    from config import BASE_URL
    driver = get_driver()
    driver.get(BASE_URL)
    time.sleep(3)

    try:
        view_all = driver.find_element(By.XPATH, "//a[contains(text(),'View All')]")
        view_all.click()
        time.sleep(2)
    except:
        pass

    data = []
    page = 1
    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        rows = soup.select("table tbody tr")
        new_tx_found = False

        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 9:
                continue
            tx_hash = safe_get_text(cols[0])
            if tx_hash in existing_hashes:
                driver.quit()
                return data

            block = safe_get_text(cols[1])
            age = safe_get_text(cols[2])
            action = safe_get_text(cols[3])
            token_out = safe_get_text(cols[4])
            token_in = safe_get_text(cols[5])
            rate = safe_get_text(cols[6])
            value = safe_get_text(cols[7])
            dex = safe_get_text(cols[8])

            data.append({
                "tx_hash": tx_hash,
                "block": block,
                "age": age,
                "action": action,
                "token_out": token_out,
                "token_in": token_in,
                "rate": rate,
                "value": value,
                "dex": dex
            })
            new_tx_found = True

        try:
            next_btn = driver.find_element(By.XPATH, "//a[contains(text(),'Next')]")
            next_btn.click()
            time.sleep(2)
            page += 1
        except:
            break

        if not new_tx_found:
            break

    driver.quit()
    return data
