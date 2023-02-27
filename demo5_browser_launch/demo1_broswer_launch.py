
from selenium import webdriver
import time

d1=webdriver.Chrome()

d1.get("https://www.google.com/")

print(d1.title)
time.sleep(10)