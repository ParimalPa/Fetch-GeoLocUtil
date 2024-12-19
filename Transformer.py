# This is where that will take input as a string provided by the user and transform it to the appropreate format for the api 
#   Transformations include  multiple inputs
# Parsing for city, state or zip code 

import re

def find_zipcodes_in_string(input_data):  #function to find zip codes within inputed string
    return re.findall(r'\d+', input_data)

def find_citystate_in_string(input_data):  #function to find city and state within inputed string
    return re.findall(r'\w+[a-z,A-Z], \w+', input_data)


