#Bibliotecas
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

#URL da steam
url = "https://store.steampowered.com/app/753640/Outer_Wilds/"

option = Options()