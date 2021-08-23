import requests
from bs4 import BeautifulSoup
import re
import sqlite3, config
from urllib.parse import urlparse

connection = sqlite3.connect(config.DB_FILE)
cursor = connection.cursor()

URL = "#"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

internal_links = []
external_links = []

link_list = soup.find_all("a")
for link in link_list:
    if re.match(r'^https://gardeem.com', link['href']):
        # print(link)
        if link['href'] not in internal_links:
            internal_links.append(link['href'])
    else:
        domain = urlparse(link['href']).netloc
        if domain not in external_links and domain != '' :
            external_links.append(domain)
            # Check if we already know about this domain and write to databse if not



# print( len(internal_links) )
print(external_links)
