import requests
from bs4 import BeautifulSoup as BS 
from time import time
import sqlite3 as sql

db = sql.connect("cities.db")
cur = db.cursor()

t1  = time()

url  = "http://www.topix.com/city/list/p"
a_url = []
all_cities = []
for i in range(1,26):
	a_url.append(url+str(i))

try:
	for u in a_url:
		d = requests.get(u)
		soup = BS(d.text, "html.parser")
		print("Scraping "+u)
		soup = soup.select('a[t="dir-list-all-childnode"]')
		for i in soup:
			all_cities.append(i.text.strip())
except Exception as e:
	print(e)

print("Number of Cities:"+str(len(all_cities)))
f = open("cities.txt", "w")

for i in all_cities:
	f.write(i+"\n")
t2=  time()
query = "INSERT INTO us_cities (city_name) VALUES (?)"

for name in all_cities:
	cur.execute(query, (name,))
db.commit()

print("Time Taken: "+str(t2-t1))
