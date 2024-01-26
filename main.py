from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world(message=None):
    message = 'Ello!'
    return render_template('welcome.html', message=message)

@app.route("/optional")
def test_opt():
	return render_template('index.html')
