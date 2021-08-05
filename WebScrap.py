#Bibliotecas
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import openpyxl

#URLs
steam = "https://store.steampowered.com/app/753640/Outer_Wilds/"
microsoft = "https://www.microsoft.com/pt-br/p/outer-wilds/c596fkdkmqn7?activetab=pivot:overviewtab"
egs = "https://www.epicgames.com/store/pt-BR/p/outerwilds"


option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'C:\Users\gazet\AppData\Local\Programs\Python\Python39\geckodriver.exe')

#Steam
driver.get(steam)
element = driver.find_element_by_xpath("//div[@class='game_purchase_price price']")
html_content1 = element.get_attribute('innerHTML')
print(html_content1)

#Microsoft
driver.get(microsoft)
element = driver.find_element_by_xpath("//div[@class='pi-price-text']/.//span")
html_content2 = element.get_attribute('innerHTML')
print(html_content2)

driver.get(egs)
element = driver.find_element_by_xpath("//div[@class='css-nxq7ez-PriceLayout__rowItem']/.//span")
html_content3 = element.get_attribute('innerHTML')
print(html_content3)



time.sleep(10)
driver.quit()