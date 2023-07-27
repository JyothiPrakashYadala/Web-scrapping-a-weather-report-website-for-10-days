import requests
from bs4 import BeautifulSoup
link = 'https://www.w3schools.com/python/default.asp'
response = requests.get(link)
soup = BeautifulSoup(response.content,'html.parser')
res = soup.find('h1').get_text()
fo = open('ws.txt','w')
fo.write(res)
fo.close()

