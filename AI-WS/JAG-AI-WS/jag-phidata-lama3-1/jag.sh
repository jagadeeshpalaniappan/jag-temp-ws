# STOP ALL DOCKER CONTAINER
docker stop $(docker ps -a -q)

# REMOVE ALL DOCKER CONTAINER
docker rm $(docker ps -a -q)
# ----------------------------

docker network create my_network

docker run -d --name python-app --net my_network -p 8080:80 python:3.9-slim python app.py

docker run -d --name app2 --net my_network -p 8081:80 another-app-image

curl http://172.17.0.2:8080/api/ endpoint

docker run -d --name python-app --net my_network -p 8080:80 python:3.9-slim python app.py


# ----------------------------

docker network create jag_network

docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  --net jag_network \
  phidata/pgvector:16


docker rm -f pgvector

# Remove the existing container
docker rm -f jag-phidata-lama3-1
# Stop and remove the existing container
docker stop jag-phidata-lama3-1


docker build -t jag-phidata-lama3-1 .
docker run -d --name jag-phidata-lama3-1  -p 8501:8501 jag-phidata-lama3-1

docker run -d --name jag-phidata-lama3-1  --net jag_network -p 8501:8501 jag-phidata-lama3-1


