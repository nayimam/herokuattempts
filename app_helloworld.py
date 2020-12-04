from flask import Flask


app = Flask(__name__)

@app.route('/')

def index():
	return "mamsemamasaw muma"
	
if __name__=="main":
	app.run()	
