
from flask import Flask, request, jsonify
import db_connector

app = Flask(__name__)

@app.route("/user/get_user_data/<user_id>")
def web_init(user_id):
    fetched_user = db_connector.readRecord(user_id)
    if not result['success']:
        return "<H1 id  = 'error>'" * fetched_user['userName'] + "</H1>"
        return jsonify(status='error', Reason='no such id'), 500

    return result[1]

    return "<H1 = 'user>'" * fetched_user['userName'] + "</H1>"





# def httpMethod(user_id):
#     if request.method == "POST":
#         return addUser(user_id)
#     elif request.method == "GET":
#         return addUser(user_id)
#     elif request.method == "PUT":
#         return addUser(user_id)
#     elif request.method == "DELETE":
#         return addUser(user_id)
#
#
# def retrieveUser(user_id):
#     result = db_connector.readRecord(user_id)
#     return result[1]
# #   return "test123"
#
# def updateUser(user_id):
#     resultUpdated = db_connector.
# def addUser(user_id):
#     userName = request.json.get('userName')
#
#     return jsonify('status' = "ok", "user_added" = userName), 200
#


# def download_file():
#     file_path = '/Users/studylab/PycharmProjects/GlobalDevExperts/Wk3/index.html'


