from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Replace 'your_url' with the actual URL you want to visit
url = 'your_url'

# Set the path to the webdriver executable (e.g., chromedriver.exe for Chrome)
webdriver_path = 'path/to/chromedriver'

# Create a webdriver instance (for Chrome in this example)
driver = webdriver.Chrome(executable_path=webdriver_path)

try:
    # Open the URL
    driver.get(url)

    # Locate the toggle button using its XPath (replace 'your_toggle_xpath' with the actual XPath)
    toggle_button = driver.find_element(By.XPATH, 'your_toggle_xpath')

    # Check if the toggle is currently off
    if not toggle_button.is_selected():
        # If off, click to turn it on
        toggle_button.click()

    # You can add more interactions or actions as needed

finally:
    # Close the webdriver
    driver.quit()
