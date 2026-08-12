from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    retun none:
    if none:


@app.route('/health')
def health():
    return 'Server is up and running'
