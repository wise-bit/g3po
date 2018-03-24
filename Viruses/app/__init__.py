from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)
app.static_folder = 'static'
# app._static_folder = os.path.abspath("static/style.css")
print(os.path.abspath(app._static_folder))

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()

