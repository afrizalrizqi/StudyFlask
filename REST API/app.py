#import library dan file
from flask import Flask, request, jsonify
from flask_cors import CORS
from crud_handler import create_user, get_all_user, get_user_by_id, edit_user, delete_user

#flask CORS
app = Flask(__name__)
CORS(app, resources={
    r"/*" : {"origins" : "*"}
})

#Route untuk melihat keseluruhan employee
@app.route('/user', methods=['GET'])
def api_get_all_users():
    dot=get_all_user()
    result = jsonify(get_all_user())
    return result

#Route untuk melihat salah satu employee
@app.route('/user/<user_id>', methods=['GET'])
def api_get_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))

#Route untuk menambahkan data employee baru
@app.route('/user/add', methods=['POST'])
def api_create_user():
    user = request.get_json()
    jsonify(create_user(user))
    return "Data berhasil ditambahkan!"

#Route untuk mengedit data employee baru
@app.route('/user/update', methods=['PUT'])
def api_edit_user():
    user = request.get_json()
    jsonify(update_user(user))
    return "Data berhasil diedit!"

#Route untuk menghapus data employee
@app.route('/user/delete/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    jsonify(delete_user(user))
    return "Dara berhasil dihapus!"

#Running apps
if __name__ == '__main__':
    app.run(debug=True)