import requests
from bs4 import BeautifulSoup



url = r'http://vcsm.vatech.co.kr/vcare/pub/product/product03.do'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')
result = soup.prettify()
print(result)