# Turn

## Adding a turn
This endpoint allows the current user to add a new turn in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/1/turns/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name" : "turn test 2", "start_time": "08:12:12", "end_time": "12:13:15", "days_of_week": [1, 2, 3, 4]}` |
| **Request Response**  | `{"id": 4, "turn_scheme_id": 1, "name": "turn test 2", "start_time": "08:12:12", "end_time": "12:13:15", "days_of_week": [ 1, 2, 3, 4 ], "created": "2019-09-07T12:10:29.581614Z", "modified": "2019-09-07T12:10:29.581614Z"}` |


## Listing the turns
This endpoint allows the current user to list the turns of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/2/turns/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 2, "next": null, "previous": null, "results": [ {"id": 4,"turn_scheme_id": 2,"name": "turn test 2",<...> }, {"id": 1, "turn_scheme_id": 2 <...>}]}` |


## Retrieving a turn
This endpoint allows the current user to retrieve a turn of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/2/turns/1     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "id": 1, "turn_scheme_id": 2, "name": "manha", "start_time": "11:48:58", "end_time": "18:00:00", "days_of_week": [ 1, 2, 3 ], "created": "2019-09-07T11:49:29.441922Z", "modified": "2019-09-07T11:49:29.441922Z"}` |


## Updating a turn
This endpoint allows the current user to update a turn of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/1/turns/2     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name" : "turn test 2 - updated", "start_time": "09:12:12", "end_time": "12:13:15", "days_of_week": [1, 2]}` |
| **Request Response**  | `{"id": 2, "company_id": 1, "name": "turn 2 updated", "modified": "2019-09-05T21:14:52.410398Z"}` |


## Deleting a Turn
This endpoint allows the current user to delete a turn of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/turn_schemes/2/turns/3/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |
