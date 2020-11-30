# Helpful links
# https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
# https://medium.com/@sateesh.gmc/how-to-scrape-wikipedia-table-using-python-beautiful-soup-cd0d8ee1a319
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#tag
# https://www.w3schools.com/TAGs/

# Website we are scraping 
# https://en.wikipedia.org/wiki/List_of_chemical_elements

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import sys
import requests 


wiki = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'

# If your request is successful, then expected HTTP response status code is 200
s = requests.Session()
response = s.get(wiki, timeout=10)
print(response)

# Sends a get request to the URL
page = requests.get(wiki)
soup = BeautifulSoup(page.content, 'html.parser')

# .text prints the string 
title = soup.title.text
print(title)
# body = soup.body.text
# # print(body)
# head = soup.head.text
# print(head)

Elements = []

# Selecting DOM (document object model) elements
for elementNum in soup.select('tr'):

    title = Elements.select('h4 > .title')[0].text
    review_label = Elements.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    Elements.append(elementNum.text)



print('Number of td (data cells in HTML):', len(Elements))
# print(Elements[0:8])


