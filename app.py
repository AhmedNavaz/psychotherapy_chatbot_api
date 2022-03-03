from flask import Flask, jsonify, request
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "This is psychotherapy chatbot"})


@app.route("/chatbot", methods=["POST"])
def response():
    query = dict(request.form)['query']
    result = chatbot_response(query)
    return jsonify({"response": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", )