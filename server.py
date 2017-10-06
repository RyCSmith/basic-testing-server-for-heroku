from flask import Flask
app = Flask(__name__)
from flask import Response
from flask import request
import json

# from flask import json
# from flask import jsonify
@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def root():
	log_request_data(request)
	# print request.args
	# print request.headers
	return Response("You're at the root.<br/>Nothing's here yo...", status=200, mimetype='text/html')

@app.route("/200", methods=['GET', 'POST', 'PUT', 'DELETE'])
def two_hundred():
	log_request_data(request)
	return Response("You got a 200!", status=200, mimetype='text/plain')


@app.route("/404", methods=['GET', 'POST', 'PUT', 'DELETE'])
def four_o_four():
	log_request_data(request)
	return Response("You got a 404!", status=404, mimetype='text/plain')

@app.route("/500", methods=['GET', 'POST', 'PUT', 'DELETE'])
def five_hundred():
	log_request_data(request)
	return Response("You got a 500!", status=500, mimetype='text/plain')

def log_request_data(request):
	r = {
		'endpoint' :request.endpoint,
		'json' : request.get_json(force=True, silent=True),
		'method' : request.method,
		'path' : request.path,
		'full_path' : request.full_path,
		'script_root' : request.script_root,
		'url' : request.url,
		'base_url' : request.base_url,
		'url_root' : request.url_root,
		'data' : request.data,
		'args' : request.args
	}
	print(json.dumps(r, default=lambda o: o.__dict__, indent=4, sort_keys=True))