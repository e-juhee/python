from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@3.39.234.202', 27017)
db = client.jungle


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def create_memo():
    sort_by_index = list(db.memo.find({}, {"_id": False}).sort('index', -1))
    new_index = 0
    if len(sort_by_index) > 0:
        new_index = sort_by_index[0]['index'] + 1
    text_receive = request.form['text_give']
    title_receive = request.form['title_give']
    memo = {
        'index': new_index,
        'title': title_receive, 'text': text_receive}
    db.memo.insert_one(memo)
    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def show_memos():
    result = list(db.memo.find({}, {"_id": False}))
    return jsonify({'result': 'success', 'memos': result})


@app.route('/memo/modify', methods=['POST'])
def modify_memo():
    index_receive = request.form['index_give']
    title_receive = request.form['title_give']
    text_receive = request.form['text_give']
    db.memo.update_one({'index': int(index_receive)}, {
                       '$set': {'title': title_receive, 'text': text_receive}})
    return jsonify({'result': 'success'})


@app.route('/memo/delete', methods=['POST'])
def delete_memo():
    index_receive = request.form['index_give']
    db.memo.delete_one({'index': int(index_receive)})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
