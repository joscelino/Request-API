from src.errors import HttpRequestError

from .swap_api_consumer import SwapApiConsumer


def test_get_starships(requests_mock):
    """Testing get_startships method"""
    requests_mock.get(
        "https://swapi.dev/api/starships/",
        status_code=200,
        json={"some": "thing", "results": [{}]},
    )
    swap_api_consumer = SwapApiConsumer()
    page = 1
    get_starships_response = swap_api_consumer.get_starships(page=page)

    assert get_starships_response.request.method == "GET"
    assert get_starships_response.request.url == "https://swapi.dev/api/starships/"
    assert get_starships_response.request.params == {"page": page}
    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response["results"], list)


def test_get_starships_httperror(requests_mock):
    """Testing error in get_startships method"""

    requests_mock.get(
        "https://swapi.dev/api/starships/",
        status_code=404,
        json={"detail": "something"},
    )
    swap_api_consumer = SwapApiConsumer()
    page = 1000

    try:
        swap_api_consumer.get_starships(page=page)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
        # print(error.message)
        # print(error.status_code)
        # print(type(error))
