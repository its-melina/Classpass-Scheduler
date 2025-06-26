from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def book_class(driver):
    sections = driver.find_elements(By.CSS_SELECTOR, "section.uK1zXcGKM5742QoxvHdU")

    for section in sections:
        time = section.find_element(By.CSS_SELECTOR, "time.cdnPp6xZIZ3D8Ad0YMhn")
        if "11:30" in time.text:
            print(time.text)
            
            reserve_button_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(section.find_element(By.CSS_SELECTOR, "button.Schedule__cta")))
            reserve_button_1.click()
            reserve_button_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, '.bt.bt--primary.bt--lg.bt--width-lg')))
            reserve_button_2.click()