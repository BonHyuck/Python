from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Temp/chromedriver')
driver.implicitly_wait(3)

driver.get("https://comic.naver.com/genre/bestChallenge.nhn?&page=")

title = driver.find_element_by_xpath('//td/div/h6/a/text()')
summary = driver.find_element_by_xpath('//td/div/div[1]')
rating = driver.find_element_by_xpath('//td/div/div[2]/strong')

print(title)
print(summary)
print(rating)