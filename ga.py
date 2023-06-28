import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Prompt the user for the website URL
website_url = input("Enter the website URL: ")

# Set up the Selenium WebDriver
driver = webdriver.Chrome(executable_path = r'C:\Users\samue\Desktop\selenium_python\chromedriver2.exe')

# Launch the browser and navigate to the website
driver.get(website_url)

# Scroll down the page
driver.find_element_by_tag_name('body').send_keys(Keys.END)
time.sleep(2)  # Adjust the wait time as needed

# Scroll up the page
driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
time.sleep(2)  # Adjust the wait time as needed

# Extract the GIF URLs from the network tab
entries = driver.execute_script("return window.performance.getEntriesByType('resource')")
gif_urls = [entry['name'] for entry in entries if '.gif' in entry['name']]

# Close the browser
driver.quit()

# Display the GIF URLs in the terminal
print("GIF URLs:")
for gif_url in gif_urls:
    print(gif_url)
