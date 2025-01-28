from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.21vek.by/')

try:
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'AgreementCookie_reject__f5oqP')))
    button.click()
    btn2 = driver.find_element(By.CLASS_NAME,'Button-module__gray-secondary')
    btn2.click()
    btn3 = driver.find_element(By.CLASS_NAME,'styles_userToolsToggler__c2aHe')
    btn3.click()
    btn4 = driver.find_element(By.CLASS_NAME,'userToolsBtn')
    btn4.click()
    inp1 = driver.find_element(By.ID,'login-email')
    inp1.send_keys('ffllyfnya@gmail.com')
    inp2 = driver.find_element(By.ID,'login-password')
    inp2.send_keys('2004010203')
    btn5 = driver.find_element(By.CLASS_NAME,'EmailLoginForm_baseActionButton__OAFqW')
    btn5.click()
    btn6 = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="modalClose"]')))
    btn6.click()
    print('authorization completed')


    time.sleep(5)
    driver.get('https://www.21vek.by/portable_audio/2yndx00026vio_yandex_9211399.html?recommendationId=ab0424e8d159447f97fb1918a2241d52')
    btn7 = driver.find_element(By.CLASS_NAME,'FavoritesButton_button__oIuqE')
    btn7.click()
    print('test passed')

    

    time.sleep(100)
except Exception as e:
    print(e)