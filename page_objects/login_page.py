from selenium.webdriver.common.by import By

from page_objects.applicant_document_upload_page import ApplicantDocumentUploadPage
from page_objects.dashboard_page import DashboardPage


class LoginPage:

    username = (By.CSS_SELECTOR, "#_username")
    password = (By.CSS_SELECTOR, "#Password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    login_title = (By.CSS_SELECTOR, "h3[class='m-t-20 text-center']")
    blank_password_error_msg = (By.CSS_SELECTOR, "#Password-error")
    invalid_credentials_msg = (By.CSS_SELECTOR, "div[class='text-danger validation-summary-errors'] ul li")

    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.login_button).click()
        # dashboard_page = DashboardPage(self.driver)
        document_upload_pge = ApplicantDocumentUploadPage(self.driver)
        #return dashboard_page
        return document_upload_pge

    def get_login_title(self):
        return self.driver.find_element(*LoginPage.login_title)

    def get_blank_password_error_msgs(self):
        return self.driver.find_elements(*LoginPage.blank_password_error_msg)

    def get_invalid_credentials_error_msgs(self):
        return self.driver.find_elements(*LoginPage.invalid_credentials_msg)

    def get_blank_password_error_msg(self):
        return self.driver.find_element(*LoginPage.blank_password_error_msg)

    def get_invalid_credentials_error_msg(self):
        return self.driver.find_element(*LoginPage.invalid_credentials_msg)
