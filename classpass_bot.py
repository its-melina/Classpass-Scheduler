from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import selenium
from datetime import datetime, timedelta, date
from util import *
import time
import os

# email and password should be set as environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://classpass.com/login")

# say ok to cookies
time.sleep(3)
try:
    cookie_button = driver.find_element(By.ID, "truste-consent-button")
    cookie_button.click()
except:
    print('no cookie popup')

# type in username and password
username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.ID, "email")))
username_field.send_keys(email)

time.sleep(1)
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.ID, "password")))
password_field.send_keys(password)


# click login
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, ".mt.bt.bt--primary.bt--lg.bt--width-full")))
login_button.click()

# click x on popup
try:
    x_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "button[data-qa='Modal.close']")))
    x_button.click()
except:
    print('no popup')

time.sleep(5)

sculpt = 'https://classpass.com/studios/sculpt50-campbell'
club_pilates = "https://classpass.com/studios/club-pilates-west-san-jose-aiuh"

driver.get(club_pilates)

# the booking window opens 3 days before the date at 5 AM
today = datetime.now()
three_days = timedelta(days=3)
day_to_book = today + three_days

next_day_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, "[aria-label='Next day']")))

for i in range(3):
    # Click using JavaScript to bypass the overlay
    driver.execute_script("arguments[0].click();", next_day_button)
    time.sleep(0.5)

time.sleep(2) 
book_class(driver)



