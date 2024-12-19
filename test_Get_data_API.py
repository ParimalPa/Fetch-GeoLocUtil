import requests
import unittest
from unittest.mock import patch, Mock
from Get_data_API import Get_APIs


base_url = "http://api.openweathermap.org/geo/1.0/"

API_key = "f897a99d971b5eef57be6fafa0d83239" #Parimal's API Key #API keys should be taken from a keyvault instead of being hardcoded. :-( 
#"9518d69092b66fb062a842773319be22" #Parimal's API Key 
#"f897a99d971b5eef57be6fafa0d83239" #provided by Fetch

input_citystate = 'des plaines, il'
input_zipcode = "60056"

url_citystate = f"{base_url}direct?q={input_citystate},US&limit=1&appid={API_key}"
url_zip = f"{base_url}zip?zip={input_zipcode},US&appid={API_key}"


def test_can_call_endpoints(): #Test if the actual endpoint is working, connectivity, dependancy online and is unchanged
    response = requests.get(url_citystate)
    assert response.status_code == 200
    response2 = requests.get(url_zip)
    assert response2.status_code == 200


class TestAPIbyMockData(unittest.TestCase): #mocking the 2 API endpoints, so that even if dependancy is down we can iterate based on expectations

    @patch('requests.get')
    def test_get_citystate_API(self, mock_get): 
        mock_response = Mock()
        response_dict = {'name' : 'Des Plaines', 'lat': 42.0415823, 'lon': -87.8873916, 'country': 'US', 'state': 'Illinois'}
        mock_response.json.return_value = response_dict
        mock_get.return_value = mock_response

        user_input = Get_APIs.get_openweathermap_by_citystate_API("des plaines, il")
        
        mock_get.assert_called_with("http://api.openweathermap.org/geo/1.0/direct?q=des plaines, il,US&limit=1&appid="+API_key)
        self.assertEqual(user_input, response_dict)

    @patch('requests.get')
    def test_get_zipcode_API(self, mock_getzip): 
        mock_response = Mock()
        response_dict = {"zip":"60056", "name":"Mount Prospect", "lat":42.0624, "lon":-87.9377, "country":"US"}
        mock_response.json.return_value = response_dict

        mock_getzip.return_value = mock_response

        user_input = Get_APIs.get_openweathermap_by_zipcode_API("60056")
        
        mock_getzip.assert_called_with("http://api.openweathermap.org/geo/1.0/zip?zip=60056,US&appid="+API_key)
        self.assertEqual(user_input, response_dict)
