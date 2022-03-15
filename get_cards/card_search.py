import requests
import itertools
api_url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'


def response_to_list(resp: dict) -> list:
    # This function returns a list of all cards
    response_values = resp.values()
    flat_list = list(itertools.chain.from_iterable(response_values))
    return flat_list


def search_all() -> list:
    # This function will get all cards from the API in JSON format.
    api_call_results = requests.get(api_url).json()
    return response_to_list(api_call_results)
