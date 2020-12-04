from flask import Flask


app = Flask(__name__)

@app.route('/')

def index():
	print("bababa")
	return "mamsemamasaw muma"
	
if __name__=="main":
	app.run()	
