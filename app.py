from flask import Flask

app = Flask("marconi")

@app.route('/')
def hello():
	return "ciao sono Luigi"
