# Cloud Computing - _Final Assignment 2021_
_This repository contains my final submission for the Cloud Computing module in Queen's University Belfast. I received a First Class grade for this submission._

### Overview
Each directory in this repository corresponds to a registry service orginally hosted using Docker on the Queen's Private Cloud - QPC, and managed using Rancher - K8s. The core application,
(webcalc) is a basic HTML frontend, where every arithmetic operation corresponds to a different service endpoint. Each operation is written using a different stack. There also features a value
persistence/load operation allowing users to store values from previous operations, as well as a endpoint proxy and service failure handler. 

## Services Breakdown

### Services Provided With Assignment
- [**webcalc-frontend**](): Simple calculator container containing static HTML and JS that implements the calculator.
- [**webcalc-add**](): PHP Based container that accepts two parameters to complete addition.
- [**webcalc-subtract**](): Node/Express Based container that accepts two parameters to complete subtraction.

## Network Diagram
![image](https://user-images.githubusercontent.com/73965127/208995484-9918a69b-7a05-43e5-92e1-645aa7763ad2.png)
