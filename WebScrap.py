#Bibliotecas
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

#URLs
steam = "https://store.steampowered.com/"
microsoft = "https://www.microsoft.com/pt-br/"
egs = "https://www.epicgames.com/store/pt-BR/"

#pede o nome do jogo
search = input("Nome do Jogo: ")

#usa o launcher do firefox
option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'C:\Users\gazet\AppData\Local\Programs\Python\Python39\geckodriver.exe')


#faz pesquisa na steam
driver.get(steam)
element = driver.find_element_by_xpath("//div[@class='searchbox']//input")
element.click()
element.send_keys(search)
element.send_keys(Keys.ENTER)
time.sleep(3)
element = driver.find_element_by_xpath("//div[@class='col search_price  responsive_secondrow']")
html_content1 = element.get_attribute('innerHTML')
print(html_content1)

time.sleep(2)


#faz pesquisa na MsStore
driver.get(microsoft)
time.sleep(2)
element = driver.find_element_by_xpath("//form[@class='c-search']")
element.click()
time.sleep(2)
driver.find_element_by_id("cli_shellHeaderSearchInput").send_keys(search)
time.sleep(2)
driver.find_element_by_xpath("ul[@class='c-menu']/li[1]").click()
time.sleep(2)
element = driver.find_element_by_xpath("//div[@class='pi-price-text']/.//span")
html_content2 = element.get_attribute('innerHTML')
print(html_content2)

//*[@id="universal-header-search-auto-suggest-ul"]
#pesquisa na EGS
driver.get(egs)
driver.find_element_by_id("searchInput").send_keys(search)
time.sleep(2)
driver.find_element_by_id("result-item-0").click()
time.sleep(2)
element = driver.find_element_by_xpath("//div[@class='css-nxq7ez-PriceLayout__rowItem']/.//span")
html_content3 = element.get_attribute('innerHTML')
print(html_content3)



time.sleep(10)
driver.quit() 