from flask import Flask, render_template
#import requests
#from bs4 import BeautifulSoup

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
    return result

if __name__ == '__main__':
    app.run(port=8080, debug=True)
