import requests
page = requests.get("http://www.usccb.org/bible/readings/073019.cfm")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

mass_reading = soup.find_all(class_="poetry")

f = open("daily_reading.txt",'w', encoding = 'utf-8')
for reading in mass_reading: 
    f.write(str(reading))

f.close()
