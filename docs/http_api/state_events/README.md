# State Event

## Adding a state event
This endpoint allows the current user to add a new state event in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"channel_id": null, "stop_code_id": 1, ""event_datetime": "2019-10-14T11:39:13","state": "On"}` |
| **Request Response**  | `{"id": 2,"channel": null,"channel_id": null,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-24T14:15:36.527407Z"}` |


## Listing the state events
This endpoint allows the current user to list the state events of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 2,"channel": null,"channel_id": null,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-24T14:15:36.527407Z"}]}` |


## Retrieving a state event
This endpoint allows the current user to retrieve a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/2/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 2,"channel": null,"channel_id": null,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-24T14:15:36.527407Z"}` |


## Updating a state event
This endpoint allows the current user to update a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"channel_id": 1,"stop_code_id": 1, "event_datetime": "2019-10-20T11:29:13","state": "Off"}` |
| **Request Response**  | `{"id": 2,"channel": {"id": 1,"created": "2019-10-28T15:02:08.899685Z","modified": "2019-10-28T15:02:08.899685Z","number": 16,"channel_type": "Good","inverse_state": true,"is_cumulative": false,"production_line": {"id": 1,"company_id": 1,"name": "production-line-1","is_active": true,"discount_rework": true,"discount_waste": true,"stop_on_production_absence": true,"time_to_consider_absence": 10500,"reset_production_changing_order": false,"micro_stop_seconds": 20000,"in_progress_order": null,"turn": {"id": 1,"turn_scheme_id": 1,"name": "turn test","start_time": "06:00:00","end_time": "14:00:00","days_of_week": [1,2,3,4,5],"created": "2019-10-24T12:35:09.548556Z","modified": "2019-10-24T12:35:09.548556Z"},"created": "2019-10-24T12:35:12.095341Z","modified": "2019-10-24T12:35:12.095341Z"},"production_line_id": 1},"channel_id": 1,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-28T15:02:22.097555Z"}` |

## Deleting a state event
This endpoint allows the current user to delete a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |