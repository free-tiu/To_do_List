from flask import Flask,request, render_template,redirect, jsonify

from models import todo
# 跨域请求
from flask_cors import CORS

app = Flask(__name__)
# 解决跨域问题
CORS(app, supports_credentials=True)


@app.route('/todo', methods=['GET', 'POST'])
def todo_view():
    # 判断请求
    if request.method == 'GET':
        return jsonify(todo.todo_list)
    # 判断请求
    if request.method == 'POST':
        title = request.json.get('title', None)
        item = {
            'id': todo.count,
            'title': title,
            'done': False
        }
        todo.todo_list.append(item)
        return {'status': 'ok'}


@app.route('/todo/<int:_id>', methods=['PUT', 'DELETE'])
def todo_item(_id):
    # 判断请求
    if request.method == 'PUT':
        for item in todo.todo_list:
            if item['id'] == _id:
                item['done'] = not item['done']
                return {'status': 'ok'}
        return {'status': 'error'}

    # 判断请求
    if request.method == 'DELETE':
        for item in todo.todo_list:
            if item['id'] == _id:
                todo.todo_list.remove(item)
                return {'status': 'ok'}
        return {'status': 'error'}


if __name__ == '__main__':

    print(app.url_map)

    app.run(host='0.0.0.0', port=5000, debug=True)
