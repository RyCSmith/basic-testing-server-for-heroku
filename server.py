from flask import Flask
app = Flask(__name__)
from flask import Response
from flask import request

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def root():
	print(request.__dict__)
	return Response("You're at the root.<br/>Nothing's here yo...", status=200, mimetype='text/html')

@app.route("/200", methods=['GET', 'POST', 'PUT', 'DELETE'])
def two_hundred():
	print(request.__dict__)
	return Response("You got a 200!", status=200, mimetype='text/plain')


@app.route("/404", methods=['GET', 'POST', 'PUT', 'DELETE'])
def four_o_four():
	print(request.__dict__)
	return Response("You got a 404!", status=404, mimetype='text/plain')

@app.route("/500", methods=['GET', 'POST', 'PUT', 'DELETE'])
def five_hundred():
	print(request.__dict__)
	return Response("You got a 500!", status=500, mimetype='text/plain')
