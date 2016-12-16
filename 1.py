
from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
}


=url = 'http://www.u17.com/chapter/266667.html'

driver = webdriver.PhantomJS()
driver.get(url)
soup = BeautifulSoup(driver.page_source,'lxml')
titles = soup.select('.image_cache.loading.cur_img')

# img = [x for x in titles]
imgArray = []
for info in titles:
    infoes = {
        'id': info['id'][-7:],
        'imgUrl': info['src']
        }
os.chdir('/Users/user/desktop')
imgId = int(infoes['id'])
imgArray.append(infoes['imgUrl'])
# print(imgId)
class GetImg(object):
    def __init__(self, new_url):
        self.new_url = new_url

    def whilwImg(self,new_url):
        driver = webdriver.PhantomJS()
        driver.get(new_url)
        c_soup = BeautifulSoup(driver.page_source, 'lxml')
        c_titles = c_soup.select('.image_cache.loading.cur_img')
        imgg = [y['src'] for y in c_titles]
        return imgg

lastNum = imgId + =8
while imgId < lastNum:
    imgId += 1
    new_url = url + '#image_id={}'.format(imgId)
    x = GetImg(new_url)
    img = x.whilwImg(new_url)
    imgArray.append(img[0])
print(imgArray)
def saveImg(imageURL, fileName):
    img = requests.get(imageURL)
    f = open(fileName, 'wb')
    f.write(img.content)
    f.close()

for one in imgArray:
    saveImg(one,one[-12:])

