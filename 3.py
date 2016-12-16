from bs4 import BeautifulSoup
from jichu import Chapter
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
data2 = [re.compile(r'\d+').search(x.get_text()).group() for x in yeshus]
# re.compile(r'\d+').search(x.get_text()).group()
# pageNum = []


chapterInfo = []
for name,url,page in zip(data1,data,data2):
    listof = {
        'name': name,
        'url': url,
        'page': int(page)
    }
    chapterInfo.append(listof)
os.makedirs('/Users/user/desktop/guidao')
for x in chapterInfo:
    name = x['name']
    url = x['url']
    page = x['page']
    spider = Chapter(name, url, page)
    spider.start()






