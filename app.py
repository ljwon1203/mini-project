from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.obco8e7.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

'''
페이지 템플릿 렌더링 기능
'''
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/members", methods=["GET"])
def members():
    parameter_dict = request.args.to_dict()
    name = parameter_dict['name']
    return render_template(f'members/{name}.html')

'''
API 목록
'''
# 1. comments GET
@app.route("/comments", methods=["GET"])
def get_comments():
    comment_list = list(db.comments.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

# 2. comment POST
@app.route("/comments", methods=["POST"])
def post_comments():
    name_receive = request.form['name_give']
    comment_receive = request.form["comment_give"]
    # 멤버추가
    # member_receive = request.form["member_receive"]


    doc = {
        'name': name_receive,
        'comment': comment_receive,
        # 멤버추가
        # 'member': member_receive
    }

    db.comments.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

# 3. comments DELETE
@app.route("/comments/delete", methods=["POST"])
def delete_comments():
    name_receive = request.form['name_give']
    db.comments.delete_one({"name": name_receive})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)