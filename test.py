import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

def test_ota(ip):

    try:
        driver.get('http://{0}:8888/gem/mmx/connect'.format(ip))
        time.sleep(2)
    except Exception as e:
        print(e)
    finally:
        driver.quit()



if __name__ == '__main__':
    test_ota("10.80.101.10")

