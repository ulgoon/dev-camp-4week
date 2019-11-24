from flask import Flask, render_template
import requests
import lxml
from bs4 import BeautifulSoup
import json
from time import ctime

# flask를 시작합니다.
app = Flask(__name__)

# 메인페이지의 라우팅을 위한 함수와 데코레이터
@app.route('/')
def index():
    return render_template('index.html', msg="greet")

# D포털의 실시간 검색어를 가져오는 /daum
@app.route('/daum')
def get_du_querys():
    response = requests.get('https://www.daum.net/')
    exec_time = ctime()
    html_text = response.text

    soup = BeautifulSoup(html_text, 'lxml')
    ol_tag = soup.find('ol', attrs={'class':'list_hotissue'})
    div_list = ol_tag.find_all('div', attrs={'class':'rank_cont'})
    keywords={'time': exec_time}
    for div in div_list:
        rank = int(div.find('span', attrs={'class':'ir_wa'}).text.replace('위','').replace('}',''))
        keyword = div.find('a', attrs={'class':'link_issue'}).text
        keywords[rank] = keyword
    return json.dumps(keywords, ensure_ascii=False)

# N포털의 실시간 검색어를 가져오는 /naver
@app.route('/naver')
def get_nv_querys():
    # requests로 요청하여 html text를 가져옵니다.
    response = requests.get('https://www.naver.com/')
    # 실행당시의 시간을 기록합니다
    exec_time = ctime()
    html_text = response.text
    
    # BeautifulSoup으로 분석 시작
    soup = BeautifulSoup(html_text, 'lxml')
    # 검색어 묶음 단위를 찾은 뒤, 검색어 순위별로 리스트로 가져옴
    ul_tag = soup.find('ul', attrs={'class':'ah_l'})
    li_list = ul_tag.find_all('li')
    # 각 검색어에 대해 순위와 검색어를 찾아 keywords에 저장
    keywords = {'time': exec_time}
    for li in li_list:
        rank = int(li.find('span', attrs={'class':'ah_r'}).text)
        keyword = li.find('span', attrs={'class':'ah_k'}).text
        keywords[rank] = keyword
    # 이 함수의 실행 결과를 json 형식으로 전달(한글 유니코드 문제 해결을 위한 ascii->False)
    return json.dumps(keywords, ensure_ascii=False)
    
# 메인함수(프로그램의 실행이 쉘 단위에서 실행될 경우)에만 flask 서버를 시작
# 127.0.0.1:8080 로 연결, 확인 가능
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)