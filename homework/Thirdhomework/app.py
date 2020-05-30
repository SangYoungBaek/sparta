from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/pays', methods=['POST'])
def write_pay():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    add_receive = request.form['add_give']
    pon_receive = request.form['pon_give']

    pay = {
        'name': name_receive,
        'number': number_receive,
        'add': add_receive,
        'pon': pon_receive
    }
    
    db.pays.insert_one(pay)
    return jsonify({'result':'success', 'msg': '주문이 완료되었습니다.'})


@app.route('/pays', methods=['GET'])
def read_pay():
    pays = list(db.pays.find({}, {'_id': 0}))
    return jsonify({'result':'success', 'pays': pays})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)