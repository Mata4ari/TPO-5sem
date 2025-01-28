from BaseTest import VekTests
import time
from pages.CatalogPage import CatalogPage

class FilterTests(VekTests):
    def test_04(self):
        try:
            time.sleep(2)
            
            catalogPage = CatalogPage(self.driver)
            catalogPage.click_catalog_search()
            catalogPage.select_catalog('холодильник')
            
            time.sleep(2)
            catalogPage.click_chbox()
            catalogPage.click_filter_submit()
            names = catalogPage.get_names()
            res = True;
            for i in names:
                if('Idea' not in i.text):
                    res=False
            self.assertTrue(res, "Тест не пройден: 'LG' не найден в результатах.")

        except Exception as e:
            self.fail(f"Тест завершился с ошибкой: {e}")