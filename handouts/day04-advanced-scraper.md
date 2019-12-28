---
marp: true
---

# Fastcampus Sprint - Programming

## Day 4. Advanced Web Scraping

---
<!--
paginate: true
theme: default
size: 16:9
footer : fastcampus Sprint Programming, Wooyoung Choi, 2019
-->

## Index

- Advanced Web Scraping with Selenium
- Web Scraping with cloud service

---

## Requirements

- `$ pip install selenium`
- ChromeDriver: https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.11/

---

## requests && BeautifulSoup

- 정적인 페이지를 수집할 때
- requests: HTTP 요청 -> HTML 응답
- BeautifulSoup: HTML 응답 -> 분석 후 요소 접근

---

## But..

- BeautifulSoup은 AJAX나 javaScript로 그려지는(렌더링) 요소나 행동은 접근할 수 없음

---

## Selenium!

- Web Application User test tool
- `$ pip install selenium`
- with webdriver

---

## Pros & Cons

### Pros

- 동적 페이지 제어 가능
- 사용자처럼 행동 가능
- iframe 제어 가능

### Cons

- 느림
- BS4에 비해 신경써야 할 것이 많음

---

## Route is important while using Selenium

- BeautifulSoup : 수집할 요소 선택 -> url 정보 수집 -> 스크래핑 수행
- Selenium: 수집할 요소 선택 -> 요소까지의 경로 선정 -> 스크래핑 수행

---

## Web Scraping with Selenium

```python
from selenium import webdriver
ch_driver = webdriver.Chrome(<your webdriver path>)
ch_driver.get('https://www.google.com/')
```

---

## N사 포털 카페 서비스

> 특정 카페의 검색 결과물을 가져와봅시다.

---

## Key script

```python
query_input = ch_driver.find_element_by_id("<id of element>")
query_input.send_keys(<query>)
ch_driver.execute_script(<javascript>)
ch_driver.switch_to_frame(<element>)
```

---

## Twitter

> 더 많은 데이터 로딩을 위해 스크롤 후 데이터를 가져와봅시다.

```python
ch_driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
```

---

## Google Cloud

---

## Cloud?

- 인터넷에 연결된 다른 컴퓨터로 연산을 하는 기술
- 접근성, 주문형 서비스 제공으로 경제적이고 효율적인 컴퓨팅 서비스 제공
- Amazon Web Service(Amazon), Google Cloud Platform(Google), Microsoft Azure(Microsoft), ..
- Virtual Machine, Cloud Storage, Database, Docker Engine 등 다양한 서비스 제공

---

## Google Cloud Flatform

- 2011년 Google이 출시한 클라우드 컴퓨팅 솔루션서비스
- 20개의 region과 61개의 zone 서비스 중
- 2020년 서울 region 오픈예정
- https://cloud.google.com/

---

## Google Cloud Functions

- Pricing: https://cloud.google.com/functions/pricing

---

## Google Cloud Functions

![height:400px](./img/gcp01.png)

---

## Google Cloud Functions

![height:400px](./img/gcp02.png)

---

## Google Cloud Functions

![height:400px](./img/gcp03.png)

---

## Google Cloud Functions

![height:400px](./img/gcp04.png)

---

## Google Cloud Functions

![height:400px](./img/gcp05.png)

---

## Google Cloud Functions

![height:400px](./img/gcp06.png)

---

## Nv_query with gcloud

```python
import requests
import lxml
from bs4 import BeautifulSoup
from time import ctime
import json


def get_nv_query(request):
    base_uri = "https://www.naver.com/"
    exec_time = ctime()
    response = requests.get(base_uri)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    ul_tag = soup.find("ul", attrs={"class":"ah_l"})
    querys = []
    for li in ul_tag.find_all("li"):
        query = li.find("span", attrs={"class":"ah_k"}).text
        querys.append(query)
    result = {
        "time": exec_time,
        "items": querys,
    }
    print(result)
    return json.dumps(result, ensure_ascii=False)
```

---

## Google Cloud Functions

![height:400px](./img/gcp07.png)

---

## Google Cloud Functions

![height:400px](./img/gcp08.png)

---

## Google Cloud Functions

![height:400px](./img/gcp09.png)

---

## Store data with Mongodb atlas

- https://www.mongodb.com/cloud/atlas

---

```python
import requests
import lxml
from bs4 import BeautifulSoup
from time import ctime
#import json
from pymongo import MongoClient


def get_nv_query(event, context):
    # ...
    result = {
        "time": exec_time,
        "items": querys,
    }
    # ...
    # insert into mlab
    mongo_uri = "mongodb://betteradmin:1q2w3e4r@ds255403.mlab.com:55403/allquerys?retryWrites=false"
    try:
        client = MongoClient(mongo_uri)
        db = client.allquerys
        db_nvquerys = db.nvquerys
        db_nvquerys.insert_one(result)
    except:
        return "failed on {}".format(exec_time)
    return "success on {}".format(exec_time)
```

---

## Google Cloud Functions

![height:400px](./img/gcp10.png)

---

## Turn into pubsub and schedule function

---

## Google Cloud Functions

![height:400px](./img/gcp11.png)

---

## Google Cloud Functions

![height:400px](./img/gcp12.png)

---

## Google Cloud Functions

![height:400px](./img/gcp13.png)

---

## Google Cloud Functions

![height:400px](./img/gcp14.png)

---

## Google Cloud Functions

![height:400px](./img/gcp15.png)


<link href="https://fonts.googleapis.com/css?family=Nanum+Gothic:400,800" rel="stylesheet">
<link rel='stylesheet' href='//cdn.jsdelivr.net/npm/hack-font@3.3.0/build/web/hack-subset.css'>

<style>
h1,h2,h3,h4,h5,h6,
p,li, dd, table > * > * {
font-family: 'Nanum Gothic', Gothic;
}
span, pre {
font-family: Hack, monospace;
}
</style>