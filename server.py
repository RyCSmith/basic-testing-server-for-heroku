from flask import Flask
app = Flask(__name__)
from flask import Response
from flask import request

# from flask import json
# from flask import jsonify

@app.route("/200")
def two_hundred():
	print request.__dict__
	# print request.args
	# print request.headers
	return Response("You got a 200!", status=200, mimetype='text/plain')


@app.route("/404")
def four_o_four():
	print request.__dict__
	return Response("You got a 404!", status=404, mimetype='text/plain')

@app.route("/500")
def five_hundred():
	print request.__dict__
	return Response("You got a 500!", status=500, mimetype='text/plain')
