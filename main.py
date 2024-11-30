from flask import Flask, render_template, request, redirect, url_for
import pandas as pd


app = Flask(__name__)

df = pd.read_csv("data/dictionary.csv")

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def defi(word):
    definition = df.loc[df["word"] == str(word)]["definition"].squeeze()
    result_dictionary = {"definition": definition, "word": word}

    return result_dictionary

if __name__ == "__main__":
    app.run(debug=True, port=5001)


