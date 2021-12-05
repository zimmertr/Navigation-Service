# Navigation Service

<hr>

## Summary

Navigation Service is a Python application that receives two coordinate pairs and leverages [OpenRouteService](https://github.com/GIScience/openrouteservice) to determine driving directions between them. 

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



