from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox() # CAN PROBABLY CHANGE THIS TO CHROME

driver.get("https://discord.com/login")
time.sleep(6)

file = open("info.txt","r")
info = file.readlines()

username_input = driver.find_element("name","email")
username_input.send_keys(info[0])

password_input = driver.find_element("name","password")
password_input.send_keys(info[1])

#ogin_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
#login_button.click()
time.sleep(1000)

file.close()
driver.close()