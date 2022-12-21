from random import randint

import requests

#@app.route('/')
#

performance_monitor = {
    "add" : [[0,1,0],[0,1,0],[0,1,0]],
    "subtract" : [[0,1,0],[0,1,0],[0,1,0]],
    "multiply" : [[0,1,0],[0,1,0],[0,1,0]],
    "divide" : [[0,1,0],[0,1,0],[0,1,0]],
    "square" : [[0,1,0],[0,1,0],[0,1,0]],
    "modulo" : [[0,1,0],[0,1,0],[0,1,0]],
    "backup-add" : [[0,1,0],[0,1,0],[0,1,0]],
    "backup-subtract" :[[0,1,0],[0,1,0],[0,1,0]],
    "backup-multiply" : [[0,1,0],[0,1,0],[0,1,0]],
    "backup-divide" : [[0,1,0],[0,1,0],[0,1,0]],
    "backup-square" : [[0,1,0],[0,1,0],[0,1,0]],
    "backup-modulo" : [[0,1,0],[0,1,0],[0,1,0]]
}

def testServer(URL, name):
    resp =requests.get(URL)

    #Monitoring average response time, how many times executed, and last response time.
    response_time = resp.elapsed.total_seconds()
    vals = performance_monitor.get(name)[0]
    vals[0] = ((vals[0]*vals[1]) + response_time) / vals[1]
    vals[1] += 1
    vals[2] = response_time

    if resp.status_code != 200:
        r = "Bad response from server"
    else:
        r = "Server active"
    return r

def testServerLogic(URL, name):
    #Maybe do this 3 times???
    r=""
    for i in range(3):
        x = randint(0,50)
        y = randint(1,10)
        if "square" in name:
            x = randint(0,10)
            y = randint(0,8)

        r = ""
        ops = {'add':'+','subtract':'-','multiply':'*','divide':'//','modulo':'%','square':'**'}
        for op in ops.keys():
            if op in URL:
                opd = ops.get(op)
                ans = eval(str(x)+ops.get(op)+str(y))

        #Monitoring average response time, num executions and last response time.
        print("Evaluating with.... " +str(x)+ opd+str(y))
        resp =requests.get(URL+"/?x="+str(x)+"&y="+str(y))
        response_time = resp.elapsed.total_seconds()
        vals = performance_monitor.get(name)[1]
        vals[0] = ((vals[0]*vals[1]) + response_time) / vals[1]
        vals[1] += 1
        vals[2] = response_time

        if resp.status_code != 200:
            print(opd)
            if opd == '**':
                r = "Overloaded integer value"
            r = "Server down"
        else:
            resp = resp.json()
            print("Expected: " + str(ans) + " -- Received: " + str(resp['answer']))
            if int(resp['answer']) == ans:
                r = "Logic correct"
    return r

def testServiceErrorHandling(URL, name):
    x = str(randint(0,100))
    tests = [
        "/?x=&y="+x,
        "/?x="+x+"&y=",
        "/?x=test&y="+x,
        "/?x="+x+"&y=test",
        "/?x=&y=test",
        "/?x=test&y=",
        "/?x="+x,
        "/?y="+x
    ]
    # Run series of tests on given URL
    for query in tests:

        resp =requests.get(URL+query)
        response_time = resp.elapsed.total_seconds()
        vals = performance_monitor.get(name)[2]
        vals[0] = ((vals[0]*vals[1]) + response_time) / vals[1]
        vals[1] += 1
        vals[2] = response_time

        if resp.status_code != 200:
            r = "Server down"
            return r
        else:
            resp = resp.json()
            if str(resp['error']).lower() == 'true':
                print("Error caught in URL: " + query)
            else:
                return "Error handling failed, bad request passed @"+URL+query

    return "All error handling tests passed"

def getPerformance():
    performance_report = {}
    for key in performance_monitor.keys():
        performance_report[key] = {
            "Average Basic Response Time" : performance_monitor.get(key)[0][0],
            "Previous Basic Response Time" : performance_monitor.get(key)[0][2],
            "Average Computation Response Time": performance_monitor.get(key)[1][0],
            "Previous Computation Response Time": performance_monitor.get(key)[1][2],
            "Average Error Handling Response Time": performance_monitor.get(key)[2][0],
            "Previous Error Handling Response Time": performance_monitor.get(key)[2][2]
        }
    return performance_report

if __name__ == '__main__':
    getPerformance()
