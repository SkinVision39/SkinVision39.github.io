from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def hello_world():
    return 'Привет, мир! Это мой первый веб-сайт на Flask!'

if __name__ == '__main__':
    freezer.freeze()

