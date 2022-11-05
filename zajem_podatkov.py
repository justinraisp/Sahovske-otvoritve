import csv
import os
import requests
import re


url_otvoritve = r"https://old.chesstempo.com/chess-openings.html"

def download_url_to_string(url):
    """Funkcija kot argument sprejme niz in poskusi vrniti vsebino te spletne
    strani kot niz. V primeru, da med izvajanje pride do napake vrne None.
    """
    try:
        # del kode, ki morda sproži napako
        page_content = requests.get(url)
    except Exception as e:
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        print(f"NAPAKA PRI PRNOSU: {url} ::",e)
        return None
    # nadaljujemo s kodo če ni prišlo do napake
    return page_content.text

def save_string_to_file(text, directory, filename):
    """Funkcija zapiše vrednost parametra "text" v novo ustvarjeno datoteko
    locirano v "directory"/"filename", ali povozi obstoječo. V primeru, da je
    niz "directory" prazen datoteko ustvari v trenutni mapi.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

from requests_html import HTMLSession
session = HTMLSession()
resp = session.get("https://old.chesstempo.com/chess-openings.html")

stran = download_url_to_string(url_otvoritve)
#print(stran)
page_content = requests.get("https://old.chesstempo.com/chess-openings.html")
print(page_content)


import traceback

def searchApi(query):
    endpoint = "https://old.chesstempo.com/requests/openingslist.php?"
    data = {
        "q": query
    }
    try:
        response = requests.post(endpoint, data=data)
        if(response.status_code == 200):
            for msg in response:
                print(msg)
                
    except Exception:
        print(traceback.format_exc())
searchApi("total_openings")

content = requests.post("https://old.chesstempo.com/requests/openingslist.php?").content
print(content)

import json
import urllib.request
url = "https://old.chesstempo.com/requests/session_details.php"
x = urllib.request.urlopen(url)
raw_data = x.read()
encoding = x.info().get_content_charset('utf8')  # JSON default
print(raw_data)   #this is data in string format
data = json.loads(raw_data.decode(encoding))
print(data)   #this would be your json data
/html/body/div/div[2]/div/div/div/div[3]/div/table/tbody[2]/tr[1]
//*[@id="yui-rec0"]
<a href="#" class="yui-pg-page" page="2">2</a>