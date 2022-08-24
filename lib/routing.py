# This file will contain functions for making sure scraped data is formatted correctly and then written to the appropriate place.

import json
# import csv
# from pathlib import Path

def send_data_to_file(data:dict, filename:str):
    """Write data to a file.
    
    Args:
        data (_dict_): _The data to be written to a file._
        filename (_str_): _The name of the file to be written to._
    """
    with open(filename, "w+", encoding='utf-8') as f:
        json.dump(data, f, indent=2)