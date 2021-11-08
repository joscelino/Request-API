from .swap_api_consumer import SwapApiConsumer


def test_get_starships():
    """Testing get_startships method"""
    # requests_mock.get(
    #     "https://swapi.dev/api/starships/", status_code=200, json={"some": "thing"}
    # )
    swap_api_consumer = SwapApiConsumer()
    page = 1
    get_starships_response = swap_api_consumer.get_starships(page=page)

    assert get_starships_response.request.method == "GET"
    assert get_starships_response.request.url == "https://swapi.dev/api/starships/"
    assert get_starships_response.request.params == {"page": page}
    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response["results"], list)
