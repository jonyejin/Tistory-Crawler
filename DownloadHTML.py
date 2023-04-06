from selenium import webdriver
from Database import Databases
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
from urllib.parse import urlparse
from selenium.webdriver import ActionChains
from typing import *
from urllib.parse import urljoin, urlencode, urlparse, urlunparse
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, TimeoutException

class DownloadHTML():
    def __init__(self, driver):
        self.driver = driver

    # 주어진 url에 대해서 iteration을 만들어준다.
    def getSingleTistoryDownloadList(self, url: str, count: int) -> List[str]:
        urls = []
        for num in range(1, count+1):
            urls.append(urlparse(url).hostname  + f"/{num}")
        return urls

    def downloadHTML(self, driver, hostname, url):
        print(">>")
        # check driver status
        time.sleep(3) 
        try:
            driver.get(url)
        except TimeoutException as e:
            print("TIMEOUT")
            print(e)
            return

        print(">>")

        # 에러 페이지인지 확인 - $x("//*[@id="mArticle"]/div")
        b = None
        try:
            b = driver.find_element(By.XPATH, "//h2[text()='에러 메세지']")
            if b is not None:
                return None
        except NoSuchElementException or NoSuchAttributeException:
            if b is None:
                return (hostname, url, driver.page_source)
            else:
                return None
        except Exception as e:
            print(e)


    def saveToDatabase(self, db: Databases, hostname, url, body):
        db.insertTistoryBlogBody(hostname, url, body)
        return