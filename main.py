from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException 
import urllib.request
import random
import os

# path for the chromedriver.exe
from config import local_path


url = input('Enter the url : ')

driver = webdriver.Chrome(executable_path=local_path)
driver.get(url)
try:
  # Wait for the webpage to load all images
  WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
  print('OK')
except TimeoutException:
  print('Timeout')

# get all img tags and assign the 'src' attributes to returnImgs array
imgs = driver.find_elements_by_tag_name('img')
returnImgs = []
for img in imgs:
  returnImgs.append(img.get_attribute('src'))
  print(img.get_attribute('src'))

# Loop through each source link
for src in returnImgs:
  imgsrc = str(src)
  imgExt = imgsrc[-4:] # Not reliable

  # Fixes for base64 (Need better approach)
  if(imgExt != '.png' or imgExt != '.jpg' or imgExt != '.svg'):
    if(imgExt.find('.svg') > 0):
      imgExt = ".svg"
    elif(imgExt.find('jpeg') > 0):
      imgExt = ".jpg"
    else:
      imgExt = ".jpg"
  
  # Creating a local download link path with image extension
  download_link = os.path.dirname(os.path.realpath(__file__))+'/downloads/'+str(random.randint(1, 1000))+imgExt

  print("Downlodaing to :::: "+download_link)
  # Download to ./downloads folder
  urllib.request.urlretrieve(imgsrc, download_link)
