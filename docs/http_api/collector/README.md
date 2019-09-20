# Collector

## Adding a Collector
This endpoint allows the current user to add a new collector in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"mac" : "12334421",	"collector_type": Wise}` |
| **Request Response**  | `{"id": 1,"created": "2019-09-18T12:18:55.826760Z","modified": "2019-09-18T12:18:55.826760Z","mac": "1324424123213","collector_type": "HW","company_id": 1}` |


## Listing the Collectors
This endpoint allows the current user to list the collectors of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 1,"created": "2019-09-18T12:18:55.826760Z","modified": "2019-09-18T12:18:55.826760Z","mac": "1324424123213","collector_type": "HW","company_id": 1}]}` |


## Retrieving a Collector
This endpoint allows the current user to retrieve a collector of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | /v1/companies/1/collectors/1/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "id": 1,"created": "2019-09-18T12:18:55.826760Z","modified": "2019-09-18T12:18:55.826760Z","mac": "1324424123213","collector_type": "HW","company_id": 1}` |


## Updating a Collector
This endpoint allows the current user to update a collector of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"mac" : "1324424123",	"collector_type": Lora}` |
| **Request Response**  | `{"id": 1,"created": "2019-09-18T12:18:55.826760Z","modified": "2019-09-20T13:51:50.982075Z","mac": "1324424123","collector_type": "Lora","company_id": 1}` |

## Deleting a Collector
This endpoint allows the current user to delete a collector of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |