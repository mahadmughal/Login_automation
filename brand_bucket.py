import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import time
import pdb

CAPTCHA_API_KEY = 'f7635ad1dba976555ce8a68a4dc311dc'
WEBSITE_LOGIN_URL = 'https://www.brandbucket.com/user/signin/'

# Function to solve Captcha using 2Captcha API
def solve_captcha(api_key, site_key, page_url):

    solver = TwoCaptcha(CAPTCHA_API_KEY)
    response = solver.recaptcha(sitekey=site_key, url=WEBSITE_LOGIN_URL)

    return response['code']

    # response = requests.post('http://2captcha.com/in.php', data=captcha_data)
    # request_id = response.text.split('|')[1]

    # while True:
    #     response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}')
    #     if 'CAPCHA_NOT_READY' not in response.text:
    #         return response.text.split('|')[1]
    
    # return None

# Launch the browser with Selenium
# driver = webdriver.Chrome()

# # Navigate to the page with the Captcha
# driver.get(url)

# # Find the Captcha element using Selenium and get its attributes
# captcha_element = driver.find_element_by_xpath('//div[@class="g-recaptcha"]')
# captcha_site_key = captcha_element.get_attribute('data-sitekey')

# # Solve the Captcha using 2Captcha
# captcha_response = solve_captcha(API_KEY, captcha_site_key, url)

# # Inject the Captcha response into the input field using JavaScript
# driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_response}";')


def login_to_website(username, password):
    username_field_id = 'edit-name'
    password_field_id = 'edit-pass'
    captcha_checkbox_id = 'recaptcha-anchor'

    try:
        # Initialize the WebDriver (here we'll use Chrome, but you can use Firefox or others too)
        driver = webdriver.Chrome()
        
        # Navigate to the website
        driver.get(WEBSITE_LOGIN_URL)

        # Wait for the page to load (you might need to adjust the waiting time based on your website)
        time.sleep(10)

        # Find the username and password fields and enter the credentials
        username_field = driver.find_element(By.ID, username_field_id)
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, password_field_id)
        password_field.send_keys(password)

        time.sleep(10)

        captcha_page_url = driver.find_element(By.CSS_SELECTOR, "iframe[src^='https://www.google.com/recaptcha/api2/anchor']").get_attribute('src')
        captcha_element = driver.find_element(By.XPATH, '//div[@class="g-recaptcha"]')
        captcha_site_key = captcha_element.get_attribute('data-sitekey')

        wait = WebDriverWait(driver, 10)
        iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor']")))
        driver.switch_to.frame(iframe)

        driver.switch_to.default_content()

        captcha_code = solve_captcha(CAPTCHA_API_KEY, captcha_site_key, captcha_page_url)

        recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response')
        driver.execute_script(f'arguments[0].value = "{captcha_code}";', recaptcha_response_element)

        # driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{captcha_response}";')

        # driver.find_element(By.CSS_SELECTOR, "div.recaptcha-checkbox-border").click()

        # pdb.set_trace()

        # Submit the login form (you might need to adjust this based on your website's structure)
        login_btn = driver.find_element(By.ID, 'edit-submit')
        login_btn.click()

        # Wait for a few seconds to let the page load after login (you might need to adjust this as well)
        time.sleep(10)

        # Optionally, you can add code here to check if the login was successful
        # For example, check if a specific element exists on the dashboard/homepage after login

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window
        driver.quit()

# Replace 'your_username_here' and 'your_password_here' with your actual login credentials
login_to_website('abdulsameedotcom@gmail.com', 'op3nit/Hbb369ss')
