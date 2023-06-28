import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Prompt the user for the website URLs (comma-separated)
website_urls_input = input("Enter the website URLs (comma-separated): ")
website_urls = [url.strip() for url in website_urls_input.split(",")]

# Set up the Selenium WebDriver
driver = webdriver.Chrome(executable_path = r'C:\Users\samue\Desktop\selenium_python\chromedriver2.exe')

# Create a list to store the results
results = []

# Loop through the website URLs
for url in website_urls:
    # Launch the browser and navigate to the website
    driver.get(url)

    # Scroll down the page
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)  # Adjust the wait time as needed

    # Scroll up the page
    driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
    time.sleep(2)  # Adjust the wait time as needed

    # Extract the GIF URLs from the network tab
    entries = driver.execute_script("return window.performance.getEntriesByType('resource')")
    gif_urls = [entry['name'] for entry in entries if '.gif' in entry['name']]

    # Append the results for the current website URL
    if gif_urls:
        results.extend([(url, gif_url) for gif_url in gif_urls])
    else:
        results.append((url, 'No GIF URLs found. Try a different website or check the page content.'))

# Close the browser
driver.quit()

# Display the results in the terminal
for result in results:
    print("Website:", result[0])
    if 'No GIF URLs found' in result[1]:
        print("Failure:", result[1])
    else:
        print("GIF URL:", result[1])
    print()
