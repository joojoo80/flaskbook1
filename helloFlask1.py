from flask import Flask, request


print(f'__name__ : {__name__}')

app = Flask(__name__)

@app.route('/')
# http://127.0.0.1:5000/
def index() :
    return '안녕1'


@app.route('/trans')
# Flask 웹 프레임워크에서 특정 URL 경로와 해당 경로로 요청이 들어왔을 때 실행될 함수를 연결(라우팅)하는 데 사용되는 데코레이터
# http://127.0.0.1:5000/trans
def trans() :
    return '<p> 교통현황 대시보드 </p>'


@app.route('/hello')
def hello() :
    name = request.args.get('name','christmas')
    # http://127.0.0.1:5000/hello >> 안녕 christmas 출력
    # http://127.0.0.1:5000/hello?name=kang  >> 안녕 kang 출력
    return f'<p> 안녕 {name} </p>'





