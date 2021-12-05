import json, requests
from flask import Flask, request

api = Flask(__name__)

@api.route('/directions', methods=['GET'])
def directions():

	startCoordinates 	= request.args.get('start')
	endCoordinates		= request.args.get('end')
	orsServer			= request.args.get('server')

	return requests.get(orsServer+"directions/driving-car?start="+startCoordinates+"&end="+endCoordinates).json()

@api.errorhandler(500)
def not_found(error):
	return "Invalid parameters were provided!"

@api.errorhandler(404)
def not_found(error):
	return "Invalid API path was provided!"

if __name__ == '__main__':
	api.run(host='0.0.0.0')
