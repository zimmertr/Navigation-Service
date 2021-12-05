# Navigation Service

<hr>

## Summary

Navigation Service is a Python application that receives two coordinate pairs and leverages [OpenRouteService](https://github.com/GIScience/openrouteservice) to determine driving directions between them. 

## Example

```bash
$> python3 app.py 8.681495,49.41461 8.687872,49.420318
{"type":"FeatureCollection","metadata":{"attribution":"openrouteservice.org, OpenStreetMap contributors","service":"routing","timestamp":1638731341901,"query":{"coordinates":[[8.681495,49.41461],[8.687872,49.420318]],"profile":"driving-car","format":"json"},"engine":{"version":"6.6.1","build_date":"2021-12-05T18:17:38Z","graph_date":"2021-12-05T18:20:23Z"}},"features":[{"bbox":[8.681445,49.41461,8.690123,49.420514],"type":"Feature","properties":{"segments":[{"distance":1365.3,"duration":315.2,"steps":[{"distance":312.2,"duration":74.9,"type":11,"instruction":"Head north on Wielandtstraße","name":"Wielandtstraße","way_points":[0,6]},{"distance":253.2,"duration":60.8,"type":1,"instruction":"Turn right onto Mönchhofstraße","name":"Mönchhofstraße","way_points":[6,13]},{"distance":213.2,"duration":51.2,"type":0,"instruction":"Turn left onto Keplerstraße","name":"Keplerstraße","way_points":[13,14]},{"distance":372.9,"duration":89.5,"type":1,"instruction":"Turn right onto Moltkestraße","name":"Moltkestraße","way_points":[14,20]},{"distance":83.0,"duration":7.5,"type":0,"instruction":"Turn left onto Handschuhsheimer Landstraße, B 3","name":"Handschuhsheimer Landstraße, B 3","way_points":[20,22]},{"distance":130.8,"duration":31.4,"type":0,"instruction":"Turn left onto Roonstraße","name":"Roonstraße","way_points":[22,25]},{"distance":0.0,"duration":0.0,"type":10,"instruction":"Arrive at Roonstraße, straight ahead","name":"-","way_points":[25,25]}]}],"way_points":[0,25],"summary":{"distance":1365.3,"duration":315.2}},"geometry":{"coordinates":[[8.681495,49.41461],[8.681445,49.415755],[8.681509,49.416087],[8.681674,49.4166],[8.681815,49.417079],[8.681873,49.417276],[8.681882,49.417391],[8.682107,49.41739],[8.682461,49.417389],[8.68269,49.417388],[8.682782,49.417388],[8.683596,49.417386],[8.684681,49.417373],[8.685382,49.417368],[8.68504,49.419273],[8.686507,49.41943],[8.687109,49.419488],[8.6883,49.41962],[8.688398,49.41963],[8.690104,49.419828],[8.690123,49.419833],[8.689854,49.420216],[8.689652,49.420514],[8.68963,49.42051],[8.688601,49.420393],[8.687872,49.420318]],"type":"LineString"}}],"bbox":[8.681445,49.41461,8.690123,49.420514]}
````

## Requirements

* [Python 3](https://www.python.org/downloads/)
* [Requests Python Module](https://docs.python-requests.org/en/latest/user/install/)

## Instructions

Use Python 3 to call `app.py` and pass any necessary arguments. 

```bash
python3 app.py $START $END $APISERVER
```

## Arguments

| Argument  | Description                        | Required | Default                       |
| --------- | ---------------------------------- | -------- | ----------------------------- |
| START     | Starting Coordinate Pair           | Yes      | N/A                           |
| END       | Ending Coordinate Pair             | Yes      | N/A                           |
| APISERVER | OpenRouteService API Server to Use | No       | http://localhost:8080/ors/v2/ |

## ToDo

- [ ] Add argument for API Key for non-local OpenRouteService API
- [ ] Modify app to communicate over web API



