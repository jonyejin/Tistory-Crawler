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
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.support.ui import WebDriverWait

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
        try:
            driver.implicitly_wait(5)
            driver.get(url)
        except TimeoutException as e:
            print("TIMEOUT") # TEST: https://httpstat.us/200?sleep=50000
            print(e)
            raise TimeoutException
        except InvalidSessionIdException as e:
            print(e)
            print("이게 매일 멈추는 원인인 것 같음")
            raise InvalidSessionIdException
        except Exception as e:
            print(e)
            print("이게 매일 멈추는 원인인 것 같음")
            raise TimeoutException


        print(">>")

        # 에러 페이지인지 확인 - $x("//*[@id="mArticle"]/div")
        b = None
        try:
            b = driver.find_element(By.XPATH, "//h2[text()='에러 메세지']")
            if b is not None:
                return (None, None, None)
        except NoSuchElementException or NoSuchAttributeException:
            if b is None:
                return (hostname, url, driver.page_source)
            else:
                return (None, None, None)
        except Exception as e:
            print(e)
            return (None, None, None)


    def saveToDatabase(self, db: Databases, hostname, url, body):
        db.insertTistoryBlogBody(hostname, url, body)
        return