# x-button : ytp-ad-overlay-close-button
# skip-button : ytp-ad-skip-button ytp-button

from selenium import webdriver
import time

try:
    # driver = webdriver.Chrome() # dist에 chromedriver를 비롯한 필요파일
    # driver.get("https://www.naver.com")
    f = open("test.txt", 'r')
    print(f.read())
    f.close()
except Exception as e:
    print(e)
print('test')

time.sleep(3)