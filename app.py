from aitextgen import aitextgen
from flask import Flask, jsonify

app = Flask(__name__)
ai = aitextgen(model_folder="model", tokenizer_file="model/aitextgen.tokenizer.json")


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/name/")
def generate_name():
    generated = ai.generate_one().strip()
    app.logger.info(generated)
    return jsonify({"name": generated})


@app.route("/name/<prompt>")
def generate_name_prompt(prompt):
    generated = ai.generate_one(prompt=prompt).strip()
    app.logger.info(generated)
    return jsonify({"name": generated})
