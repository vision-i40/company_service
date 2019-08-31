# Vision i4.0 - Authentication

## Get current user information
This endpoints provide current user information and its default company. **This route is authenticated**.

| **Method**            | auth/signin/          |
|-----------------------|:---------------------:|
| **Resources**         | GET                   |
| **Request Response**  | `{"id": 1,"name":"A Name","email":"email@email.com","default_company":{"id": 1,"trade_name":"Corp. Name","slug":"a-slug"<...>}, <...>}` |
