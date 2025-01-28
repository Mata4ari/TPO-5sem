from BaseTest import VekTests
from pages.MainPage import MainPage
import time

class LoginTests(VekTests):
    def test_01(self):
        test_credentials = [
            ('ffllyfnya@gmail.com', '2004010203'),
        ]

        for email, password in test_credentials:
            with self.subTest(email=email, password=password):
                try:
                    mainPage = MainPage(self.driver)
                    
                    mainPage.click_ToolsToggler()
                    
                    mainPage.click_userToolsBtn()
                    
                    mainPage.enter_email(email)
                    mainPage.enter_login_password(password)
                    mainPage.click_login_submit()
                    mainPage.click_modal_close()
                    time.sleep(1)
                    mainPage.click_ToolsToggler()
                    mail = mainPage.get_user_mail()

                    print('mail: '+mail+'\n')
                    self.assertEqual(mail, email, "")
                except Exception as e:
                    self.fail(f"Тест завершился с ошибкой: {e}")