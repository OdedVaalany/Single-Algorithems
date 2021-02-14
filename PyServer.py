import pymongo
import flask
import DataConfig

from bson.json_util import dumps
from flask import Flask, request
from pymongo import MongoClient

# define a connection into the database with mongodb platform
URI = f'mongodb+srv://Avoded2:{DataConfig.password}@cluster0.vwucm.mongodb.net/{DataConfig.defultDB}?retryWrites=true&w=majority'
client = MongoClient(URI, tls=True)
db = client[DataConfig.defultDB]
users = db[DataConfig.collection]
print(f"Connect to {DataConfig.collection}")

# define the server
app = Flask(__name__)


@app.route('/users/', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        print(request.args.to_dict())
        data = users.find(request.args.to_dict())
        return dumps(data)
    else:
        res = request.json
        email = res['Email']
        password = res['Password']
        users.insert_one(res)
        data = users.find_one({"Email": email, "Password": password})
        return dumps(data)


@app.route('/users/delete-all/<password>', methods=['DELETE'])
def delete_all(password):
    if password == "Vaalany_Oded":
        data = users.find({})
        for n in data:
            users.delete_one({"_id": n["_id"]})
        return "good"
    else:
        return "invaild password"


@app.route('/users/delete/<id>', methods=['DELETE'])
def delete(id):
    try:
        users.delete_one({"_id": id})
        return "deleted"
    except:
        return "not existing user"


# run the server
if __name__ == "__main__":
    app.run()
