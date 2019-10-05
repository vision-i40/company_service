# Channel

## Adding a Channel
This endpoint allows the current user to add a new channel in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/1/channels/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"number": 23,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line_id": 1,"collector_id": 1}` |
| **Request Response**  | `{"id": 2,"created": "2019-09-18T12:24:53.660401Z","modified": "2019-09-18T12:24:53.660401Z","number": 23,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": false,"time_to_consider_absence": null,"reset_production_changing_order": false,"micro_stop_seconds": null,"created": "2019-09-18T12:23:17.246490Z","modified": "2019-09-18T12:23:17.246490Z"},"production_line_id": 1,"collector_id": 1}` |


## Listing the Channels
This endpoint allows the current user to list the channels of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/1/channels/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 2,"created": "2019-09-18T12:24:53.660401Z","modified": "2019-09-18T12:24:53.660401Z","number": 23,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": false,"time_to_consider_absence": null,"reset_production_changing_order": false,"micro_stop_seconds": null,"created": "2019-09-18T12:23:17.246490Z","modified": "2019-09-18T12:23:17.246490Z"},"production_line_id": 1,"collector_id": 1}]}` |


## Retrieving a Channel
This endpoint allows the current user to retrieve a channel of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | /v1/companies/1/collectors/1/channels/2/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 2,"created": "2019-09-18T12:24:53.660401Z","modified": "2019-09-18T12:24:53.660401Z","number": 23,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": false,"time_to_consider_absence": null,"reset_production_changing_order": false,"micro_stop_seconds": null,"created": "2019-09-18T12:23:17.246490Z","modified": "2019-09-18T12:23:17.246490Z"},"production_line_id": 1,"collector_id": 1}` |


## Updating a Channel
This endpoint allows the current user to update a channel of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/1/channels/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"number": 22,"channel_type": "Rework","inverse_state": true,"is_cumulative": true,"production_line_id": 1,"collector_id": 1}` |
| **Request Response**  | `{"id": 2,"created": "2019-09-18T12:24:53.660401Z","modified": "2019-09-20T14:11:48.561422Z","number": 22,"channel_type": "Rework","inverse_state": true,"is_cumulative": true,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": false,"time_to_consider_absence": null,"reset_production_changing_order": false,"micro_stop_seconds": null,"created": "2019-09-18T12:23:17.246490Z","modified": "2019-09-18T12:23:17.246490Z"},"production_line_id": 1,"collector_id": 1}` |

## Deleting a Channel
This endpoint allows the current user to delete a channel of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/collectors/2/channels/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |