from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instantiate the WebDriver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# # Load the target page
# captcha_page_url = "https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php"
# driver.get(captcha_page_url)

# # Solve the Captcha
# print("Solving Captcha")
# solver = TwoCaptcha("f7635ad1dba976555ce8a68a4dc311dc")
# response = solver.recaptcha(sitekey='6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9', url=captcha_page_url)
# code = response['code']
# print(f"Successfully solved the Captcha. The solve code is {code}")

# test_driver = webdriver.Chrome()

# solver = RecaptchaSolver(driver=test_driver)

# test_driver.get('https://www.google.com/recaptcha/api2/demo')

# recaptcha_iframe = test_driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')

# solver.click_recaptcha_v2(iframe=recaptcha_iframe)


import pytesseract
from PIL import Image
import time

# Path to Tesseract executable (You need to install Tesseract separately)
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Launch the browser with Selenium
driver = webdriver.Chrome()

# Navigate to the page with the Captcha
driver.get('https://www.brandbucket.com/user/signin/')  # Replace with the URL of the page with the Captcha

time.sleep(12)

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()

# time.sleep(10)

# Find the Captcha element using Selenium and 
# get its screenshot
captcha_element = driver.find_element_by_xpath('//div[@class="captcha-image"]')  # Replace with the correct XPath
captcha_screenshot = captcha_element.screenshot_as_png

# Convert the screenshot to a PIL Image and perform OCR
captcha_image = Image.open(BytesIO(captcha_screenshot))
captcha_text = pytesseract.image_to_string(captcha_image)

# Inject the Captcha response into the input field using Selenium
captcha_input = driver.find_element_by_xpath('//input[@id="captcha-input"]')  # Replace with the correct XPath
captcha_input.send_keys(captcha_text)

# Continue with your login or form submission process
# ...

# Remember to close the browser after you're done
driver.quit()
