# Production Line

## Adding a production line
This endpoint allows the current user to add a new product in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"name": "production-line-2","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_abscence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10012}` |
| **Request Response**  | `{"id": 4,"company_id": 1,"name": "production-line-2","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_abscence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10012, "created": "2019-09-07T13:30:13.947539Z", "modified": "2019-09-07T13:30:13.947539Z"}` |


## Listing the production lines
This endpoint allows the current user to list the production lines of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1, "next": null, "previous": null, "results": [ {"id": 2,"company_id": 1,"name": "a new nice product name","units_of_measurement": [{"id": 4,"company_id": 1,"name": "production-line-2","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_abscence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10012, "created": "2019-09-07T13:30:13.947539Z", "modified": "2019-09-07T13:30:13.947539Z"}, { "id": 1, <...> } ]}` |


## Retrieving a production line
This endpoint allows the current user to retrieve a production line of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/2     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 4,"company_id": 1,"name": "production-line-2","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_abscence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10012, "created": "2019-09-07T13:30:13.947539Z", "modified": "2019-09-07T13:30:13.947539Z"}` |


## Updating a production line
This endpoint allows the current user to update a production line of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"name": "production-line-2 updated","is_active": false,"discount_rework": false,"discount_waste": false,"stop_on_production_abscence": false,"time_to_consider_absence": 666,"reset_production_changing_order": false,"micro_stop_seconds": 333}` |
| **Request Response**  | `{"id": 4,"company_id": 1,"name": "production-line-2 updated","is_active": false,"discount_rework": false,"discount_waste": false,"stop_on_production_abscence": false,"time_to_consider_absence": 666,"reset_production_changing_order": false,"micro_stop_seconds": 333, "created": "2019-09-07T13:30:13.947539Z", "modified": "2019-09-07T13:30:13.947539Z"}` |

## Deleting a production line
This endpoint allows the current user to delete a production line of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |
