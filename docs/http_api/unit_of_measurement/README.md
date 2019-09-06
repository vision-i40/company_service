# Product

## Adding a Unit of Measurement
This endpoint allows the current user to add a new Unit of Measurement in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/2/units_of_measurement/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name" : "test unit 1",	"is_default": true,	"conversion_factor": 1}` |
| **Request Response**  | `{"id": 4,"name" : "test unit 1",	"is_default": true,	"conversion_factor": 1,"created","2019-09-06T00:08:07.288388Z","modified":"2019-09-06T00:08:07.288388Z"}` |


## Listing the products
This endpoint allows the current user to list the products of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/2/units_of_measurement     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 1,            "name": "test unit update","is_default": false,"conversion_factor": 0.5,"created": "2019-09-04T02:24:22.156384Z","modified": "2019-09-06T00:55:39.352918Z"}]}` |


## Retrieving a Unit of Measurement
This endpoint allows the current user to retrieve a Unit of Measurement of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | /v1/companies/1/products/2/units_of_measurement/1/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 1,"name": "test unit 1","is_default": true,"conversion_factor": 1,"created": "2019-09-04T02:24:22.156384Z","modified":"2019-09-06T00:55:39.352918Z"}` |


## Updating a Unit of Measurement
This endpoint allows the current user to update a Unit of Measurement of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/2/units_of_measurement/1/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name":"test unit update", "is_default": false, "conversion_factor": 0.5}` |
| **Request Response**  | `{"id": 1,"name": "test unit update","is_default": false,"conversion_factor": 0.5,"created": "2019-09-04T02:24:22.156384Z","modified":"2019-09-06T00:55:39.352918Z"}` |

## Deleting a Unit of Measurement
This endpoint allows the current user to delete a Unit of Measurement of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/2/units_of_measurement/1/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |
