import requests
from setting import URL_TO_PLAYLIST

#URL_TO_PLAYLIST = input("PlayList URL: ")

RESPONSE = requests.get(URL_TO_PLAYLIST)

if RESPONSE.ok:
    with open("log.html", "w") as f:
        #f.write(RESPONSE.text)
        for attr in dir(RESPONSE):
            f.write(f"Attrib_name: '{attr}', Value: '{getattr(RESPONSE, attr)}'\n\n--------------------------------------------------------------------------\n")