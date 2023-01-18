import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from services.process import Process
import time
from time import sleep

def main():
    BrowserPath = ResourcePath("./browser/chrome.exe")
    DriverPath = ResourcePath("./driver/chromedriver.exe")

    # ウェブドライバ設定
    options = Options()
    options.binary_location = BrowserPath
    options.add_argument("--headless")  # 動きを見たい場合はコメントアウトする。
    driver = webdriver.Chrome(DriverPath, options=options)

    # スクレイピング
    ProcessC = Process(driver)
    ProcessC.goPage()

    # クローズ処理
    time.sleep(15)
    driver.close()
    driver.quit()

def ResourcePath(relativePath):
    try:
        basePath=sys._MEIPASS
    except Exception:
        basePath=os.path.dirname(__file__)
    return os.path.join(basePath, relativePath)

if __name__ == '__main__':
    main()
