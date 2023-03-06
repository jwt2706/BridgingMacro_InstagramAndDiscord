#actual application, for edge browser

from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://discord.com/login")




discordUsername.sendKeys("username")
discordPassword.sendKeys("password")

driver.close()