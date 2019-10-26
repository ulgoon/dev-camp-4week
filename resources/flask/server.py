from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import lxml
import json


# Flask 시작
app = Flask(__name__)

# 사용자의 접근 경로 별 처리
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "I am what I am."

@app.route('/nvquery')
def get_query():
    # TODO
    # requests, bs4를 이용하여 N사 실시간 검색어
    # 가져오는 거 까지만 하세요.
    # result = [(1,"검색어"), (2,"검색어")]
    response = requests.get("https://www.naver.com/")
    html_text = response.text
    soup = BeautifulSoup(html_text, "lxml")
    ul_text = soup.find("ul", attrs={"class":"ah_l"})
    li_list = ul_text.find_all("li")
    result = []
    for li in li_list:
        rank = int(li.find("span", attrs={"class":"ah_r"}).text)
        keyword = li.find("span", attrs={"class":"ah_k"}).text
        result.append((rank, keyword))
    return json.dumps(dict(result), ensure_ascii=False)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
