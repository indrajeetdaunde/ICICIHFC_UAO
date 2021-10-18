from selenium.webdriver.common.by import By
from page_objects.application_form import ApplicationForm


class NewApplication:

    page_title = (By.CSS_SELECTOR, ".kt-subheader__title")
    applicant_name = (By.CSS_SELECTOR, "#Name")
    applicant_email = (By.CSS_SELECTOR, "#Email")
    applicant_mobile = (By.CSS_SELECTOR, "#Mobile")
    customer_type = (By.CSS_SELECTOR, "#CustomerTypeID")
    branch = (By.CSS_SELECTOR, "#BranchID")
    branch_list = (By.CSS_SELECTOR, "#BranchID option")
    location = (By.CSS_SELECTOR, "#select2-LocationID-container")
    search_location_text = (By.CSS_SELECTOR, ".select2-search__field")
    searched_location_list = (By.CSS_SELECTOR, ".select2-results__options li")
    searched_location_list_xpath = (By.XPATH, "//ul[@class='select2-results__options']/li")
    broker = (By.CSS_SELECTOR, "#select2-ddlVendor-container")
    search_broker_text = (By.CSS_SELECTOR, ".select2-search__field")
    searched_broker_list = (By.CSS_SELECTOR, ".select2-results__options li")
    searched_broker_list_xpath = (By.XPATH, "//ul[@class='select2-results__options']/li")
    save_application_button = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(*NewApplication.page_title)

    def get_applicant_name(self):
        return self.driver.find_element(*NewApplication.applicant_name)

    def get_applicant_email(self):
        return self.driver.find_element(*NewApplication.applicant_email)

    def get_applicant_mobile(self):
        return self.driver.find_element(*NewApplication.applicant_mobile)

    def get_customer_type(self):
        return self.driver.find_element(*NewApplication.customer_type)

    def get_branch(self):
        return self.driver.find_element(*NewApplication.branch)

    def get_branch_list(self):
        return self.driver.find_elements(*NewApplication.branch_list)

    def get_location(self):
        return self.driver.find_element(*NewApplication.location)

    def get_search_location_text(self):
        return self.driver.find_element(*NewApplication.search_location_text)

    def get_searched_location_list(self):
        return self.driver.find_elements(*NewApplication.searched_location_list)

    def get_searched_location_list_xpath(self):
        return self.driver.find_elements(*NewApplication.searched_location_list_xpath)

    def get_broker(self):
        return self.driver.find_element(*NewApplication.broker)

    def get_search_broker_text(self):
        return self.driver.find_element(*NewApplication.search_broker_text)

    def get_searched_broker_list(self):
        return self.driver.find_elements(*NewApplication.searched_broker_list)

    def get_searched_broker_list_xpath(self):
        return self.driver.find_elements(*NewApplication.searched_broker_list_xpath)

    def click_save_application_button(self):
        self.driver.find_element(*NewApplication.save_application_button).click()
        application_form = ApplicationForm(self.driver)
        return application_form
