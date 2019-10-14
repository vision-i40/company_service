# State Event

## Adding a state event
This endpoint allows the current user to add a new state event in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_orders/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"production_line_id": 1,"channel_id": 1,"event_datetime": "2019-10-14T11:39:13","state": "On"}` |
| **Request Response**  | `{"id": 4,"production_line_id": 1,"channel": {"id": 1,"created": "2019-10-14T15:41:57.215989Z","modified": "2019-10-14T15:41:57.215989Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10000,"in_progress_order": null,"created": "2019-10-14T12:43:06.464893Z","modified": "2019-10-14T12:43:06.464893Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-14T11:39:13Z","state": "On","created": "2019-10-14T20:53:20.440518Z","modified": "2019-10-14T20:53:20.440518Z"}` |


## Listing the state events
This endpoint allows the current user to list the state events of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_orders/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 4,"production_line_id": 1,"channel": {"id": 1,"created": "2019-10-14T15:41:57.215989Z","modified": "2019-10-14T15:41:57.215989Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10000,"in_progress_order": null,"created": "2019-10-14T12:43:06.464893Z","modified": "2019-10-14T12:43:06.464893Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-14T11:39:13Z","state": "On","created": "2019-10-14T20:53:20.440518Z","modified": "2019-10-14T20:53:20.440518Z"}]}` |


## Retrieving a state event
This endpoint allows the current user to retrieve a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_orders/1/state_events/4/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 4,"production_line_id": 1,"channel": {"id": 1,"created": "2019-10-14T15:41:57.215989Z","modified": "2019-10-14T15:41:57.215989Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10000,"in_progress_order": null,"created": "2019-10-14T12:43:06.464893Z","modified": "2019-10-14T12:43:06.464893Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-14T11:39:13Z","state": "On","created": "2019-10-14T20:53:20.440518Z","modified": "2019-10-14T20:53:20.440518Z"}` |


## Updating a state event
This endpoint allows the current user to update a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_orders/1/state_events/4/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"production_line_id": 2,"channel_id": 1,"event_datetime": "2019-10-18T14:59:13","state": "On"}` |
| **Request Response**  | `{"id": 4,"production_line_id": 2,"channel": {"id": 1,"created": "2019-10-14T15:41:57.215989Z","modified": "2019-10-14T15:41:57.215989Z","number": 16,"channel_type": "Good","inverse_state": false,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": false,"discount_waste": false,"stop_on_production_absence": true,"time_to_consider_absence": 20000,"reset_production_changing_order": false,"micro_stop_seconds": 10000,"in_progress_order": null,"created": "2019-10-14T12:43:06.464893Z","modified": "2019-10-14T12:43:06.464893Z"},"production_line_id": 1},"channel_id": 1,"event_datetime": "2019-10-18T14:59:13Z","state": "On","created": "2019-10-14T20:53:20.440518Z","modified": "2019-10-14T21:14:50.896631Z"}` |

## Deleting a state event
This endpoint allows the current user to delete a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_orders/1/state_events/4/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |