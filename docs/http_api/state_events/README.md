# State Event

## Adding a state event
This endpoint allows the current user to add a new state event in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"channel_id": 1,"event_datetime": "2019-10-14T11:39:13","state": "On"}` |
| **Request Response**  | `{"id": 3,"channel": {"id": 1,"created": "2019-10-19T13:05:31.579532Z","modified": "2019-10-19T13:05:31.579532Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": true,"discount_waste": true,"stop_on_production_absence": true,"time_to_consider_absence": 20500,"reset_production_changing_order": false,"micro_stop_seconds": null,"in_progress_order": null,"created": "2019-10-17T13:57:50.617464Z","modified": "2019-10-17T13:57:50.617464Z"}` |


## Listing the state events
This endpoint allows the current user to list the state events of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 2,"channel": {"id": 1,"created": "2019-10-19T13:05:31.579532Z","modified": "2019-10-19T13:05:31.579532Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": true,"discount_waste": true,"stop_on_production_absence": true,"time_to_consider_absence": 20500,"reset_production_changing_order": false,"micro_stop_seconds": null,"in_progress_order": null,"created": "2019-10-17T13:57:50.617464Z","modified": "2019-10-17T13:57:50.617464Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-14T11:39:13Z","state": "On","created": "2019-10-19T13:05:34.902009Z","modified": "2019-10-19T13:05:34.902009Z"}]}` |


## Retrieving a state event
This endpoint allows the current user to retrieve a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/3/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 3,"channel": {"id": 1,"created": "2019-10-19T13:05:31.579532Z","modified": "2019-10-19T13:05:31.579532Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": true,"discount_waste": true,"stop_on_production_absence": true,"time_to_consider_absence": 20500,"reset_production_changing_order": false,"micro_stop_seconds": null,"in_progress_order": null,"created": "2019-10-17T13:57:50.617464Z","modified": "2019-10-17T13:57:50.617464Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-14T11:39:13Z","state": "On","created": "2019-10-19T13:23:20.217838Z","modified": "2019-10-19T13:23:20.217838Z"}` |


## Updating a state event
This endpoint allows the current user to update a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/3/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"channel_id": 1,"event_datetime": "2019-10-18T14:59:13","state": "Off"}` |
| **Request Response**  | `{"id": 3,"channel": {"id": 1,"created": "2019-10-19T13:05:31.579532Z","modified": "2019-10-19T13:05:31.579532Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": true,"discount_waste": true,"stop_on_production_absence": true,"time_to_consider_absence": 20500,"reset_production_changing_order": false,"micro_stop_seconds": null,"in_progress_order": null,"created": "2019-10-17T13:57:50.617464Z","modified": "2019-10-17T13:57:50.617464Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-14T11:39:13Z","state": "Off","created": "2019-10-19T13:23:20.217838Z","modified": "2019-10-19T14:33:50.882850Z"}` |

## Deleting a state event
This endpoint allows the current user to delete a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/3/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |