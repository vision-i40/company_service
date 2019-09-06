# Turn Scheme

## Adding a turn scheme
This endpoint allows the current user to add a new turn scheme in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name": "new turn scheme"}` |
| **Request Response**  | `{"id": 1, "company_id": 1, "name": "new turn scheme", "modified": "2019-09-05T20:59:45.007494Z"}` |


## Listing the turn schemes
This endpoint allows the current user to list the turn schemes of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 2, "next": null, "previous": null, "results": [ { "id": 2, <...>, "modified": <...> }, { "id": 1, <...> } ]}` |


## Retrieving a turn scheme
This endpoint allows the current user to retrieve a turn scheme of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/2     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 2, "company_id": 1, "name": "turn 2", "modified": "2019-09-05T20:59:45.007494Z" }` |


## Updating a turn scheme
This endpoint allows the current user to update a turn scheme of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name": "turn 2 updated"}` |
| **Request Response**  | `{"id": 2, "company_id": 1, "name": "turn 2 updated", "modified": "2019-09-05T21:14:52.410398Z"}` |
