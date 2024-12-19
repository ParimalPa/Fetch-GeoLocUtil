import requests

base_url = "http://api.openweathermap.org/geo/1.0/"
API_key = "f897a99d971b5eef57be6fafa0d83239" #Fetch's API Key #API keys should be taken from a keyvault instead of being hardcoded. :-( 
#"9518d69092b66fb062a842773319be22" #Parimal's API Key 
#"f897a99d971b5eef57be6fafa0d83239" #provided by Fetch

class Get_APIs():

    def get_openweathermap_by_citystate_API (input_citystate):
        response = requests.get(f"{base_url}direct?q={input_citystate},US&limit=1&appid={API_key}")
        return response.json()

    def get_openweathermap_by_zipcode_API (input_zipcode):
        response = requests.get(f"{base_url}zip?zip={input_zipcode},US&appid={API_key}")
        return response.json()
