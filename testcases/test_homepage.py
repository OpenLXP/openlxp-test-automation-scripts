import HtmlTestRunner
import unittest
from selenium import webdriver
from values import strings
from pageobjects import homepage


class Test_homepage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\aktailor\PycharmProjects\chromedriver.exe")
        cls.driver.get(strings.base_url)

    def test_home_screen_title_searchbar(self):
        driver = self.driver
        home_screen = homepage.Homepage(driver)
        # check search bar and title
        home_screen.validate_title_is_present()
        home_screen.validate_searchbar_is_present()

    def test_home_screen_navbar(self):
        driver = self.driver
        home_screen = homepage.Homepage(driver)
        # check the navigation bar and its buttons are present
        home_screen.validate_aboutButton_is_present()
        home_screen.validate_resourcesButton_is_present()
        home_screen.validate_helpButton_is_present()

    def test_home_screen_spotlight(self):
        driver = self.driver
        home_screen = homepage.Homepage(driver)
        # search the homepage for the following objects
        home_screen.validate_spotlightcard1_is_present()
        home_screen.validate_spotlightcard2_is_present()
        home_screen.validate_spotlightcard3_is_present()
        home_screen.validate_spotlightcard4_is_present()

    def test_home_screen_footer(self):
        driver = self.driver
        home_screen = homepage.Homepage(driver)

        home_screen.validate_footerhome_is_present()
        home_screen.validate_footerabout_is_present()
        home_screen.validate_footerDefense_is_present()
        home_screen.validate_footerFOIA_is_present()
        home_screen.validate_footerSection808_is_present()
        home_screen.validate_footerStrategicPlans_is_present()
        home_screen.validate_footerInfoQuality_is_present()
        home_screen.validate_footerFearAct_is_present()
        home_screen.validate_footerOpenGov_is_present()
        home_screen.validate_footerPlainWriting_is_present()
        home_screen.validate_footerPrivacyPol_is_present()
        home_screen.validate_footerPrivacyProg_is_present()
        home_screen.validate_footerDoDCareers_is_present()
        home_screen.validate_footerWebPolicy_is_present()
        home_screen.validate_footerPublicUseNotice_is_present()
        home_screen.validate_footerUSAGOV_is_present()
        home_screen.validate_footerExternalLinks_is_present()
        home_screen.validate_footerContactUs_is_present()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


html_report_dir = 'C:/Users/aktailor/PycharmProjects/ECCTesting/reports'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(Test_homepage('test_home_screen_title_searchbar'))
    suite.addTest(Test_homepage('test_home_screen_navbar'))
    suite.addTest(Test_homepage('test_home_screen_spotlight'))
    suite.addTest(Test_homepage('test_home_screen_footer'))

    runner = HtmlTestRunner.HTMLTestRunner(
        output=html_report_dir, verbosity=2, report_title='ECC Homepage Test Results')
    runner.run(suite)
