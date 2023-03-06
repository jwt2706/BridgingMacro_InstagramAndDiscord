#updates the edge driver, then opens google.com as a test

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
 
driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.maximize_window()
driver.get("https://google.com")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.quit()