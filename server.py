from flask import Flask
app = Flask(__name__)
from flask import Response
from flask import request

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def root():
	print(request.__dict__)
	return Response("You're at the root.<br/>Nothing's here yo...", status=200, mimetype='text/html')

@app.route("/<int:desired_response_code>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def two_hundred(desired_response_code):
	print("User is requesting response code: " + str(desired_response_code))
	print(request.__dict__)
	return Response("You got a {code}!".format(code=desired_response_code), status=desired_response_code, mimetype='text/plain')
