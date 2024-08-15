

### 1. Create a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Install libraries

```shell
pip install -r requirements.txt
```


### 3.API Keys

```shell
export OPENAI_API_KEY=xxxxxxxxxx
export OPENAI_MODEL_NAME=gpt-4o
```


### 4.Run pgvector DB

```shell
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
```




### 4.Run the App

```shell
python app.py
```

