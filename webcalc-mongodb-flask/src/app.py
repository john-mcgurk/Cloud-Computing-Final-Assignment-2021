from flask import Flask, jsonify, request
import ssl
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient('10.42.10.86:27017')
db = client.test
# Database
Database = client.get_database('webcalc')
# Table
numbers = Database.numbers

@app.route('/')
def home():
    return "Landing screen for mongodb-flask api"



# Insert method
@app.route('/insert/', methods=['POST'])
def insert():
    val = request.args.get('val')
    if val.lower() == 'undefined':
        resp = {'error':"True: Cannot store undefined value"}
    else:
        id = str(numbers.find({}).count() + 1)
        queryObject = {'id': id,'val': val }
        query = numbers.insert_one(queryObject)
        test_query = numbers.find_one({'id':id})
        resp = {'error':"False", 'answer':test_query['id']}
    r = jsonify(resp)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

# Find a value from given id
@app.route('/val/', methods=['GET'])
def findOne():
    id = request.args.get('id')
    queryObject = {'id': id}
    query = numbers.find_one(queryObject)
    if query:
        resp = {'error':"False", 'answer':query['val']}
    else:
        resp = {'error':'True'}
    r = jsonify(resp)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
