from flask import Flask, Response, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate/<value>')
def translate(value):
    return render_template('translate.html', value=int(value))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
