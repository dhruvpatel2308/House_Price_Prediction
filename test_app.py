from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://housepriceui-aocbtsgxyzsdudmixmzktu.streamlit.app/") 

# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Switch to the first <iframe> (index 0)
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(0))

# driver.switch_to.frame(0)
input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'text_input_1')))

driver.find_element(By.ID, 'text_input_1').send_keys('8.3252')
driver.find_element(By.ID, 'text_input_2').send_keys('41')
driver.find_element(By.ID, 'text_input_3').send_keys('6.0')
driver.find_element(By.ID, 'text_input_4').send_keys('1.0')
driver.find_element(By.ID, 'text_input_5').send_keys('1.0')
driver.find_element(By.ID, 'text_input_6').send_keys('2.5')
driver.find_element(By.ID, 'text_input_7').send_keys('37.88')
driver.find_element(By.ID, 'text_input_8').send_keys('-122.23')

driver.find_element(By.XPATH, '//button/div/p').click()


# Wait for the response
try:
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), 'House Price is')
    )
    # Capture and print the result
    result = driver.find_element(By.XPATH, "//div/div/p").text
    print(result)
except Exception as e:
    print("Error: Unable to get the prediction result.")
    print(e)

# Close the browser
driver.quit()
