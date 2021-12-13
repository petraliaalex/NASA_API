# -*- coding: utf-8 -*-
"""
Name: Alexander Petralia
Project: NASA API
"""


import requests
import pytest
import poetry
import pprint
from datetime import datetime
import calendar


"""
NOTES:
============================================================================
#What is our API Key?
api_key=DEMO_KEY


#What is our endpoint (or a url)
https://api.nasa.gov/neo/rest/v1/neo/browse


#What is the HTTP method that we need?
ENDPOINT
GET
/neo/{id}


Endpoint with GET method
=> https://api.nasa.gov/neo/rest/v1/neo/browse/neo/{id}?api_key=DEMO_KEY
============================================================================
"""


#===============================HTTP Request Setup=========================

api_base_url = "https://api.nasa.gov/neo/rest/v1"
neo_id = "browse"
api_key = "?api_key=DEMO_KEY"
endpoint_path = f"/neo/{neo_id}"
endpoint = f"{api_base_url}{endpoint_path}{api_key}"

#==========================================================================



#============================Print Methods for Testing=====================
#print(endpoint)
#print(r.status_code)
#print(r.text)
#with open('asteroid_data_1.txt', 'w') as output:
#    output.write(pprint.pformat(r.json()))
#==========================================================================



#============================Function 1=====================================
"""
This function should return JSON data that includes each asteroid and its closest 
approach to Earth
"""
def asteroid_closest_approach():
    #Setup HTTP Request
    api_base_url = "https://api.nasa.gov/neo/rest/v1"
    neo_id = "browse"
    api_key = "?api_key=DEMO_KEY"
    
    #Execute HTTP Request
    endpoint_path = f"/neo/{neo_id}"
    endpoint = f"{api_base_url}{endpoint_path}{api_key}"
    r = requests.get(endpoint)
    print(pprint.pformat(r.json()))
#==========================================================================
    

    
#============================Function 2=====================================
"""
This function should return JSON data that includes all the closest asteroid approaches 
in a given calendar month, including a total element_count for the month. 
Please keep in mind that the endpoint is only able to return 7 days of data at a time.

#Function prints all closest asteroid approaches in the given/current month
#example query = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-12-01&end_date=2021-12-31&api_key=DEMO_KEY'
"""
def month_closest_approaches():
    #Setup HTTP Request
    api_base_url = 'https://api.nasa.gov/neo/rest/v1/'
    neo_id = "feed?"
    api_key = "&api_key=DEMO_KEY"
    
    #Execute HTTP Request
    #iterate through i weeks for each HTTP Request
    for i in range(0,3):       
        start_day_num = 0
        end_day_num = 0
        if i == 3:
            start_date_key = str(datetime.now().year) + "-" + str(datetime.now().month) + "-25"
            end_date_key =   str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(calendar.monthrange(datetime.now().year, datetime.now().month)[1])
            endpoint_path = f"start_date={start_date_key}&end_date={end_date_key}"
            endpoint = f"{api_base_url}{neo_id}{endpoint_path}{api_key}"
            r = requests.get(endpoint)
            print(pprint.pformat(r.json()))
            #with open('asteroid_data_2.txt', 'w') as output:
            #    output.write(pprint.pformat(r.json()))
        else:
            start_day_num = 1 + (7 * i)    #tracks the next start day number based on week i
            end_day_num = 8 + (7 * i)      #tracks the next end   day number based on week i
            start_date_key = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(start_day_num)
            end_date_key =   str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(end_day_num)
            endpoint_path = f"start_date={start_date_key}&end_date={end_date_key}"
            endpoint = f"{api_base_url}{neo_id}{endpoint_path}{api_key}"
            r = requests.get(endpoint)
            print(pprint.pformat(r.json()))
            #with open('asteroid_data_2.txt', 'w') as output:
            #    output.write(pprint.pformat(r.json()))
#==========================================================================      



#===========================Function 3=====================================
"""
This function should return JSON data that includes the 10 nearest misses, 
historical or expected, of asteroids impacting Earth.


Tree Structure for nearest_miss_data:
    Level 0: "near_earth_objects"
    Level 1: "close_approach_data"
    Level 2: "miss_distance"
    Level 3: "miles"
=>
Find Top 10 Results using min("miles")
"""
def nearest_misses():
    
    #Setup HTTP Request
    api_base_url = "https://api.nasa.gov/neo/rest/v1"
    neo_id = "browse"
    api_key = "?api_key=DEMO_KEY"
    
    
    #Execute HTTP Request
    endpoint_path = f"/neo/{neo_id}"
    endpoint = f"{api_base_url}{endpoint_path}{api_key}"
    r = requests.get(endpoint)
    json_data = r.json()
    asteroid_list = json_data['near_earth_objects']
    
    #Setup Lists and Dictionaries
    miles_dict = {}
    asteroid_dict = {}
    sorted_id_list = []
    
    #Save the asteroid_id, miles and related data into the dictionaries
    for asteroid in asteroid_list:
        #asteroid = contains all needed data for each asteroid
        asteroid_id = str(asteroid['id'])
        asteroid_miles = str(asteroid['close_approach_data'][3]['miss_distance']['miles'])
        miles_dict.update({asteroid_id: asteroid_miles})
        asteroid_dict.update({asteroid_id: asteroid})
        
    #sorts the asteroid_id with its given miss_distance in miles (descending)
    sorted_miles_dict = {k: v for k, v in sorted(miles_dict.items(), key=lambda item: item[1])}
    
    #stores the sorted asteroid_ids in sorted_id_list
    for items in sorted_miles_dict:
        print(pprint.pformat(items))
        sorted_id_list.append(items)
        
    #prints the asteroid record using asteroid_id in sorted order for a TOP 10
    for i in range(0,9):
        cur_id = sorted_id_list[i]
        print(pprint.pformat(asteroid_dict[cur_id]))
    
    #Testing
    #print(pprint.pformat(json_data))
    #print(type(json_data))
    #print(type(asteroid_list))
#==========================================================================
    
    
    
#============================Execution=====================================
#asteroid_closest_approach()
#month_closest_approaches()
#nearest_misses()
#==========================================================================





    













