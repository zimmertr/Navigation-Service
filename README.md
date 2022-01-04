# Navigation Service

<hr>

## Summary

Navigation Service is a Python application with a [Flask](https://flask.palletsprojects.com/en/2.0.x/) web frontend that is used to determine driving directions between two coordinate pairs. Flask listens for incoming requests to `/directions` and when one is received, it leverages the [Requests](https://docs.python-requests.org/en/latest/) HTTP library to invoke a secondary request to an instance of [OpenRouteService](https://github.com/GIScience/openrouteservice). The applicaion accepts three parameters, `start`, `end`, and `server` which represent the respective coordinate pairs as well as the URL where OpenRouteService can be found. There is basic error handling that will detect when an invalid API path or parameters are used.

Navigation Service can be deployed in a multitude of ways. Included is a `Dockerfile` for building it as well as a `Docker-Compose` file for running it. It also has support for running on Kubernetes via an example `Kustomization` overlay. Or it can simply be ran locally on a workstation using `Python3`. Instructions are provided below for each use case. 

If one intends to deploy the Navigation Service into production the solution leveraging Kubernetes is recommended. Furthermore, they should consider the following elements to improve reliability & security:

* Use multiple replicas of the Navigation Service to ensure high availability. 
* Use a [managed instance](https://openrouteservice.org/plans/) of OpenRouteService or otherwise ensure it is also highly available. 
  * If you are self hosting OpenRouteService, ensure that you properly provide [JAVA_OPTS and CATALINE_OPTS](https://github.com/GIScience/openrouteservice/blob/master/docker/docker-compose.yml#L22) to your deployment to ensure proper resource and security configurations are enforced. Similarly, ensure that you provide Persistent Volumes for the [necessary directories](https://github.com/GIScience/openrouteservice/blob/master/docker/docker-compose.yml#L15) associated with your graphs, logs, configuration, etc. You might also consider ensuring that the workload is NOT run as the root user, whether it is deployed on a dedicated server or within a container. 

The Navigation Service can be tested. To get started I would recommend using [PyTest](https://docs.pytest.org/en/6.2.x/) and the Werkzeug test [`Client`](https://werkzeug.palletsprojects.com/en/2.0.x/test/#werkzeug.test.Client). This harness will allow you to automate the testing of authentication, various invalid and valid responses, contexts, and more. The Flask project provides extensive documentation on this procedure [here](https://flask.palletsprojects.com/en/2.0.x/testing/). 

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
  * [Kubernetes](https://kubernetes.io/docs/setup/)
  * [MetalLB](https://metallb.universe.tf/installation/)

## Instructions

### Using Docker & Docker-Compose with NGINX:

1. Generate an SSL certificate & private key using `openssl`:
   
   ```bash
   openssl req -nodes -x509 -newkey rsa:4096 -keyout nginx/key.pem -out nginx/cert.pem -sha256 -days 9999 -subj '/CN=nav.svc'
   ```
   
1. Create a DNS entry for `nav.svc` & `ors.svc`:
   
   ```bash
   echo "127.0.0.1    nav.svc" | sudo tee -a /etc/hosts
   echo "127.0.0.1    ors.svc" | sudo tee -a /etc/hosts
   ```
   
1. Build & run the infrastructure:
   
   ```bash
   docker-compose up -d
   ```
   
2. Wait for OpenRouteService to be available. This may take several minutes. You may test it with `curl`. If it responds `52`, it likely is not ready yet.

   ```bash
   curl 'http://ors.svc:8080/ors/v2/directions/driving-car?start=8.681495,49.41461&end=8.687872,49.420318'
   ```

3. Issue a request to the Navigation Service, specifying the `start` and `end` coordinates as well as the OpenRouteService API Server:

   ```bash
   curl -k 'https://nav.svc/directions?start=8.681495,49.41461&end=8.687872,49.420318&server=http://ors-app:8080/ors/v2/'
   ```

### Using Kubernetes:

1. Build a Kubernetes cluster & deploy a Load Balancer integration. I use TKS & MetalLB.

2. Modify the Kustomization overlay as per your environment and deploy the Navigation Service & OpenRouteService to Kubernetes. 

   ```bash
   kubectl apply -k Kustomize/overlays/example
   ```

3. Wait for OpenRouteService to be available. This may take several minutes. A `readinessProbe` will release it when it is. You can ensure it is running by tailing the logs:

   ```bash
   kubectl logs -f -n nav-svc ors-app-#########-#####
   ```

4. Ensure that the Navigation Service has a Load Balancer configured properly. `EXTERNAL-IP` should be populated.

   ```bash
   kubectl get svc -n nav-svc nav-svc
   ```

5. Issue a request to the Navigation Service, specifying the `start` and `end` coordinates as well as the OpenRouteService API Server:

   ```bash
   curl 'http://192.168.50.200:5000/directions?start=8.681495,49.41461&end=8.687872,49.420318&server=http://ors-app:8080/ors/v2/'
   ```

### Using Python & Flask

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
### Using Python:

1. Install the requirements:

   ```bash
   pip3 install -r requirements.txt
   ```

2. Ensure that you have access to an instance of OpenRouteService.

2. Use Python 3 to call `cli.py` and pass any necessary arguments. 

   ```bash
   python3 cli.py $start $end $server
   ```

## Arguments

| Argument | Description                        |
| -------- | ---------------------------------- |
| `start`  | Starting Coordinate Pair           |
| `end`    | Ending Coordinate Pair             |
| `server` | OpenRouteService API Server to Use |

## TODO

* Build NGINX configuration for proxying requests to each service 
* Build a diagram for the network and infrastructure topology
* Add additional production considerations to the Summary
* Add unit testing examples
* Test OpenRouteService with additional OSM datasets 
* Test scaling with multiple replicas in Kubernetes 
* Lean on TLS & NGINX to enforce authentication to the Navigation Service & encryption between it and the OpenRouteService. 
