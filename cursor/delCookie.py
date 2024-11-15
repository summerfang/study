from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to the Edge WebDriver
service = Service("C:\edgedriver_win64\msedgedriver.exe")

# Initialize the Edge WebDriver
driver = webdriver.Edge(service=service)

# Open the website
driver.get("https://www.cursor.com")

# Delete cookies for the specific website
driver.delete_all_cookies()

print("Cookies cleared for www.cursor.com")

# Close the browser
driver.quit()
