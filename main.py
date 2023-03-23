from selenium import webdriver
from selenium.webdriver.common.by import By

from Database import Databases
from DownloadHTML import DownloadHTML
from AdressCollecting import *
import urllib.request as req
import re
import time
import os
import ssl

# 인증서 문제 해결
ssl._create_default_https_context = ssl._create_unverified_context

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--no-sandbox')
options.add_argument("disable-gpu")
options.add_argument('window-size=1920x1080')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome(r'/home/dilab/Documents/GitHub/Tistory-Crawler/chromedriver', options = options)
driver.set_window_position(0, 0)
# driver.maximize_window()
driver.set_window_size("1879", "2427")
driver.set_page_load_timeout(10)

# Database
db = Databases()
downloader = DownloadHTML(driver)

# db.selectTistoryLink(0, 1)


# Tistory 주소 수집용
# print(tistory_recommendation(driver=driver, database=db, callback_function=db.insertTistoryBlogLink))


# tistory 본문 수집용
# url이 저장되어 있을 때 중복되지 않게 불러와서 tistory url리스트를 만들고 
# 각각에 대해서 download하고 다시 db에 저장해준다.

value = 137
limit = 100
try:
    while True:
        print(value, limit)        
        urls = db.selectTistoryLink(offset=value, limit=limit) # List 
        print(urls)

        # 원래는 개수를 비교해야 하지만...
        if urls == []:
            print("Query결과 URL이 비어있다.")
            break

        for url_packed in urls:
            u = url_packed[0] # str
            isNumberAddress = checkTistoryLink(u)[0]
            countForBlog = checkTistoryLink(u)[1]
            if isNumberAddress:
                hostname = urlparse(u).hostname
                urls_for_each_blog = downloader.getSingleTistoryDownloadList(u, countForBlog)
                for posting in urls_for_each_blog:
                    print(posting)
                    try:
                        _, _, body = downloader.downloadHTML(driver, hostname, "https://" + posting)
                        downloader.saveToDatabase(db, hostname, posting, body)
                    except Exception as e:
                        # print(e)
                        print("없는 포스팅")
                        print("======")
            else:
                print("path가 숫자가 아님")
        value += limit
except Exception as e:
    print('여기에요 여기')
    # print(e)