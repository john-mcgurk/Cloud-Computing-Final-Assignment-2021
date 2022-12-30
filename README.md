# Cloud Computing - _Final Assignment 2021_
_This repository contains my final submission for the Cloud Computing module in Queen's University Belfast. I received a First Class grade for this submission._

### Overview
Each directory in this repository corresponds to a registry service orginally hosted using Docker on the Queen's Private Cloud - QPC, and managed using Rancher - K8s. The core application,
(webcalc) is a basic HTML frontend, where every arithmetic operation corresponds to a different service endpoint. Each operation is written using a different stack. There also features a value
persistence/load operation allowing users to store values from previous operations, as well as a endpoint proxy and service failure handler. 

## Services Breakdown

### Services Provided With Assignment
- [**webcalc-frontend**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-frontend): Simple calculator container containing static HTML and JS that implements the calculator.
- [**webcalc-add**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc-add): PHP Based container that accepts two parameters to complete addition.
- [**webcalc-subtract**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc-subtract): Node/Express Based container that accepts two parameters to complete subtraction.

### Services Implemented
- [**webcalc-multiply**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-multiply): Python-Flask based container that accepts 2 parameters and returned multipied value. Includes basic CI testing, 6 error response tests and 3 logic response tests that run every hour. When the server provides no response, a second backup server also hosted on QPC is used.
- [**webcalc-square**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-square): C# .NET based container that accepts 2 parameters and returned exponent value. When the server provides no response, a second backup server also hosted on QPC is used.
- [**webcalc-modulo**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-modulo): Java-Spring based container that accepts 2 parameters and returned modulo value. When the server provides no response, a second backup server also hosted on QPC is used.
- [**webcalc-divide**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-divide): Golang based container that accepts 2 parameters and returned division result. When the server provides no response, a second backup server also hosted on QPC is used.

### Further Features Implemented
- [**webcalc-proxy**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-modulo): Proxy service implemented in python that accepts 3 parameters - 2 integer values and an operation string. Proxy decodes the request and uses the respective service to return to the frontend. Every service also contains a backup server, which the proxy will use should the main server not provide a response in adequate time.
- [**webcalc-monitor-service**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-monitor-service): Monitor service written in Python-Flask, app.py implements functions defined in monitor_functions.py to monitor and analyse responses across all servers within the system. From these variety of functions, analytics for all servers can be defined and are emailed daily to my private inbox as a 'Performance Report'.
- [**webcalc-mongodb-flask**](https://github.com/john-mcgurk/Cloud-Computing-Final-Assignment-2021/tree/main/webcalc/webcalc-mongodb-flask): A Python-Flask API that interacts with a MongoDB instance hosted on the QPC to allow for persistence of results from the calculator. Allows for both load and save values.

## Network Diagram
![image](https://user-images.githubusercontent.com/73965127/208995484-9918a69b-7a05-43e5-92e1-645aa7763ad2.png)
