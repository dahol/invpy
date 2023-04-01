docker build . -t dahol/invpy
docker stop invpy
docker rm invpy
docker run -p 80:8000 --name invpy -d dahol/invpy