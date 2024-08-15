# RAG
Rag (Retreival Augmented Generation) Python solution with llama3, LangChain, Ollama and ChromaDB in a Flask API based solution



### 1. Create a virtual environment

```shell
python3 -m venv ~/.venvs/aienv
source ~/.venvs/aienv/bin/activate
```

### 2. Install libraries

```shell
pip install -r requirements.txt
```


### 4.Turn Off Proxy and MyApps

```sh
# Turn OFF MyApps and run the app

export HTTP_PROXY=""
export HTTPS_PROXY=$HTTP_PROXY
export http_proxy=$HTTP_PROXY
export https_proxy=$HTTP_PROXY
export all_proxy=$HTTP_PROXY
export ALL_PROXY=$HTTP_PROXY
```

### 4.Run the App

```shell
python app.py
```

