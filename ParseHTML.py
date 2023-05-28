from selenium import webdriver
from selenium.webdriver.common.by import By

from Database import Databases
from DownloadHTML import DownloadHTML
from AdressCollecting import *
import urllib.request as req
from utils import korean_character_ratio

# 저장된 html파일에서 제목, 작성자, 내용, 댓글, 좋아요 수, 태그를 분리해 낼 수 있지만
# 일단은 제목/작성자/내용만 분리한다. 
def parseBody(body):
    class NoTagsException(BaseException):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    from bs4 import BeautifulSoup
    title = ""
    result = []

    soup = BeautifulSoup(body, 'html.parser')
    title = soup.title.string
    try:
        # TODO: 지금 받아온애가 descentandts가 nil임.
        big_body = soup.find('div', "tt_article_useless_p_margin") # Tag
        print(big_body == None)
        # print(big_body)
        try:
            tags = big_body.find_all('p') # attrs={'data-ke-size': 'size16'})
        except Exception as e:
            raise NoTagsException
        for tag in tags:
            # if tag['class'] == 'another_category another_category_color_gray': # 카테고리쪽이라 pass
            #     continue

            if tag.string != None:
                stripped = tag.string.replace("\xa0", "").strip()
                # print(stripped)
                if len(stripped) == 0:
                    continue
                # if korean_character_ratio(stripped, ignore_whitespace=True) < 0.5 :
                #     print("한글 컨텐츠가 아님")
                #     continue
                if stripped == '타이틀 시작' or stripped == '타이틀 종료' or stripped == '소제목1 종료' or stripped == '소제목1 시작' or stripped == '소제목2 시작' or stripped == '소제목2 종료' or stripped == '마무리 시작' or stripped == '마무리 종료':
                    continue
                if stripped is not None:
                    result.append(stripped)
    except NoTagsException:
        content = soup.get_text(strip=True)
        return (title, content, True)
    except Exception as e:
        print(e)
        return

    return (title, "\n".join(result), False)

db = Databases()
value = 0
limit = 100

while True:
    try:
        htmls = db.selectTistoryBlogBody(offset=value, limit=limit) # List 
        if htmls == []:
            print("Query결과 htmls 비어있다.")
            break

        for html in htmls:
            raw_html = html[0] # str
            url = html[1]
            print("=======")
            print(url)
            title, body, isParsedByMachine = parseBody(raw_html)
            if body is not None:
                db.updatistoryBlogCleanedBody(url, title, body, isParsedByMachine)
            else:
                print(f"비었다: {url}")
        value += limit
    except Exception as e:
        print(e)
print("==done==")