import Transformer
from Get_data_API import Get_APIs


print("example: “Madison, WI” “12345” “Chicago, IL” “10001”")
User_Input = input('Enter your USA City, State or Zipcodes \n')

User_zipcodes = Transformer.find_zipcodes_in_string(User_Input) # string manulation from user input to get zipcodes
User_citystates = Transformer.find_citystate_in_string(User_Input) # string manulation from user input to get city states


for zips in User_zipcodes:
    print(zips)
    response_zipcodes = Get_APIs.get_openweathermap_by_zipcode_API(zips)
    print(response_zipcodes)


for cities in User_citystates:
    print(cities)
    response_citystates = Get_APIs.get_openweathermap_by_citystate_API(cities)
    print(response_citystates)
