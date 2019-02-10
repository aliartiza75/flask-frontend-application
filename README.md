# HT Frontend Repository

This repository contains frontend logic and kubernetes manifests.


# Guidelines for containerizing frontend
* Building image
```bash
sudo docker build -t ht-fe:0.0.1 -f Dockerfile .
```

* To run docker container on host machine
```bash
sudo docker run -e FLASK_ENV=development -e FLASK_HOST_IP=0.0.0.0 -e=FLASK_HOST_PORT=5001 -e BE_IP_ADDR=<172.17.0.4>:5001 -p 9002:5001 ht-fe:0.0.1
```

# Kubernetes deployment Guidelines

Before the creation of frontend deployement, backend deployment and service *must* be created. Guideline for creating the backend deployment and service is given in the `README.md` file of backend respository. Once pre-requisites are completed. Frontend `deployment.yaml` file must be updated by changing the `BE_IP_ADDR` env variable with the ip address of the backend pod.

* To get the ip address of the backend pod, use the command given below:


```bash
# to get pod list
sudo kubectl get pods

# to get the information of the backend pod
sudo kubectl describe pod <pod-id>
```

* Once the above changes are done, create the frontend deployment.
```bash
sudo kubectl apply -f deployment.yaml
```

* To create the frontend service
```bash
sudo kubectl apply -f htfe_service.yaml
```
