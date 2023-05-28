
from bs4 import BeautifulSoup
import requests
from utils import korean_character_ratio

# body = open('44.html')
title = ""
result = []

url = 'https://sports.news.naver.com/kbaseball/news/index?isphoto=N&page=10'
body = requests.get(url).text
print(body)
with open("links.html", "a") as f:  
        f.write(body)
        f.close()
soup = BeautifulSoup(requests.get(url), 'html.parser')
title = soup.title.string
# TODO: 지금 받아온애가 descentandts가 nil임.
big_body = soup.find('div', "tt_article_useless_p_margin") # Tag
tags = big_body.find_all('p', attrs={'data-ke-size': 'size16'})
for tag in tags:
    # if tag['class'] == 'another_category another_category_color_gray': # 카테고리쪽이라 pass
    #     continue

    if tag.string != None:
        stripped = tag.string.replace("\xa0", "").strip()
        # print(stripped)
        if len(stripped) == 0:
            continue
        if korean_character_ratio(stripped, ignore_whitespace=True) < 0.5 :
            # print("한글 컨텐츠가 아님")
            continue
        if stripped == '타이틀 시작' or stripped == '타이틀 종료' or stripped == '소제목1 종료' or stripped == '소제목1 시작' or stripped == '소제목2 시작' or stripped == '소제목2 종료' or stripped == '마무리 시작' or stripped == '마무리 종료':
            continue
        if stripped is not None:
            result.append(stripped)