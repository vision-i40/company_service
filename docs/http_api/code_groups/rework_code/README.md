# Rework Code

## Adding a Rework Code
This endpoint allows the current user to add a new rework code in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/rework_codes/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name" : "rework-1"}` |
| **Request Response**  | `{"id": 1,"company_id": 1,"name": "rework-1","code_group": {"id": 1,"company_id": 1,"name": "code group 2","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T15:09:16.377670Z"},"created": "2019-09-25T12:24:17.825190Z","modified": "2019-09-25T12:24:17.825190Z"}` |


## Listing the Rework Codes
This endpoint allows the current user to list the rework codes of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/rework_codes/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "count": 1,"next": null,"previous": null,"results": [{"id": 1,"company_id": 1,"name": "rework-1","code_group": {"id": 1,"company_id": 1,"name": "code group 2","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T15:09:16.377670Z"},"created": "2019-09-25T12:24:17.825190Z","modified": "2019-09-25T12:24:17.825190Z"}]}` |


## Retrieving a Rework Code
This endpoint allows the current user to retrieve a rework code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/rework_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "id": 1,"company_id": 1,"name": "code group 1","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T12:24:15.822692Z"}` |


## Updating a Rework Code
This endpoint allows the current user to update a rework code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/rework_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name" : "rework-2"}` |
| **Request Response**  | `{ "id": 1,"company_id": 1,"name": "rework-2","code_group": {"id": 1,"company_id": 1,"name": "code group 2","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T15:19:56.765654Z"},"created": "2019-09-25T12:24:17.825190Z","modified": "2019-09-25T15:19:43.891887Z"}` |

## Deleting a Rework Code
This endpoint allows the current user to delete a rework code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/rework_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |