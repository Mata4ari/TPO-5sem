from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.21vek.by/')

try:
    time.sleep(2)
    button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'AgreementCookie_reject__f5oqP')))
    button.click()
    btn2 = driver.find_element(By.CLASS_NAME,'Button-module__gray-secondary')
    btn2.click()
   
    inp3 = driver.find_element(By.ID, 'catalogSearch')
    inp3.click()
    inp3.send_keys('холодильник')
    inp3.send_keys(Keys.RETURN)
    btn3 = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.cr-tools-sort__bi')))
    btn3.click()
    time.sleep(5)
    btn3.click()
    print('test passed')

    time.sleep(5)
    checkbox = driver.find_element(By.CSS_SELECTOR,'label[title="LG"]')
    checkbox.click()
    btn4 = driver.find_element(By.CLASS_NAME,'filter-controls__submit')
    btn4.click()
    print('test passed')

    time.sleep(1000)
except Exception as e:
    print(e)