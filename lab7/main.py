from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome() 
driver.get("https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BB%D0%BE%D0%B4%D0%B5%D1%80%D0%B1%D0%B5%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B5_%D1%81%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B5_%D0%BC%D1%83%D0%BD%D0%B8%D1%86%D0%B8%D0%BF%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5")


try:
    element1 = driver.find_element(By.CSS_SELECTOR, 'span.mw-page-title-main')
    elements2 = driver.find_elements(By.CSS_SELECTOR,"div.mw-content-ltr > p")
    element3 = driver.find_element(By.CSS_SELECTOR,'a[href="/wiki/%D0%A1%D0%B5%D0%BB%D1%8C%D1%81%D0%BA%D0%BE%D0%B5_%D0%BF%D0%BE%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5"]')
    print(element1.text)
    print(len(elements2))
    print(element3.text+'\n')
except NoSuchElementException:
    print("Элемент не найден")


try:
    element4 = driver.find_element(By.XPATH,'//a[@href="/wiki/%D0%9C%D0%B0%D0%BB%D0%BE%D0%B4%D0%B5%D1%80%D0%B1%D0%B5%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D1%80%D0%B0%D0%B9%D0%BE%D0%BD"]')
    element5 = driver.find_element(By.XPATH,'//button[@title="Установки языка"]')
    element6 = driver.find_element(By.XPATH,'//div[@class="toctitle"]//h2')
    print(element4.text)
    print(element5.tag_name)
    print(element6.text+'\n')
except:
    print("Элемент не найден")

try:
    elemetnts7 = driver.find_elements(By.TAG_NAME,'div')
    element8 =driver.find_element(By.PARTIAL_LINK_TEXT,'2004')
    print(len(elemetnts7))
    print(element8.text)
except:
    print("Элемент не найден")

