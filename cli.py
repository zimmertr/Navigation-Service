import sys, requests

start 		= sys.argv[1]
end 		= sys.argv[2]

if len(sys.argv) > 3:
	orsApi	= sys.argv[3]
else:
	orsApi 	= "http://localhost:8080/ors/v2/"

def getDirections(start: str, end: str, orsApi: str) -> str:
	r = requests.get(orsApi+"directions/driving-car?start="+start+"&end="+end)
	print(r.json())
	
getDirections(start, end, orsApi)
