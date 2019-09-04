from rest_framework.test import APIRequestFactory
import json


def assert_unauthorized_with_no_token(testInstance, route, method='get', resource='list', pk=None, companies_pk=None):
    view = testInstance.view.as_view({method: resource})
    factory = APIRequestFactory()

    request = factory.get(route)
    response = view(request, pk=pk, companies_pk=companies_pk)

    testInstance.assertEqual(response.status_code, 401)
    response.render()
    response_dict = json.loads(response.content.decode('utf-8'))
    testInstance.assertTrue("credentials were not provided" in response_dict['detail'])


def assert_unauthorized_with_invalid_token(testInstance, route, method='get', resource='list', pk=None,
                                           companies_pk=None):
    view = testInstance.view.as_view({method: resource})
    factory = APIRequestFactory()

    request = factory.get(route, HTTP_AUTHORIZATION='Bearer invalid.token')
    response = view(request, pk=pk, companies_pk=companies_pk)

    testInstance.assertEqual(response.status_code, 401)
    response.render()
    response_dict = json.loads(response.content.decode('utf-8'))
    testInstance.assertTrue("Given token not valid" in response_dict['detail'])


def assert_unauthorized_with_unactivated_user(testInstance, route, unactivatedToken, method='get', resource='list', pk=None,
                                           companies_pk=None):
    view = testInstance.view.as_view({method: resource})
    factory = APIRequestFactory()

    request = factory.get(route, HTTP_AUTHORIZATION='Bearer {}'.format(unactivatedToken))
    response = view(request, pk=pk, companies_pk=companies_pk)

    testInstance.assertEqual(response.status_code, 401)
    response.render()
    response_dict = json.loads(response.content.decode('utf-8'))
    testInstance.assertTrue("User is inactive" in response_dict['detail'])

