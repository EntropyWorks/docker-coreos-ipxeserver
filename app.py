# app.py
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/ping')
def ping():
	return 'PONG-foo'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
