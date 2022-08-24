# This file will contain functions for scraping data from the various sites we need to pull data from.

# from time import sleep
from requests_html import HTMLSession
import json
# from pprint import pprint
# from alive_progress import alive_bar
# from pathlib import Path
# import html5lib
# from bs4 import BeautifulSoup

def set_gwasi_details()->set:
    """_Hard-coded details for pulling data from the front page of gwasi.com _

    Returns:
        set: _A set containing a session object, a string containing a url, and a dictionary containing the headers._
    """
    sesh = HTMLSession() # Create a session for scraping
    url = "https://gwasi.com/delta.json"
    # If we need to, we can set up an auto-rotater for different user agents to keep the sites from banning us.

    headers = {
        "Host" : "gwasi.com",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept" : "*/*",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding" : "gzip, deflate, br",
        "Referer" : "https://gwasi.com/",
        "X-KL-Ajax-Request" : "Ajax_Request",
        "DNT" : "1",
        "Connection" : "keep-alive",
        "Sec-Fetch-Dest" : "empty",
        "Sec-Fetch-Mode" : "cors",
        "Sec-Fetch-Site" : "same-origin",
        "TE" : "trailers"
    } # Set up the headers for the session
    return set(sesh, url, headers) # Return the session, url, and headers

def set_custom_site_details(target_url:str, headers:dict)->set:
    """_Set the url and header details for pulling data from the front page of gwasi.com _

    Returns:
        set: _A set containing a session object, a string containing a url, and a dictionary containing the headers._
    """
    sesh = HTMLSession() # Create a session for scraping
    url = target_url
    # If we need to, we can set up an auto-rotater for different user agents to keep the sites from banning us.

    headers = {} # Set up the headers for the session
    return set(sesh, url, headers) # Return the session, url, and headers

def site_request(sesh, url:str, headers:dict):
    """Generate a request to a site and return the response.
    
    Args:
        url (_str_): _The url obtained through the developer tools investigation of the requests sent to the site being scraped._
        headers (_dict_): _A dictionary of key-value pairs that matches the request header sent to the site to be scraped. Extracted from the browser's developer tools._

    Returns:
        _HTMLResponse_: _The session response and key to accessing content from the parsed-in url._
    """    
    session = sesh.get(url,headers=headers)
    return session

def site_request_html(session)->str:
    """Render the page content from the session response.

    Args:
        session (_HTMLResponse_): _The session response and key to accessing content from the parsed-in url._

    Returns:
        _str_: _A string containing the returned HTML from the session's 'GET' request._
    """
    session.html.render(sleep=1, keep_page=True, scrolldown=1)
    return session.html.html

def get_site_json(session)->json:
    """Get the JSON from the session response.

    Args:
        session (_HTMLResponse_): _The session response and key to accessing content from the parsed-in url._

    Returns:
        _json_: _A json dictionary containing the returned JSON from the session's 'GET' request._
    """
    payload = {}
    
    if set_gwasi_details() is not None:
        url = set_gwasi_details()[1]
        headers = set_gwasi_details()[2]
    
    get_back = site_request_html(site_request(url, headers))
    payload = json.loads(get_back[84:-20])
    return payload

def get_site_user_list(json_payload:json)->list:
    """Get the list of users from the JSON payload.

    Args:
        json_payload (_json_): _A json dictionary containing the returned JSON from the session's 'GET' request._
    
    Returns:
        _list_: _A list of users from the JSON payload._
    """

    user_list = []

    for entry in json_payload['entries']:
        user_list.append(entry[2])
    return user_list

def get_gwasi_users()->list:
    """Get the list of users from the gwasi.com front page.
    
    Returns:
        _list_: _A list of users from the gwasi.com front page._
    """
    sesh, url, headers = set_gwasi_details()
    session = site_request(sesh, url, headers)
    get_back = site_request_html(session)
    payload = json.loads(get_back[84:-20])
    user_list = []

    for entry in payload['entries']:
        user_list.append(entry[2])
    return user_list