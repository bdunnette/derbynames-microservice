import random

from aitextgen import aitextgen
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)
MIN_TEMP = 0.7
MAX_TEMP = 1.5
TOP_P = 0.9
MAX_LENGTH = 100

ai = aitextgen(model_folder="model", tokenizer_file="model/aitextgen.tokenizer.json")


@app.route("/")
def home(name=None):
    return render_template("index.html", name=name)


@app.route("/name")
def generate_name():
    max_length = request.args.get("max_length", MAX_LENGTH)
    top_p = request.args.get("top_p", TOP_P)
    max_temp = request.args.get("max_temp", MAX_TEMP)
    min_temp = request.args.get("min_temp", MIN_TEMP)
    temperature = request.args.get("temperature", random.uniform(MIN_TEMP, MAX_TEMP))
    prompt = request.args.get("prompt", None)
    if prompt:
        prompt = prompt.strip()
        generated = ai.generate_one(
            temperature=abs(float(temperature)),
            top_p=TOP_P,
            max_length=MAX_LENGTH,
            prompt=prompt,
        ).strip()
    if not prompt:
        generated = ai.generate_one(
            temperature=abs(float(temperature)), top_p=TOP_P, max_length=MAX_LENGTH
        ).strip()
    app.logger.info(generated)
    return jsonify(
        {
            "name": generated,
            "temperature": temperature,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "top_p": top_p,
            "max_length": max_length,
            "prompt": prompt,
        }
    )
