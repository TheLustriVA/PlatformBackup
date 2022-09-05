# This file will contain functions for making sure scraped data is formatted correctly and then written to the appropriate place.

import json
# import csv
# from pathlib import Path

def cache_data(data:list, filename="../data/cache.json"):
    """Write progressive data to a file.
    
    Args:
        data (_dict_): _The data to be written to a file._
        filename (_str_): _The name of the file to be written to._
    """
    with open(filename, "w+", encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def send_data_to_file(data:list, filename:str):
    """Write data to a file.
    
    Args:
        data (_dict_): _The data to be written to a file._
        filename (_str_): _The name of the file to be written to._
    """
    with open(filename, "w+", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
def send_data_to_stdout(data:list):
    """Write data to a file.
    
    Args:
        data (_dict_): _The data to be written to a file._
        filename (_str_): _The name of the file to be written to._
    """
    print(type(data))
    for idx, key, value in enumerate(data.items()):
        print(f"{key} : {value}\n")
        if idx == 5:
            break