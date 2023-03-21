# Tistory Crawler

**주의! 모든 법적인 책임은 크롤링을 하는 본인에게 있습니다.**
**위 코드는 학습용으로 개발 되었습니다.**

### Introduction

`Tistory Crawler`은 대량의 티스토리 포스팅을 수집하는 라이브러리입니다. 간단하게 한국어 뉴스 데이터셋을 구성하도록 도와줍니다. Chrome Driver와 Selenium을 통해 간단하게 사용할 수 있습니다.


### Setup
* Chrome Driver 설치하기
    - [`Chrome Driver`](https://chromedriver.chromium.org/downloads)중 사용자 OS와 맞는 드라이버를 다운받아 최상단 폴더에 넣습니다.
    - `main.py`의 driver PATH를 driver가 저장된 절대경로로 바꿔줍니다. 

* (Optional) Database 연결하기
    - 위 프로젝트는 Postgresql에 데이터를 저장하는 형태로 개발되었습니다. `Secrets.py`파일을 만들어서 `SECRET_HOST`, `SECRET_DBNAME`, `SECRET_USER`, `SECRET_PASSWORD`, `SECRET_PORT` 변수를 채워줍니다.

### Crawl Blog Path
[티스토리 메인 스토리탭](https://www.tistory.com/category/) 에서 5가지 탭의 블로그 HOST명을 크롤링해서 데이터베이스에 저장합니다. 2023-03-21 기준 한 탭에 6100개의 추천 글이 있었습니다.

 티스토리 추천은 무한스크롤과 유사하게 구현되어 있기 때문에 한줄씩 내리면서 url을 파싱하는 방식으로 구현되어 있습니다. 따라서 윈도우 사이즈를 변경하면 안됩니다. [`tistory_recommendation`](https://github.com/jonyejin/Tistory-Crawler/blob/d7636f62efbae33bfc65253cb82fd01ac8ab5306/AdressCollecting.py#L20) 함수를 참고하세요.


### Crawl Blog Body
**수집한 Blog포스팅의 PATH가 숫자로만 이루어진 포스팅인 경우, 1번 포스팅부터 수집된 PATH까지 반복문을 통해서 크롤링 합니다. HTML Body를 Database에 저장합니다.

### Dependencies
* beautifulsoup4
* urllib3
* selenium
* psycopg2