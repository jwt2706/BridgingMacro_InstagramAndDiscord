from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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

#wait for captcha, and 2fa if it's there
wait = WebDriverWait(driver, 10) #might be something wrong with the gecko driver...
wait.until(lambda driver: driver.current_url=="https://www.discord.com/channels/@me")
#wait until completely in
time .sleep(1)

#navigate to the server and find the channel
driver.get("https://discord.com/channels/"+info[4])

#go to instagram
driver.execute_script('''window.open("https://instagram.com/accounts/login","_blank");''')
time.sleep(1)

#enter login information for instagram 
#driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(info[2])
#driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(info[3])
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()


#2fa if thats event a thing in this case

#navigate from home page to dms
#open dms

#while theres unread dms
    #if there's an image
        #copy
        #go to discord, paste (dont send)
        #copy username
        #paste in the message: From @xyz on instagram
        #add message "if you want to see your photos here, dm to us on insta" or smt
        #send message (make this manual???????????) [wait until enter is pressed]
        #cycle again
    #else
        #put dm as unread (if possible or maybe something similar)
        #move on
#log out
#close

time.sleep(1000)

file.close()
driver.close()