sudo docker build . -t dahol/invpy
sudo docker stop invpy # if already running
sudo docker rm invpy # if already running
sudo docker run -p 80:8000 --name invpy -d dahol/invpy