import requests
from bs4 import BeautifulSoup
import pandas as pd

link = 'https://weather.com/en-IN/weather/tenday/l/fbae48adde7ca1e8902fa6e1cee6eaa64fbefd2a8af9e009cc24dcb9d76726cb'

response = requests.get(link)

soup = BeautifulSoup(response.content,'html.parser')

res1 = soup.find_all(class_ = 'DaypartDetails--DayPartDetail--2XOOV Disclosure--themeList--1Dz21')


day = [res.find(class_='DetailsSummary--daypartName--kbngc').get_text() for res in res1]
des = [res.find(class_='DetailsSummary--extendedData--307Ax').get_text() for res in res1]

# d = {}
# for vk in range(len(day)):
#     d[day[vk]] = des[vk]
# print(d)

report = pd.DataFrame({
                        'day' : day,
                        'description' : des,
                     })

print(report)

# report.to_csv('weather_report.csv')
