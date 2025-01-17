import pytest


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    result_url = '/api/parse/' + '?address=' + '+'.join(address_string.split())
    result_status = client.get(result_url).status_code
    assert result_status == 200


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'
    result_url = '/api/parse/' + '?address=' + '+'.join(address_string.split())
    result_status = client.get(result_url).status_code
    assert result_status == 400
