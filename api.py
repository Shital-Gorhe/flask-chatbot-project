#file for API call and run flask server
"""from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Chatbot API is running"


app.run()
"""
from flask import Flask, jsonify, request
from chatbot_database import find_answer, add_knowledge , update_knowledge , remove_knowledge , knowledge_exists

app = Flask(__name__)


# -------------------------------
# GET - Read knowledge
# -------------------------------

@app.route("/answer/<question>")
def get_answer(question):


    question = question.strip().lower()
    answer = find_answer(question)

    if answer:
        return jsonify({
            "question": question,
            "answer": answer
        })

    return jsonify({
        "question": question,
        "answer": "I don't know the answer."
    })


# -------------------------------
# POST - Receive knowledge (teaches chatbot new knowledge)
# -------------------------------

@app.route("/knowledge", methods=["POST"])
def add_knowledge_api():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON data is required."
        }), 400

    question = data.get("question")
    answer = data.get("answer")

    if not question or not question.strip():
        return jsonify({
            "error": "Question is required."
        }), 400

    if not answer or not answer.strip():
        return jsonify({
            "error": "Answer is required."
        }), 400

    question = question.strip().lower()
    answer = answer.strip()

    if knowledge_exists(question):
        return jsonify({
            "error": "Question already exists."
        }), 409

    add_knowledge(question, answer)

    return jsonify({
        "message": "Knowledge added successfully.",
        "question": question,
        "answer": answer
    }), 201

# -------------------------------
# PUT - UPDATE knowledge
# -------------------------------
@app.route("/knowledge", methods=["PUT"])
def update_knowledge_api():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "JSON data is required."
        }), 400

    question = data.get("question")
    answer = data.get("answer")

    if not question or not question.strip():
        return jsonify({
            "error": "Question is required."
        }), 400

    if not answer or not answer.strip():
        return jsonify({
            "error": "Answer is required."
        }), 400

    question = question.strip().lower()
    answer = answer.strip()

    if not knowledge_exists(question):
        return jsonify({
            "error": "Question does not exist."
        }), 404

    update_knowledge(question, answer)

    return jsonify({
        "message": "Knowledge updated successfully.",
        "question": question,
        "answer": answer
    })

# -------------------------------
# DELETE - DELETE knowledge
# -------------------------------

@app.route("/knowledge/<question>", methods=["DELETE"])
def delete_knowledge_api(question):

    question = question.strip().lower()

    if not knowledge_exists(question):
        return jsonify({
            "error": "Question does not exist."
        }), 404

    remove_knowledge(question)

    return jsonify({
        "message": "Knowledge deleted successfully.",
        "question": question
    }), 200

if __name__ == "__main__":
    app.run()