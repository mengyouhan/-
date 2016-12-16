# from bs4 import BeautifulSoup
# import requests
# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'
# }
#
#
# url = 'http://www.u17.com/chapter/266667.html#image_id=1911649'
#
# driver = webdriver.PhantomJS()
# driver.get(url)
# soup = BeautifulSoup(driver.page_source,'lxml')
# titles = soup.select('.image_cache.loading.cur_img')
# print(titles)
# new_url = 'http://www.u17.com/chapter/266667.html#image_id=1911645'
# # driver.get(new_url)
#
# class GetImg(object):
#     def __init__(self, new_url):
#         self.new_url = new_url
#
#     def whilwImg(self,new_url):
#         driver = webdriver.PhantomJS()
#         driver.get(new_url)
#         c_soup = BeautifulSoup(driver.page_source, 'lxml')
#         c_titles = c_soup.select('.image_cache.loading.cur_img')
#         print(c_titles)
#         imgg = [y['src'] for y in c_titles]
#         return imgg
#
# x = GetImg(new_url)
# img = x.whilwImg(new_url)
# print(img)
# print(1)


saveId = 0
while saveId < 9:
    print(saveId+1)
    saveId += 1