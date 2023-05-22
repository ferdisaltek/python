from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the ChromeDriver executable
chrome_driver_path = 'path_to_chromedriver.exe'  # Replace with the actual path

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the webpage with the form
driver.get('https://example.com/form')  # Replace with the actual URL

# Fill in the form fields
input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'input-field-id')))
input_field.send_keys('Your text')

checkbox = driver.find_element(By.ID, 'checkbox-id')
checkbox.click()

# Submit the form
submit_button = driver.find_element(By.ID, 'submit-button-id')
submit_button.click()

# Close the browser
driver.quit()
