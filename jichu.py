from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class Chapter(object):
    def __init__(self,name,url,page):
        self.name = name
        self.url = url
        self.page = page

    def start(self):

        url = self.url


        driver = webdriver.PhantomJS()
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        titles = soup.select('.image_cache.loading.cur_img')

        imgArray = []
        for info in titles:
            infoes = {
                'id': info['id'][-7:],
                'imgUrl': info['src']
            }

        imgId = int(infoes['id'])
        imgArray.append(infoes['imgUrl'])
        # print(imgId)



        lastNum = imgId + self.page -1
        while imgId < lastNum:
            imgId += 1
            new_url = url + '#image_id={}'.format(imgId)

            driver = webdriver.PhantomJS()
            driver.get(new_url)
            c_soup = BeautifulSoup(driver.page_source, 'lxml')
            c_titles = c_soup.select('.image_cache.loading.cur_img')
            imgg = [y['src'] for y in c_titles]
            imgArray.append(imgg[0])
        # print(imgArray)
        os.makedirs('/Users/user/desktop/guidao/{}'.format(self.name))
        os.chdir('/Users/user/desktop/guidao/{}'.format(self.name))

        def saveImg(imageURL, fileName):
            img = requests.get(imageURL)
            f = open(fileName, 'wb')
            f.write(img.content)
            f.close()

        saveId = 0
        while saveId < len(imgArray):
            saveImg(imgArray[saveId],'{}.jpg'.format(saveId+1))
            saveId += 1


# name = '第零章（楔子）：天堂之眼 上 2014-03-18'
# url = 'http://www.u17.com/chapter/266667.html'
# page = 9
# spider = Chapter(name,url,page)
# spider.start()

