# Waste Code

## Adding a Waste Code
This endpoint allows the current user to add a new Waste Code in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/2/waste_codes/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name" : "waste-code 1"}` |
| **Request Response**  | `{"id": 1,"company_id": 1,"name": "waste-code 1","code_group": {"id": 2,"company_id": 1,"name": "code group 2","group_type": "WasteCode","created": "2019-09-25T12:28:31.854536Z","modified": "2019-09-25T15:23:02.208469Z"},"created": "2019-09-25T12:28:33.257915Z","modified": "2019-09-25T12:28:33.257915Z"}` |


## Listing the Waste Codes
This endpoint allows the current user to list the Waste Codes of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/2/waste_codes/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "count": 1,"next": null,"previous": null,"results": [{"id": 1,"company_id": 1,"name": "waste-code 1","code_group": {"id": 2,"company_id": 1,"name": "code group 2","group_type": "WasteCode","created": "2019-09-25T12:28:31.854536Z","modified": "2019-09-25T15:23:02.208469Z"},"created": "2019-09-25T12:28:33.257915Z","modified": "2019-09-25T12:28:33.257915Z"}]}` |


## Retrieving a Waste Code
This endpoint allows the current user to retrieve a Waste Code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/2/waste_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{ "id": 1,"company_id": 1,"name": "waste-code 1","code_group": {"id": 2,"company_id": 1,"name": "code group 2","group_type": "WasteCode","created": "2019-09-25T12:28:31.854536Z","modified": "2019-09-25T15:23:02.208469Z"},"created": "2019-09-25T12:28:33.257915Z","modified": "2019-09-25T12:28:33.257915Z"}` |


## Updating a Waste Code
This endpoint allows the current user to update a Waste Code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/2/waste_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name" : "waste-code 2"}` |
| **Request Response**  | `{ "id": 1,"company_id": 1,"name": "waste-code 2","code_group": {"id": 2,"company_id": 1,"name": "code group 2","group_type": "WasteCode","created": "2019-09-25T12:28:31.854536Z","modified": "2019-09-25T15:23:02.208469Z"},"created": "2019-09-25T12:28:33.257915Z","modified": "2019-09-25T15:28:36.330799Z"}` |

## Deleting a Waste Code
This endpoint allows the current user to delete a Waste Code of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/code_groups/2/waste_codes/1/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |