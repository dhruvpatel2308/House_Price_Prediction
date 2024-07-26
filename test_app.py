from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver (Make sure you have the correct path to your chromedriver)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the Streamlit app
driver.get('https://housepriceui-aocbtsgxyzsdudmixmzktu.streamlit.app/')  # Ensure your Streamlit app is running on this port

# Wait for the page to load
time.sleep(3)

# Input data into the text fields
driver.find_element(By.XPATH, "//input[@placeholder='income in block group:']").send_keys("8.3252")
driver.find_element(By.XPATH, "//input[@placeholder='house age in block group:']").send_keys("41")
driver.find_element(By.XPATH, "//input[@placeholder='number of rooms per household:']").send_keys("6.9841")
driver.find_element(By.XPATH, "//input[@placeholder='number of bedrooms per household:']").send_keys("1.0238")
driver.find_element(By.XPATH, "//input[@placeholder='population:']").send_keys("322")
driver.find_element(By.XPATH, "//input[@placeholder='number of household members:']").send_keys("2.5556")
driver.find_element(By.XPATH, "//input[@placeholder='Latitude:']").send_keys("37.88")
driver.find_element(By.XPATH, "//input[@placeholder='Longitude:']").send_keys("-122.23")

# Click the "Predict" button
predict_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Predict')]")
predict_button.click()

# Wait for the response
try:
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'House Price is')
    )
    # Capture and print the result
    result = driver.find_element(By.XPATH, "//div[contains(text(), 'House Price is')]").text
    print(result)
except Exception as e:
    print("Error: Unable to get the prediction result.")
    print(e)

# Close the browser
driver.quit()