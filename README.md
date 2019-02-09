# ht-fe

HT front end repository


# building image
sudo docker build -t ht-fe:0.0.1 -f Dockerfile .

# to start the container

sudo docker run -e FLASK_ENV=development -e FLASK_HOST_IP=0.0.0.0 -e=FLASK_HOST_PORT=5001 -e BE_IP_ADDR=<172.17.0.4>:5001 -p 9002:5001 ht-fe:0.0.1
