from ask_ai import ask_ai
from ask_ai_with_knowledge import ask_ai_with_knowledge
from flask import Flask, request
from load_knowledge import load_knowledge

app = Flask(__name__)


@app.route("/ai", methods=["POST"])
def ai():
    json_content = request.json
    query = json_content.get("query")
    print(f"/ai:query: {query}")

    response = ask_ai(query)
    response_answer = {"answer": response}
    return response_answer


@app.route("/ask_pdf", methods=["POST"])
def ask_pdf():
    json_content = request.json
    query = json_content.get("query")
    print(f"/ask_pdf:query: {query}")

    response_answer = ask_ai_with_knowledge(query)
    return response_answer


@app.route("/load_pdf", methods=["POST"])
def load_knowledge_from_api_pdf():

    # 1. Save file locally and pass the 'file_name' to loader
    file = request.files["file"]
    file_name = "pdf/" + file.filename
    file.save(file_name)
    print(f"/load_pdf:filename: {file_name}")

    # 2. load the newly saved file into knowledge (Chroma Store - Vector DB)
    response = load_knowledge(file_name)
    return response


def start_app():
    app.run(host="0.0.0.0", port=4040, debug=True)


if __name__ == "__main__":
    start_app()
