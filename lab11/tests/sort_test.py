from BaseTest import VekTests
import time
from pages.CatalogPage import CatalogPage

class SortTests(VekTests):
    def test_03(self):
        try:
            time.sleep(1)
            catalogPage = CatalogPage(self.driver)
            catalogPage.click_catalog_search()
            catalogPage.select_catalog('холодильник')
            catalogPage.click_sortTools()
            time.sleep(4)
            catalogPage.click_sortTools()
            time.sleep(4)
            catalogPage.get_ascIcon()
            time.sleep(1)
            print('test passed')

        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {e}")