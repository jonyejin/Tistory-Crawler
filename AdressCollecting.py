import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium
from urllib.parse import urlparse
from selenium.webdriver import ActionChains

tistory_category = ['life', 'travel', 'culture', 'it', 'sports', 'current'] # 라이프, 여행-맛집, 문화-연예, IT, 스포츠, 시사, 이벤트

def _check_exists_by_element(driver, by, name):
    try:
        driver.find_element(by, name)
    except NoSuchElementException:
        return False
    return True


# 티스토리 추천에서 찾기
def tistory_recommendation(driver, database, callback_function):
    # 티스토리 추천은 무한스크롤로 구현되어 있기 때문에 
    # 한줄씩 내리면서 url을 파싱하는 방식으로 구현함
    # 총 6100개임 

    for type in tistory_category:
        url = f"https://www.tistory.com/category/{type}"
        driver.get(url)

        time.sleep(2)
        #시작점으로 스크롤 이동 542+284 = 806
        driver.execute_script("window.scrollTo(0, 284+40+442+60)")
        # 기다리기
        time.sleep(2)

        #로고의 좌표 추출
        standard_logo = driver.find_element(By.XPATH, ".//a[@id='kakaoServiceLogo']/span[2]")
            
        while True:
            # 로고로 가기
            act = ActionChains(driver)
            act.move_to_element(standard_logo)

            # 기다리기
            time.sleep(0.3) 

            # 기존 위치
            scroll_location = driver.execute_script("return document.body.scrollHeight")

            
            #상대좌표를 통한 대상 변경 반복문
            for line in range(0, 4):  # 보이는 포스팅 4개
                y = 36 + 16 + 192 * line  #열 번호를 기준으로 192씩 y좌표를 더함, 36: 로고에서 이동할 높이만큼 계산, 16: 패딩

                #로고 좌표에 상대좌표를 더해 피드 마우스 오버
                act.move_to_element(standard_logo).move_by_offset(492, y).context_click().perform() # 필요시 context_click()으로 디버깅
                time.sleep(0.3)

                elem = driver.switch_to.active_element
                print("=====")
                print(elem.get_attribute('href'))               

                try: 
                    link = elem.get_attribute('href')
                    h = urlparse(link).hostname 
                    print(h)
                    # with open("links.csv", "a") as f:  
                    #     f.write(f"{h}\n")
                    #     f.close()
                    callback_function(h, link)

                except Exception as e:
                    print(e)

            # 페이지 다운
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)

            # 페이지 다운 하고도 높이 같은지 확인
            scroll_height = driver.execute_script("return document.body.scrollHeight")

            # 늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
            if scroll_location == scroll_height:
                break


# path가 숫자로만 이루어져 있다면 true를 리턴하고 int값을 리턴한다.
def checkTistoryLink(url: str):
    if urlparse(url).path[1:].isnumeric():
        return (True, int(urlparse(url).path[1:]))
    else:
        return (False, 0)