from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/h2'))
        )
        self.searchbar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[1]/input'))
        )
        self.spotlightcard1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div/div[1]'))
        )
        self.spotlightcard2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div/div[2]'))
        )
        self.spotlightcard3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div/div[3]'))
        )
        self.spotlightcard4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div[3]/div/div[4]'))
        )
        self.aboutButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/ul/li[2]/a'))
        )
        self.resourcesButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/ul/li[3]/a'))
        )
        self.helpButton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/ul/li[4]/a'))
        )
        # footer buttons
        self.footerHome = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[1]'))
        )
        self.footerAbout = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[2]'))
        )
        self.footerDefense = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[3]'))
        )
        self.footerFOIA = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[4]'))
        )
        self.footerSection808 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[5]'))
        )
        self.footerStrategicPlans = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[6]'))
        )
        self.footerInfoQuality = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[7]'))
        )
        self.footerFearAct = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[8]'))
        )
        self.footerOpenGov = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[9]'))
        )
        self.footerPlainWriting = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[10]'))
        )
        self.footerPrivacyPol = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[11]'))
        )
        self.footerPrivacyProg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[12]'))
        )
        self.footerDoDCareers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[13]'))
        )
        self.footerWebPolicy = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[14]'))
        )
        self.footerPublicUseNotice = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[15]'))
        )
        self.footerUSAGov = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[16]'))
        )
        self.footerExternalLinks = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[17]'))
        )
        self.footerContactUs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/footer/div/div/div/a[18]'))
        )

    def validate_title_is_present(self):
        assert self.title.is_displayed()

    def validate_searchbar_is_present(self):
        assert self.searchbar.is_displayed()

    def validate_spotlightcard1_is_present(self):
        assert self.spotlightcard1.is_displayed()

    def validate_spotlightcard2_is_present(self):
        assert self.spotlightcard2.is_displayed()

    def validate_spotlightcard3_is_present(self):
        assert self.spotlightcard3.is_displayed()

    def validate_spotlightcard4_is_present(self):
        assert self.spotlightcard4.is_displayed()

    def validate_aboutButton_is_present(self):
        assert self.aboutButton.is_displayed()

    def validate_resourcesButton_is_present(self):
        assert self.resourcesButton.is_displayed()

    def validate_helpButton_is_present(self):
        assert self.helpButton.is_displayed()

#   footer functions

    def validate_footerhome_is_present(self):
        assert self.footerHome.is_displayed()

    def validate_footerabout_is_present(self):
        assert self.footerAbout.is_displayed()

    def validate_footerDefense_is_present(self):
        assert self.footerDefense.is_displayed()

    def validate_footerFOIA_is_present(self):
        assert self.footerFOIA.is_displayed()

    def validate_footerSection808_is_present(self):
        assert self.footerSection808.is_displayed()

    def validate_footerStrategicPlans_is_present(self):
        assert self.footerStrategicPlans.is_displayed()

    def validate_footerInfoQuality_is_present(self):
        assert self.footerInfoQuality.is_displayed()

    def validate_footerFearAct_is_present(self):
        assert self.footerFearAct.is_displayed()

    def validate_footerOpenGov_is_present(self):
        assert self.footerOpenGov.is_displayed()

    def validate_footerPlainWriting_is_present(self):
        assert self.footerPlainWriting.is_displayed()

    def validate_footerPrivacyPol_is_present(self):
        assert self.footerPrivacyPol.is_displayed()

    def validate_footerPrivacyProg_is_present(self):
        assert self.footerPrivacyProg.is_displayed()

    def validate_footerDoDCareers_is_present(self):
        assert self.footerDoDCareers.is_displayed()

    def validate_footerWebPolicy_is_present(self):
        assert self.footerWebPolicy.is_displayed()

    def validate_footerPublicUseNotice_is_present(self):
        assert self.footerPublicUseNotice.is_displayed()

    def validate_footerUSAGOV_is_present(self):
        assert self.footerUSAGov.is_displayed()

    def validate_footerExternalLinks_is_present(self):
        assert self.footerExternalLinks.is_displayed()

    def validate_footerContactUs_is_present(self):
        assert self.footerContactUs.is_displayed()

