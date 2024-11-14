import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Setup WebDriver for Microsoft Edge
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Open Google
driver.get("http://www.google.com")

# Find the search box and enter "Hello World"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello World")
search_box.send_keys(Keys.RETURN)

time.sleep(10000)

# Close the browser
driver.quit()