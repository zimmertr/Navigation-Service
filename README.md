# Navigation Service

<hr>

## Summary

Navigation Service is a Python application that receives two coordinate pairs and leverages [OpenRouteService](https://github.com/GIScience/openrouteservice) to determine driving directions between them. 

## Example

```bash
$> curl 'http://localhost:5000/directions?start=8.681495,49.41461&end=8.687872,49.420318&server=http://ors-app:8080/ors/v2/'
{"bbox":[8.681445,49.41461,8.690123,49.420514],"features":[{"bbox":[8.681445,49.41461,8.690123,49.420514],"geometry":{"coordinates":[[8.681495,49.41461],[8.681445,49.415755],[8.681509,49.416087],[8.681674,49.4166],[8.681815,49.417079],[8.681873,49.417276],[8.681882,49.417391],[8.682107,49.41739],[8.682461,49.417389],[8.68269,49.417388],[8.682782,49.417388],[8.683596,49.417386],[8.684681,49.417373],[8.685382,49.417368],[8.68504,49.419273],[8.686507,49.41943],[8.687109,49.419488],[8.6883,49.41962],[8.688398,49.41963],[8.690104,49.419828],[8.690123,49.419833],[8.689854,49.420216],[8.689652,49.420514],[8.68963,49.42051],[8.688601,49.420393],[8.687872,49.420318]],"type":"LineString"},"properties":{"segments":[{"distance":1365.3,"duration":315.2,"steps":[{"distance":312.2,"duration":74.9,"instruction":"Head north on Wielandtstra\u00dfe","name":"Wielandtstra\u00dfe","type":11,"way_points":[0,6]},{"distance":253.2,"duration":60.8,"instruction":"Turn right onto M\u00f6nchhofstra\u00dfe","name":"M\u00f6nchhofstra\u00dfe","type":1,"way_points":[6,13]},{"distance":213.2,"duration":51.2,"instruction":"Turn left onto Keplerstra\u00dfe","name":"Keplerstra\u00dfe","type":0,"way_points":[13,14]},{"distance":372.9,"duration":89.5,"instruction":"Turn right onto Moltkestra\u00dfe","name":"Moltkestra\u00dfe","type":1,"way_points":[14,20]},{"distance":83.0,"duration":7.5,"instruction":"Turn left onto Handschuhsheimer Landstra\u00dfe, B 3","name":"Handschuhsheimer Landstra\u00dfe, B 3","type":0,"way_points":[20,22]},{"distance":130.8,"duration":31.4,"instruction":"Turn left onto Roonstra\u00dfe","name":"Roonstra\u00dfe","type":0,"way_points":[22,25]},{"distance":0.0,"duration":0.0,"instruction":"Arrive at Roonstra\u00dfe, straight ahead","name":"-","type":10,"way_points":[25,25]}]}],"summary":{"distance":1365.3,"duration":315.2},"way_points":[0,25]},"type":"Feature"}],"metadata":{"attribution":"openrouteservice.org, OpenStreetMap contributors","engine":{"build_date":"2021-12-05T21:43:16Z","graph_date":"2021-12-05T21:45:58Z","version":"6.6.1"},"query":{"coordinates":[[8.681495,49.41461],[8.687872,49.420318]],"format":"json","profile":"driving-car"},"service":"routing","timestamp":1638740766945},"type":"FeatureCollection"}
````

## Requirements

* [Python 3](https://www.python.org/downloads/)
* Python Modules: 
  * [Requests](https://docs.python-requests.org/en/latest/user/install/)
  * [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
* Optional
  * [Docker](https://docs.docker.com/get-docker/)
  * [Docker-Compose](https://docs.docker.com/compose/install/)



## Instructions

### Using Docker-Compose:

1. Build & run the infrastructure:
   ```bash
   docker-compose up -d
   ```

2. Wait for OpenRouteService to be available. This may take several minutes. You may test it with `curl`. If it responds `52`, it likely is not ready yet.

   ```bash
   curl 'http://localhost:8080/ors/v2/directions/driving-car?start=8.681495,49.41461&end=8.687872,49.420318'
   ```

3. Issue a request to the Navigation Service, specifying the `start` and `end` coordinates as well as the OpenRouteService API Server:

   ```bash
   curl 'http://localhost:5000/directions?start=8.681495,49.41461&end=8.687872,49.420318&server=http://ors-app:8080/ors/v2/'
   ```

### Using the API:

1. Install the requirements:

   ```bash
   pip3 install -r requirements.txt
   ```

2. Ensure that you have access to an instance of OpenRouteService.

2. Start the API Server:

   ```bash
   python3 api.py
   ```

3. Invoke a request:

   ```bash
   curl 'http://localhost:5000/directions?start=8.681495,49.41461&end=8.687872,49.420318&server=http://localhost:8080/ors/v2/'
   ```
### Using the CLI:

1. Install the requirements:

   ```bash
   pip3 install -r requirements.txt
   ```

2. Ensure that you have access to an instance of OpenRouteService.

2. Use Python 3 to call `app.py` and pass any necessary arguments. 

   ```bash
   python3 app.py $start $end $server
   ```

## Arguments

| Argument | Description                        |
| -------- | ---------------------------------- |
| `start`  | Starting Coordinate Pair           |
| `end`    | Ending Coordinate Pair             |
| `server` | OpenRouteService API Server to Use |



