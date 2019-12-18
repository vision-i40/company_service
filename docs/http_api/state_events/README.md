# State Event

## Adding a state event
This endpoint allows the current user to add a new state event in his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"stop_code_id": 1, "event_datetime": "2019-10-14T11:39:13","state": "On"}` |
| **Request Response**  | `{"id": 2,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-24T14:15:36.527407Z"}` |


## Listing the state events
This endpoint allows the current user to list the state events of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 2,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-24T14:15:36.527407Z"}]}` |


## Retrieving a state event
This endpoint allows the current user to retrieve a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/2/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 2,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-24T14:15:36.527407Z"}` |


## Updating a state event
This endpoint allows the current user to update a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/2/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"stop_code_id": 1, "event_datetime": "2019-10-20T11:29:13","state": "Off"}` |
| **Request Response**  | `{"id": 2,"stop_code": {"id": 1,"company_id": 1,"is_planned": true,"name": "stop-code 1","code_group": {"id": 1,"company_id": 1,"name": "group-stop","group_type": "StopCode","created": "2019-10-24T12:37:59.404970Z","modified": "2019-10-24T12:37:59.404970Z"},"created": "2019-10-24T12:38:02.640706Z","modified": "2019-10-24T12:38:02.640706Z"},"stop_code_id": 1,"event_datetime": "2019-10-20T11:29:13Z","state": "Off","created": "2019-10-24T14:15:36.527407Z","modified": "2019-10-28T15:02:22.097555Z"}` |

## Deleting a state event
This endpoint allows the current user to delete a state event of his company. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |
