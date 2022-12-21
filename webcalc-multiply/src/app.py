from flask import Flask
from flask import Response
from flask import request
from flask import jsonify

import multiplynum

app = Flask(__name__)

@app.route('/')
def multiplynumber():
    reply = {}
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        z = multiplynum.multiply(x,y)

        reply = {
            "answer":str(z),
            "string":str(x) + "*" + str(y) + "=" + str(z),
            "error":"false"
        }
    except:
        reply["error"] = "true"
        reply["string"] = "Error - Invalid parameters"
        reply["answer"] = "Undefined"

    r = jsonify(reply)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
