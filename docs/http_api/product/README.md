# Product

## Adding a product
This endpoint allows the current user to add a new product in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name": "new product"}` |
| **Request Response**  | `{"id": 4,"company_id": 1,"name": "another nice product name","units_of_measurement":[],"created","2019-09-06T00:08:07.288388Z","modified":"2019-09-06T00:08:07.288388Z"}` |


## Listing the products
This endpoint allows the current user to list the products of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 2, "next": null, "previous": null, "results": [ {"id": 2,"company_id": 1,"name": "a new nice product name","units_of_measurement": [{"id": 1,"name": "Displays","is_default": true,"conversion_factor": 1.0,"created": "2019-09-04T02:24:22.156384Z", "modified": "2019-09-04T02:24:22.156384Z"}],"created": "2019-09-04T01:45:02.746274Z","modified": "2019-09-06T00:17:37.348139Z"}, { "id": 1, <...> } ]}` |


## Retrieving a product
This endpoint allows the current user to retrieve a product of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/2/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 2,"company_id": 1,"name": "a new nice product name","units_of_measurement": [{"id": 1,"name": "Displays","is_default": true,"conversion_factor": 1.0,"created": "2019-09-04T02:24:22.156384Z", "modified": "2019-09-04T02:24:22.156384Z"}],"created": "2019-09-04T01:45:02.746274Z","modified": "2019-09-06T00:17:37.348139Z"}` |


## Updating a product
This endpoint allows the current user to update a product of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/products/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name": "product 2 updated"}` |
| **Request Response**  | `{"id": 2,"company_id": 1,"name": "product 2 updated","units_of_measurement": [{"id": 1,"name": "Displays","is_default": true,"conversion_factor": 1.0,"created": "2019-09-04T02:24:22.156384Z", "modified": "2019-09-04T02:24:22.156384Z"}],"created": "2019-09-04T01:45:02.746274Z","modified": "2019-09-06T00:17:37.348139Z"}` |
