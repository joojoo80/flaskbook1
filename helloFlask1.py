from flask import Flask, request, render_template

print(f'__name__ : {__name__}')

app = Flask(__name__)

@app.route('/')
# http://127.0.0.1:5000/
def index() :
    return '안녕1'

# @app.route('/trans')
@app.get('/trans')
# Flask 웹 프레임워크에서 특정 URL 경로와 해당 경로로 요청이 들어왔을 때 실행될 함수를 연결(라우팅)하는 데 사용되는 데코레이터
# http://127.0.0.1:5000/trans
def transGet() :
    return '<p> 교통현황 대시보드 - get방식</p>'

@app.post('/trans')
def transPost() :
    return '<p> 교통현황 대시보드 - post방식 </p>'


@app.route('/hello')
def hello() :
    name = request.args.get('name','christmas')
    # http://127.0.0.1:5000/hello >> 안녕 christmas 출력
    # http://127.0.0.1:5000/hello?name=kang  >> 안녕 kang 출력
    return f'<p> 안녕 {name} </p>'


@app.route('/', endpoint='root')
def index1() :
    return '안녕1'


@app.route('/hello2/<height>')
def hello2(height) :
    height=int(height)
    sum = height + 7
    return f'<p> 안녕 {sum}</p>'

#@app.route 데코레이터의 Rule에 변수를 지정할 수 있다. 변수는 <변수명>


@app.route('/tomorrow/<menu>')
def tomorrow(menu) :
    return render_template('index.html',menu=menu)









