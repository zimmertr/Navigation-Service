import sys, requests

start 		= sys.argv[1]
end 		= sys.argv[2]

if len(sys.argv) > 3:
	orsServer	= sys.argv[3]
else:
	orsServer 	= "http://localhost:8080/ors/v2/"

def getDirections(start: str, end: str, orsServer: str) -> str:
	try:
		startX 	= start.split(",")[0] 
		startY 	= start.split(",")[1]
		endX 	= end.split(",")[0]
		endY 	= end.split(",")[1]
	except IndexError:
		print("Invalid coordinate pairs were provided!")

	r = requests.get(orsServer+"directions/driving-car?start="+start+"&end="+end)
	print(r.text)

getDirections(start, end, orsServer)
