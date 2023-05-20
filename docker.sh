docker build . -t dahol/invpy
docker stop invpy # if already running
docker rm invpy # if already running
docker run -p 80:8000 --name invpy -d dahol/invpy