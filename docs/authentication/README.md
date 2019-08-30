# Vision i4.0 - Authentication

The vision authentication works on top of [Django Rest Framwork JWT](https://github.com/davesque/django-rest-framework-simplejwt) with the following endpoints

## Sign In/Token endpoint
The singin endpoint should be use in order to retrieve a token to be used in backend/front-end authentication. It works with the following parameters:

| **Method**            | auth/signin/          |
|-----------------------|:---------------------:|
| **Resources**         | POST                  |
| **Request Payload**   | `{"email": "email@email.com", "passsword": "awesome-hard-pwd"}` |
| **Request Response**  | `{"access": "a.jwt.string","refresh":"a.jwt.string"}` |

## Refresh Token endpoint
When this short-lived access token expires, you can use the longer-lived refresh token to obtain another access token:

| **Method**            | auth/token/refresh/   |
|-----------------------|:---------------------:|
| **Resources**         | POST                  |
| **Request Payload**   | `{"refresh": "<the-refresh-token>"}` |
| **Request Response**  | `{"access": "a.jwt.string"` |


## Authenticated endpoints:

All authenticated endpoints expects the [JWT](https://jwt.io/) token in request header with the following structure:
```
   Authentication: Bearer <THE.JWT.TOKEN>
```

So it is going to authenticate and give access only to the resource which the user has permission. If the request succeeds, the response will be on the 2xx HTTP family depending on the endpoint funcionality, but if it fails due to authentication error it is going to respond with 401 (Unauthorized) HTTP.
