import sys, requests

start 		= sys.argv[1]
end 		= sys.argv[2]

if len(sys.argv) > 3:
	orsServer	= sys.argv[3]
else:
	orsServer 	= "http://localhost:8080/ors/v2/"

def getDirections(start: str, end: str, orsServer: str) -> str:
	r = requests.get(orsServer+"directions/driving-car?start="+start+"&end="+end)
	print(r.json())
	
getDirections(start, end, orsServer)
