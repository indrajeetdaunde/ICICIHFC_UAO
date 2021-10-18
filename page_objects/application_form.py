from selenium.webdriver.common.by import By


class ApplicationForm:
    page_title_text = (By.CSS_SELECTOR, ".page-title")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title_text(self):
        return self.driver.find_element(*ApplicationForm.page_title_text)
