from bs4 import BeautifulSoup
import requests,re
import os

url = 'http://www.u17.com/comic/68471.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
titles = soup.select('#chapter li a')
# href title
data = [x['href'] for x in titles]
data1 = [x['title'] for x in titles]
yeshus = soup.select('#chapter li')
data2 = [x.get_text() for x in yeshus]
pageNum = []
for y in data2:
    qq = [x for x in y if x.strip().isdigit()]
    i = 0
    ll = ''
    while i < len(qq):
        ll += qq[i]
        i += 1
        pageNum.append(ll)
for name,url,page in zip(data1,data,pageNum):
    listof = {
        'name': name,
        'url': url,
        'page': page
    }







