import sqlite3
from bs4 import BeautifulSoup
import requests
response = requests.get( "https://www.accuweather.com/ru/az/baku/27103/current-weather/27103?partner=wdg_operanrw_web" )
soup = BeautifulSoup(response.text, features="html.parser")
Temperature= str(soup.find("div", 'display-temp'))



connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('?????'); ")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()
