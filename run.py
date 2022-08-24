from lib.scrape import get_gwasi_users as gg
from lib.scrape import set_custom_site_details, site_request
from lib.routing import send_data_to_file as s2f
from dotenv import load_dotenv	  #Remember to pip install python_dotenv first
import os
from alive_progress import alive_bar


def glance_soundgasm(limit=0):
    user_list = gg()

    env_path = "lib/.env"
    load_dotenv(dotenv_path=env_path)

    COOKIE = os.getenv("SOUNDGASM_COOKIE")
    

    headers = {
        "Host" : "soundgasm.net",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding" : "gzip, deflate, br",
        "DNT" : "1",
        "Connection" : "keep-alive",
        "Cookie" : COOKIE,
        "Upgrade-Insecure-Requests" : "1",
        "Sec-Fetch-Dest" : "document",
        "Sec-Fetch-Mode" : "navigate",
        "Sec-Fetch-Site" : "none",
        "Sec-Fetch-User" : "?1",
    }

    response_list = []

    with alive_bar(len(user_list)) as bar:
        for user in user_list:
            target_url = f"https://soundgasm.net/u/{user}"
            details = set_custom_site_details(target_url, headers)
            response = site_request(details[0], details[1], details[2])
            response_list.append({ "user" : user, "result" : response.http_status_code() })
            bar()
    return response_list


if __name__ == "__main__":
    s2f(glance_soundgasm(30), "data/glance_soundgasm.json")