[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-orange.svg)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=bugs)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=aliartiza75_flask-frontend-application&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=aliartiza75_flask-frontend-application)](https://sonarcloud.io/summary/new_code?id=aliartiza75_flask-frontend-application)



# Flask Frontend Application

This repository contains frontend logic and kubernetes manifests. I have used `minikube` for this project. Installation steps is given in this [gist](https://gist.github.com/aliartiza75/3a34f059de62c7de04727dae6a363ea8) 

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
* To access the frontend service
```bash
# to get list of services, copy the CLUSTER_IP
sudo kubectl get service

# Open the browser and type this URL. It will display a web page containing two buttons. The Get Date button will call the backend service
http://CLUSTER_IP:5002
```

* To curl the backend service from frontend pod
```bash
# To get pod list.
sudo kubectl get pods

# Copy the pod id of the frontend service and use the command below to enter the pod
sudo kubectl exec -it <frontend-service-pod-id> /bin/bash

# To curl the backend service
curl -X GET "http://<backend-pod-ip>:5001/datetime"
```

# Guidelines for helm charts deployment
* Helm installation guidelines [link](https://helm.sh/docs/install/#installing-the-helm-client)

* Once the helm is installed, use the command given below to install tiller in kubernetes cluster:
```bash
helm init
```

* To create a helm chart folder:

```bash
helm create <app-name>
```

* To dry run the helm chart for debugging:
```bash
sudo helm install --dry-run --debug <chart-directory>
```

* To purge a release
```bash
sudo helm del --purge <release-name>
```

* To check the status of a release
```bash
sudo helm ls --all <release-name>
```

* To search a helm package name
```bash
sudo helm search <package-name>
```

* To create a package from the helm charts folder
```bash
sudo helm package <helm-charts-package-folder-path>
```

# Important Notes
* Start the minikube cluster in the virtual machine drive in none mode [--vm-driver=none], otherwise services will not be accessible.
* Minikube will pull images from the dockerhub.
* In some cases minikube cluster doesn't work properly, one quick fix is to delete the cluster and restart the minikube cluster.
