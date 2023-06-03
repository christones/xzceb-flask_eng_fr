from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/englishToFrench, methods = 'POST'")
def englishToFrench():
    textToTranslate = request.args.get(text)
    # Write your code here
    return  englishTofrench(textToTranslate) 

@app.route("/frenchToEnglish, methods = 'POST'")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
