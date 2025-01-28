from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.common.keys import Keys
#import html_testRunner 




class VekTests(unittest.TestCase):
    def setUp(self):
            chrome_options = Options()
            chrome_options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get('https://www.21vek.by/')
            button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'AgreementCookie_reject__f5oqP')))
            button.click()
            btn2 = self.driver.find_element(By.CLASS_NAME,'Button-module__gray-secondary')
            btn2.click()
            

    #@unittest.skip("")
    def test_01(self):
        test_credentials = [
            ('ffllyfnya@gmail.com', '2004010203'),
        ]

        for email, password in test_credentials:
            with self.subTest(email=email, password=password):
                try:
                    btn3 = self.driver.find_element(By.CLASS_NAME,'styles_userToolsToggler__c2aHe')
                    btn3.click()
                    btn4 = self.driver.find_element(By.CLASS_NAME,'userToolsBtn')
                    btn4.click()
                    inp1 = self.driver.find_element(By.ID,'login-email')
                    inp1.send_keys(email)
                    inp2 = self.driver.find_element(By.ID,'login-password')
                    inp2.send_keys(password)
                    #btn5 = self.driver.find_element(By.CLASS_NAME,'EmailLoginForm_baseActionButton__OAFqW')
                    btn5 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='loginSubmit']")))
                    btn5.click()
                    time.sleep(2);
                    btn6 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='modalClose']")))
                    btn6.click()
                    btn4 = self.driver.find_element(By.CLASS_NAME,'styles_userToolsToggler__c2aHe')
                    btn4.click()
                    time.sleep(1);
                    mail = self.driver.find_element(By.CLASS_NAME,'userToolsSubtitle')
                    print('mail: '+mail.text+'\n')
                    self.assertEqual(mail.text, email, "")
                except Exception as e:
                    self.fail(f"Тест завершился с ошибкой: {e}")

    #@unittest.skip("")
    def test_02(self):
        try:
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                print(cookie)

            time.sleep(1)
            self.driver.get('https://www.21vek.by/portable_audio/2yndx00026vio_yandex_9211399.html?recommendationId=ab0424e8d159447f97fb1918a2241d52')
            btn7 = self.driver.find_element(By.CLASS_NAME,'FavoritesButton_button__oIuqE')
            btn7.click()
            aria_label = btn7.get_attribute('aria-label')
            self.driver.save_screenshot('screenshot.png')
            time.sleep(2);
            print('label: '+aria_label+'\n')
            self.assertEqual(aria_label, 'В избранном', "")
        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {e}")

    #@unittest.expectedFailure
    def test_03(self):
        try:
            time.sleep(2)
            
            inp3 = self.driver.find_element(By.ID, 'catalogSearch')
            inp3.click()
            inp3.send_keys('холодильник')
            inp3.send_keys(Keys.RETURN)
            btn3 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.cr-tools-sort__bi')))
            btn3.click()
            time.sleep(2)
            btn3.click()
            btn3 = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'g-cr-asc')))
            time.sleep(2)
            print('test passed')

        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {e}")
    
    #@unittest.skip("")
    def test_04(self):
        try:
            time.sleep(2)
            
            inp3 = self.driver.find_element(By.ID, 'catalogSearch')
            inp3.click()
            inp3.send_keys('холодильник')
            inp3.send_keys(Keys.RETURN)
            
            time.sleep(2)
            checkbox = self.driver.find_element(By.CSS_SELECTOR,'label[title="LG"]')
            checkbox.click()
            btn4 = self.driver.find_element(By.CLASS_NAME,'filter-controls__submit')
            btn4.click()
            names = self.driver.find_elements(By.CLASS_NAME,'result__name')
            res = True;
            for i in names:
                if('LG' not in i.text):
                    res=False
            self.assertTrue(res, "Тест не пройден: 'LG' не найден в результатах.")

        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {e}")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    #suite.addTest(VekTests('test_01'))
    #suite.addTest(VekTests('test_02'))
    #suite.addTest(VekTests('test_03'))
    #suite.addTest(VekTests('test_04'))
    #with open("test_report.html", "wb") as report_file:
     #   runner = html_testRunner.HTMLTestRunner(stream=report_file, title='Отчет о результатах тестирования', description='Результаты тестов для 21vek.by')
     #   runner.run(suite)
    with open('test_report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f)  
        runner.run(suite)