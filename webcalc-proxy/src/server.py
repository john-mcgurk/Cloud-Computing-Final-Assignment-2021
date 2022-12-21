from flask import Flask
from flask import Response
from flask import request
from flask import jsonify

import requests
#from flask import jsonify

app = Flask(__name__)

@app.route('/')
def proxyHandler():
    x = request.args.get('x', type=int)
    y = request.args.get('y', type=int)
    op = request.args.get('op')
    print('Docker op: ' + op)
    ops = ['add','subtract','multiply','divide','modulo','square','save','load']

    # Error handling
    if op not in ops or x == None or y == None:
        r = jsonify({'error':'true','message':'invalid parameters'})
        r.headers["Content-Type"] = "application/json"
        r.headers["Access-Control-Allow-Origin"] = "*"
        return r

    # Cast back to string after checking if valid integer
    x = str(x)
    y = str(y)

    if op == 'save':
        resp = requests.post("http://db.40208063.qpc.hal.davecutting.uk/insert/?val="+x)
    elif op == 'load':
        resp = requests.get("http://db.40208063.qpc.hal.davecutting.uk/val/?id="+x)
    else:
        resp = requests.get("http://"+op+".40208063.qpc.hal.davecutting.uk/?x="+x+"&y="+y)

    #If primary server is down, use backup
    if resp.status_code != 200:
        print("Primary server down... Trying to connect to backup")
        if op == 'save':
            resp = requests.post("http://backup.db.40208063.qpc.hal.davecutting.uk/insert/?val="+x)
        elif op == 'load':
            resp = requests.get("http://backup.db.40208063.qpc.hal.davecutting.uk/val/?id="+x)
        else:
            resp = requests.get("http://backup."+op+".40208063.qpc.hal.davecutting.uk/?x="+x+"&y="+y)

        #If backup server is down, return error
        if resp.status_code != 200:
            print("Backup server down... Returning error")
            r = jsonify({'error':'true','message':'servers are down for ' + op})
        else:
            jsonResp = resp.json()
            r = jsonify(jsonResp)
    else:
        jsonResp = resp.json()
        r = jsonify(jsonResp)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
