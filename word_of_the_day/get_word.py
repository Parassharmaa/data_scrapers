from bs4 import BeautifulSoup
import requests
data = requests.get("http://www.wordthink.com/").text
soup = BeautifulSoup(data, "html.parser")
word = soup.h2.text.strip()
meaning = soup.p.text.strip()
print("*"*10)
print("Word of the Day: %s \n**********\nMeaning: %s" %(word, meaning))

