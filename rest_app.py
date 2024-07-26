
from flask import Flask, request, jsonify
import db_connector

app = Flask(__name__)

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get(user_id):
    db_connector.readRecord(user_id)

if __name__ == '__main__':
    app.run()


# from flask import Flask, request, jsonify
# import db_connector

# # app = Flask(__name__)
#
# @app.route("/user/<user_id>", methods = ["Post", "GET", "PUT", "DELETE"])
# def httpMethod(user_id):
#     if request.method == "POST":
#         return addUser(user_id)
#     elif request.method == "GET":
#         return addUser(user_id)
#     elif request.method == "PUT":
#         return addUser(user_id)
#     elif request.method == "DELETE":
#         return addUser(user_id)


# def retrieveUser(user_id):
#     result = db_connector.readRecord(user_id)
#     return result[1]
# #   return "test123"
#
# def updateUser(user_id):
#     resultUpdated = db_connector
# def addUser(user_id):
#     userName = request.json.get('userName')
#
#     return jsonify('status' = "ok", "user_added" = userName),200



# def download_file():
#     file_path = '/Users/studylab/PycharmProjects/GlobalDevExperts/Wk3/index.html'


#
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
#     resultUpdated = db_connector
# def addUser(user_id):
#     userName = request.json.get('userName')
#
#     return jsonify('status' = "ok", "user_added" = userName), 200
#
#

# def download_file():
#     file_path = '/Users/studylab/PycharmProjects/GlobalDevExperts/Wk3/index.html'




    #
    # file = open(file_path, 'r')
    # contents = file.read()
    #
    # response = make_response(contents)
    # response.status_code = 200
    # return response

