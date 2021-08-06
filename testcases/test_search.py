import HtmlTestRunner
import unittest
from selenium import webdriver
from values import strings
from pageobjects import searchbar

class Test_Search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\aktailor\PycharmProjects\chromedriver.exe")
        cls.driver.get(strings.base_url)

    def test_search(self):
        driver = self.driver
        search_bar = searchbar.Searchbar(driver)

        search_bar.validate_searchbar_is_clickable()
        searchbox = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/input')
        searchbox.send_keys('Math')

        search_bar.validate_submit_button_is_clickable()
        submitbutton = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/button')
        submitbutton.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

html_report_dir = 'C:/Users/aktailor/PycharmProjects/ECCTesting/reports'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(Test_Search('test_search'))

    runner = HtmlTestRunner.HTMLTestRunner(
        output=html_report_dir, verbosity=2, report_title='ECC Search Functionality Test Results')
    runner.run(suite)
