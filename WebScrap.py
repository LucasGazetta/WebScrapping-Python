#Bibliotecas
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import json

#URL da steam
url = "https://store.steampowered.com/app/753640/Outer_Wilds/"

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'C:\Users\gazet\AppData\Local\Programs\Python\Python39\geckodriver.exe')


driver.get(url)
time.sleep(10)
element = driver.find_element_by_xpath("//div[@class='game_purchase_price price']")
html_content = element.get_attribute('outerHTML')

#Parseando o conteúdo HTML - BS
soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find(name=)



driver.quit()