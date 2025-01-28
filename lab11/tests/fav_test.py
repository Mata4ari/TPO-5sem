from BaseTest import VekTests
import time
from pages.ProductPage import ProductPage

class FavTests(VekTests):
    def test_02(self):
        try:

            productPage = ProductPage(self.driver)
            time.sleep(1)
            productPage.open()
            productPage.click_fav_btn()
            aria_label = productPage.get_attribute()
            time.sleep(1);
            print('label: '+aria_label+'\n')
            self.assertEqual(aria_label, 'В избранном', "")
        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {e}")