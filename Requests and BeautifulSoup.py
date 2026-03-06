""""""""""
import requests
from bs4 import BeautifulSoup

url = "https://www.goudengids.nl/nl/zoeken/ICT/Meppel/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

print(soup.find_all("a"))
"""""""""

import requests
from bs4 import BeautifulSoup

url = "https://www.goudengids.nl/nl/zoeken/ICT/Meppel/"
response = requests.get(url)

print(response.status_code)
print(response.text[:500])

soup = BeautifulSoup(response.content, 'html.parser')

for i in soup.find_all("a"):
    print(i)
