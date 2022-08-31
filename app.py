from aitextgen import aitextgen
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)

ai = aitextgen(model_folder="model", tokenizer_file="model/aitextgen.tokenizer.json")


@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)


@app.route("/name/")
# @cross_origin()
def generate_name():
    generated = ai.generate_one().strip()
    app.logger.info(generated)
    return jsonify({"name": generated})


@app.route("/name/<prompt>")
# @cross_origin()
def generate_name_prompt(prompt):
    generated = ai.generate_one(prompt=prompt).strip()
    app.logger.info(generated)
    return jsonify({"name": generated, "prompt": prompt})
