# -*- coding: utf-8 -*-
"""
Name: Alexander Petralia
Project: NASA API
"""


import requests
import pytest
import poetry
from bs4 import BeautifulSoup
import pprint
import json
from datetime import datetime
import calendar





  
"""
# the file to be converted to 
# json format
filename = 'asteroid_data_2.txt'
  
# dictionary where the lines from
# text will be stored
dict1 = {}
  
# creating dictionary
with open(filename) as fh:
  
    for line in fh:
  
        # reads each line and trims of extra the spaces 
        # and gives only the valid words
        command, description = line.strip().split(None, 1)
  
        dict1[command] = description.strip()
  
# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()



print(dict1)
"""













"""
NOTES:
============================================================================
#What is our API Key?
api_key=DEMO_KEY


#whats our endpoint (or a url)
https://api.nasa.gov/neo/rest/v1/neo/browse


#what is the HTTP method that we need?
ENDPOINT
GET
/neo/{id}


endpoint with GET method
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


#============================Functions=====================================
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
    
    
    



#Function prints all closest asteroid approaches in the given/current month
#example query = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-12-01&end_date=2021-12-31&api_key=DEMO_KEY'
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
            

def nearest_misses():
    #Setup HTTP Request
    
    """
    Tree Structure for nearest_miss data:
        Level 0: blank
        Level 1: "close_approach_data"
        Level 2: "miss_distance"
        Level 3: "miles"
    =>
    Find Top 10 Results using min("miles")
    """
    
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
    
    for asteroid in asteroid_list:
        print(pprint.pformat(asteroid['close_approach_data']))
    
    
    """
    Failed Attempts and Notes for nearest_misses() function
    ===================================================================
    
    #GOAL: SORT by 'miles' = asteroid_list['miss_distance']['miles']
    
    
    #Attempt 1: trying to sort by 'miles', couldn't find way to iterate over the 'miss_distance' dictionary
    ================================================
    final = asteroid_list.sort(key =lambda k: k['close_approach_data']['miss_distance']['miles'], reverse=True)
    #print(final)
    
    #Attempt 2: Iterate over each asteroid, get the attributes and values, append to new json object by sorting
    ================================================
    for asteroid in asteroid_list:
        for attribute,value in asteroid.items():
            print(attribute,value)
    sorted_json = sorted(asteroid_list, key=lambda d: d['close_approach_data'])
    #print(sorted_json)
    
    
    """
    
    
#============================Execution=====================================
#asteroid_closest_approach()
#month_closest_approaches()
#nearest_misses()
#==========================================================================





    













