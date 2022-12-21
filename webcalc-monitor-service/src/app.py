import monitor_functions
from flask import Flask
from flask import Response
from flask import request
from flask import jsonify
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jmcgurk99@gmail.com'
app.config['MAIL_PASSWORD'] = 'tyrone13'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

serviceUrls = {
    "add" : "http://add.40208063.qpc.hal.davecutting.uk",
    "subtract" : "http://subtract.40208063.qpc.hal.davecutting.uk",
    "multiply" : "http://multiply.40208063.qpc.hal.davecutting.uk",
    "divide" : "http://divide.40208063.qpc.hal.davecutting.uk",
    "square" : "http://square.40208063.qpc.hal.davecutting.uk",
    "modulo" : "http://modulo.40208063.qpc.hal.davecutting.uk",
    "backup-add" : "http://backup.add.40208063.qpc.hal.davecutting.uk",
    "backup-subtract" : "http://backup.subtract.40208063.qpc.hal.davecutting.uk",
    "backup-multiply" : "http://backup.multiply.40208063.qpc.hal.davecutting.uk",
    "backup-divide" : "http://backup.divide.40208063.qpc.hal.davecutting.uk",
    "backup-square" : "http://backup.square.40208063.qpc.hal.davecutting.uk",
    "backup-modulo" : "http://backup.modulo.40208063.qpc.hal.davecutting.uk",
}

monitor_response = {}

@app.route('/')
def landingScreen():
    return "Hello. Test active servers: /activeservers. Test server logic: /serverlogic. Test server error handling: /errorhandling"

@app.route('/activeservers')
def activeServers():
    for name in serviceUrls.keys():
        monitor_response[name] = monitor_functions.testServer(serviceUrls.get(name), name)
    r = jsonify(monitor_response)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

@app.route('/serverlogic')
def serverLogic():
    for name in serviceUrls.keys():
        monitor_response[name] = monitor_functions.testServerLogic(serviceUrls.get(name), name)
    r = jsonify(monitor_response)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

@app.route('/errorhandling')
def errorHandling():
    for name in serviceUrls.keys():
        monitor_response[name] = monitor_functions.testServiceErrorHandling(serviceUrls.get(name), name)
    r = jsonify(monitor_response)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

@app.route('/testWebServices')
def testWebServices():
    active_servers = activeServers().get_json()
    server_logic = serverLogic().get_json()
    error_handling = errorHandling().get_json()
    fullResponse = []
    for service in serviceUrls.keys():
        if active_servers.get(service) != "Server active":
            msg = Message('Server Down', sender = 'jmcgurk99@gmail.com', recipients = ['jmcgurk99@gmail.com'])
            msg.body = service + " Server Down. URL: " + serviceUrls.get(service)
            mail.send(msg)

        if server_logic.get(service) != "Logic correct":
            msg = Message('Logic Server Failure', sender = 'jmcgurk99@gmail.com', recipients = ['jmcgurk99@gmail.com'])
            msg.body = service + " Server has failed logic tests. Check server console for more info. URL: " + serviceUrls.get(service)
            mail.send(msg)

        if error_handling.get(service) != "All error handling tests passed":
            msg = Message('Error Handling Failure', sender = 'jmcgurk99@gmail.com', recipients = ['jmcgurk99@gmail.com'])
            msg.body = service + " has failed error handling testing. Check server console for more info. URL: " + serviceUrls.get(service)
            mail.send(msg)

        fullResponse.append({"name": service, "active" : active_servers.get(service),
            "functional": server_logic.get(service), "errors": error_handling.get(service)})
    r = jsonify(fullResponse)
    r.headers["Content-Type"] = "application/json"
    r.headers["Access-Control-Allow-Origin"] = "*"
    return r

#Email performance report every 24 hours.
@app.route('/report')
def emailReport():
    with app.app_context():
        msg = Message('Performance Report', sender = 'jmcgurk99@gmail.com', recipients = ['jmcgurk99@gmail.com'])
        msg.body = str(monitor_functions.getPerformance())
        mail.send(msg)
        return "Mailed to jmcgurk99@gmail.com"


test_sched = BackgroundScheduler(daemon=True)
test_sched.add_job(testWebServices,'interval', minutes=60)
test_sched.start()

performance_report_schedule = BackgroundScheduler(daemon=True)
performance_report_schedule.add_job(emailReport,'interval',minutes=1440)
performance_report_schedule.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
