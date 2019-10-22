# Manual Stop

## Adding a manual stop
This endpoint allows the current user to make a manual stop on the production line. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/1/manual_stops/     |
|-----------------------|:---------------------:|
| **Resources**         | POST                   |
| **Request Payload**   | `{"stop_code_id": "1","start_datetime": "2019-10-21T12:24:14.762826Z","end_datetime: "2019-10-23T12:24:14.762826Z"}` |
| **Request Response**  | `{"id": 3,"state_event": [{"start_datetime": "2019-10-21T12:24:14.762826Z","stop_code": "stop-code 1","state": "Off"},{"end_datetime": "2019-10-23T12:24:14.762826Z","stop_code": "stop-code 1","state": "Off"}],"created": "2019-10-21T20:28:06.699344Z","modified": "2019-10-21T20:28:06.699344Z"}` |


## Listing the manual stops
This endpoint allows the current user to list the manual stops of the production line. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/1/manual_stops/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"count": 1,"next": null,"previous": null,"results": [{"id": 3,"state_event": [{"start_datetime": "2019-10-21T12:24:14.762826Z","stop_code": "stop-code 1","state": "Off"},{"end_datetime": "2019-10-23T12:24:14.762826Z","stop_code": "stop-code 1","state": "Off"}],"created": "2019-10-21T20:28:06.699344Z","modified": "2019-10-21T20:28:06.699344Z"}}, { "id": 1, <...> } ]}` |


## Retrieving a manual stop
This endpoint allows the current user to retrieve a manual stop of the production line. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/1/manual_stops/3/     |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 3,"state_event": [{"start_datetime": "2019-10-21T12:24:14.762826Z","stop_code": "stop-code 1","state": "Off"},{"end_datetime": "2019-10-23T12:24:14.762826Z","stop_code": "stop-code 1","state": "Off"}],"created": "2019-10-21T20:28:06.699344Z","modified": "2019-10-21T20:28:06.699344Z"}` |


## Updating a manual stop
This endpoint allows the current user to update a manual stop of the production line. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/1/state_events/1/manual_stops/3/     |
|-----------------------|:---------------------:|
| **Resources**         | PUT                   |
| **Request Payload**   | `{"stop_code_id": "2","start_datetime": "2019-10-25T18:34:14.762826Z","end_datetime: "2019-10-26T00:04:14.762826Z"}` |
| **Request Response**  | `{"id": 3,"state_event": [{"start_datetime": "2019-10-25T18:34:14.762826Z","stop_code": "stop-code 2","state": "Off"},{"end_datetime": "2019-10-26T00:04:14.762826Z","stop_code": "stop-code 2","state": "Off"}],"created": "2019-10-21T20:28:06.699344Z","modified": "2019-10-22T13:08:05.184167Z"}` |

## Deleting a manual stop
This endpoint allows the current user to delete a manual stop of the production line. [This route is authenticated](https://github.com/vision-i40/company_service/tree/master/docs/authentication#authenticated-endpoints).

| **Method**            | v1/companies/1/production_lines/2/     |
|-----------------------|:---------------------:|
| **Resources**         | DELETE                   |