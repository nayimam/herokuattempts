from flask import Flask


app = Flask(__name__)

@app.route('/')

def index():
	return "Hello fsaf"
	
if __name__=="main":
	app.run()	