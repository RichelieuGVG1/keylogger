import logging
from bs4 import BeautifulSoup
import requests
import os

text='{'

url = 'http://netcode.ru/cpp/?artID=234'
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text, 'html.parser')
main_title = soup.find_all('td')
for title in main_title: #90 70
    try:
        if '90' in title.get('width'):
            #58 12
            title1=str(title)
            #print(title[58:][:title[58:].find("<")])
        if '70' in title.get('width'):
            #58 12
            title2=str(title)
            #print(title1[58:][:title1[58:].find("<")])
        text+=f"\n    '{title1[58:][:title1[58:].find('<')]}' : '{title2[58:][:title2[58:].find('<')]}'"
    except:
        continue
text+='\n}'
print(text)
os.system('pause')
