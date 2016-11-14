import requests
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

url = 'https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'lxml')
# print soup.prettify()

table = soup.find('table')
# print (table.prettify())
val = 0
tags = []
discription = []
for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        val %= 3
        if val == 1:
            tags.append(str(cell.text))
        elif val == 2:
            discription.append(str(cell.text))
        val += 1
print(len(tags))
print(len(discription))
