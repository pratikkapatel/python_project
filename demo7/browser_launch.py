import time

from selenium import webdriver

d=webdriver.Chrome(executable_path=r"C:\Components\chromedriver.exe")
d.get("https://google.com/")
print(d.title)

#get url
#get page source

time.sleep(10)

d.quit()