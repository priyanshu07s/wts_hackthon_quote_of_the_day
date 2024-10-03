from bs4 import BeautifulSoup
import requests

url = "https://en.wikiquote.org/wiki/Wikiquote:Quote_of_the_day"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

quote = soup.find('table', style="text-align:center; width:100%").find_all('td')[0].get_text(separator=" ", strip=True)
author_p = soup.find('table', style="text-align:center; width:100%").find_all('td')[1]
author = author_p.find('a').get_text(strip=True) if author_p.find('a') else author_p.get_text(strip=True)


featured_time = soup.find('center', string=lambda x: x and "Today is" in x).get_text(separator=" ", strip=True)
unique_number = []
for char in featured_time:
    if char.isdigit():
        unique_number.append(int(char))

print("Quote-",quote,"\n")

print("Author-" ,author,"\n")

print("Featured Time-" ,featured_time,"\n")
print("Unique ID-",end='')
for i in range(len(unique_number)):
    print(unique_number[i],end='')
