from flask import Flask


app = Flask(__name__)

@app.route('/')

def index():
	print("bababa")
	return "mamsemamasaw baba muma"
	
if __name__=="main":
	app.run()	
