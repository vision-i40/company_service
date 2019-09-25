# Stop Code

## Adding a Stop Code
This endpoint allows the current user to add a new Stop Code in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/3/stop_codes/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name" : "stop-code 1", "is_planned": "true"}` |
| **Request Response**  | `{"id": 2,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 3,"company_id": 1,"name": "code group 3","group_type": "StopCode","created": "2019-09-25T15:30:02.413156Z","modified": "2019-09-25T15:30:02.413156Z"},"created": "2019-09-25T15:31:50.297578Z","modified": "2019-09-25T15:31:50.297578Z"}` |


## Listing the Stop Codes
This endpoint allows the current user to list the Stop Codes of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/3/stop_codes/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "count": 1,"next": null,"previous": null,"results": [{"id": 2,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 3,"company_id": 1,"name": "code group 3","group_type": "StopCode","created": "2019-09-25T15:30:02.413156Z","modified": "2019-09-25T15:30:02.413156Z"},"created": "2019-09-25T15:31:50.297578Z","modified": "2019-09-25T15:31:50.297578Z"}]}` |


## Retrieving a Stop Code
This endpoint allows the current user to retrieve a Stop Code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/3/stop_codes/2/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "id": 2,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 3,"company_id": 1,"name": "code group 3","group_type": "StopCode","created": "2019-09-25T15:30:02.413156Z","modified": "2019-09-25T15:30:02.413156Z"},"created": "2019-09-25T15:31:50.297578Z","modified": "2019-09-25T15:31:50.297578Z"}` |


## Updating a Stop Code
This endpoint allows the current user to update a Stop Code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/2/waste_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name" : "stop-code 2", "is_planned" : "false"}` |
| **Request Response**  | `{ "id": 2,"company_id": 1,"is_planned": false,"name": "stop-code 2","code_group": {"id": 3,"company_id": 1,"name": "code group 3","group_type": "StopCode","created": "2019-09-25T15:30:02.413156Z","modified": "2019-09-25T15:30:02.413156Z"},"created": "2019-09-25T15:31:50.297578Z","modified": "2019-09-25T15:44:08.135159Z"}` |

## Deleting a Stop Code
This endpoint allows the current user to delete a Stop Code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/3/stop_codes/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |