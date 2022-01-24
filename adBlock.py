# x-button : ytp-ad-overlay-close-button
# skip-button : ytp-ad-skip-button ytp-button
from selenium import webdriver
import time

try:
        
    driver = webdriver.Chrome() # dist\python 파일명 에 chromedriver를 비롯한 필요파일
    driver.get("https://www.naver.com")
except Exception as e:
    print(e)
print('test')
time.sleep(3)