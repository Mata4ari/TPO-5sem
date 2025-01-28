import unittest
from tests.login_test import LoginTests
from tests.fav_test import FavTests
from tests.filter_test import FilterTests
from tests.sort_test import SortTests
#import html_testRunner             




if __name__ == "__main__":
    suite = unittest.TestSuite()
    
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTests))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(FavTests))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SortTests))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(FilterTests))
    #with open("test_report.html", "wb") as report_file:
     #   runner = html_testRunner.HTMLTestRunner(stream=report_file, title='Отчет о результатах тестирования', description='Результаты тестов для 21vek.by')
     #   runner.run(suite)
    with open('test_report.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f)  
        runner.run(suite)