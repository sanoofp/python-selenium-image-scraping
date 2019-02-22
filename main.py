from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException 
import urllib.request
import random
import os

from config import local_path


url = input('Enter the url : ')

driver = webdriver.Chrome(executable_path=local_path)
driver.get(url)
try:
  WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
  print('OK')
except TimeoutException:
  print('Timeout')

imgs = driver.find_elements_by_tag_name('img')
# imgs = driver.find_element_by_xpath('//img')
returnImgs = []
for img in imgs:
  returnImgs.append(img.get_attribute('src'))
  print(img.get_attribute('src'))

for src in returnImgs:
  imgsrc = str(src)
  imgExt = imgsrc[-4:]
  
  download_link = os.path.dirname(os.path.realpath(__file__))+'/downloads/'+str(random.randint(1, 1000))+imgExt
  print("Downlodaing to :::: "+download_link)
  urllib.request.urlretrieve(imgsrc, download_link)