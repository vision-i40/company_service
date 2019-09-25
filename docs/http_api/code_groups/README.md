# Code Groups

## Adding a Code Group
This endpoint allows the current user to add a new code group in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name" : "code group 1", "group_type": ReworkCode}` |
| **Request Response**  | `{"id": 1,"company_id": 1,"name": "code group 1","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T12:24:15.822692Z"}` |


## Listing the Code Groups
This endpoint allows the current user to list the code groups of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "count": 1,"next": null,"previous": null,"results": [{"id": 1,"company_id": 1,"name": "code group 1","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T12:24:15.822692Z"}]}` |


## Retrieving a Code Group
This endpoint allows the current user to retrieve a code group of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "id": 1,"company_id": 1,"name": "code group 1","group_type": "ReworkCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T12:24:15.822692Z"}` |


## Updating a Code Group
This endpoint allows the current user to update a code group of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name" : "code group 2", "group_type": WasteCode}` |
| **Request Response**  | `{"id": 1,"company_id": 1,"name": "code group 2","group_type": "WasteCode","created": "2019-09-25T12:24:15.822692Z","modified": "2019-09-25T15:09:16.377670Z"}` |

## Deleting a Code Group
This endpoint allows the current user to delete a code group of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/1/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |