from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class Searchbar:
    def __init__(self, driver):
        self.driver = driver

        self.searchbar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[1]/input'))
        )

        self.submitButton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div/div[1]/button'))
        )

    def validate_searchbar_is_clickable(self):
        assert self.searchbar.is_displayed()

    def validate_submit_button_is_clickable(self):
        assert self.submitButton.is_displayed()
