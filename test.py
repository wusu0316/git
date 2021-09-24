import os
import time
from selenium import webdriver



def test_ota(ip):
    driver = webdriver.Chrome(executable_path=r"C:\webdriver\chromedriver.exe")
    try:
        driver.get('http://{0}:8888/gem/mmx/connect'.format(ip))
        time.sleep(2)
    except Exception as e:
        print(e)
    finally:
        driver.quit()



if __name__ == '__main__':
    test_ota("10.80.101.10")

