from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox() # CAN PROBABLY CHANGE THIS TO CHROME

driver.get("https://discord.com/login")
time.sleep(1)

file = open("info.txt","r")
info = file.readlines()

#enters info
driver.find_element("name","email").send_keys(info[0])
driver.find_element("name","password").send_keys(info[1])
#clicks login button
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

#wait for captcha

driver.execute_script('''window.open("https://instagram.com/accounts/login","_blank");''')
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(info[2])
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(info[3])
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()


time.sleep(1000)

file.close()
driver.close()