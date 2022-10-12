import configparser
import requests
import os
# from test_api_2gis.tools.LoggerError import LoggerError


class ApiHipo:
    parser = configparser.ConfigParser()
    parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'config.ini'))

    BASE_URL = parser.get('hipo', 'basic_url')
    SEARCH = BASE_URL + "/search"

    @staticmethod
    def get_search(headers, **args):
        url = ApiHipo.SEARCH
        headers = headers
        params = args
        result = requests.request("GET", url, headers=headers, params=params)

        # LoggerError.logging_error(result)

        return result