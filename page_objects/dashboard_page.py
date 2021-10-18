from selenium.webdriver.common.by import By
from page_objects.new_application_page import NewApplication


class DashboardPage:

    dashboard_title = (By.CSS_SELECTOR, "h3[class='mb-0 mt-3']")
    profile = (By.CSS_SELECTOR, ".kt-header__topbar-user")
    sign_out = (By.XPATH, "//a[text()='Sign Out']")
    menu_list = (By.XPATH, "//div[contains(@class,'kt-aside-menu-wrapper')]/div/ul/li")
    menu = (By.XPATH, "//div[contains(@class,'kt-aside-menu-wrapper')]/div/ul/li[2]/a/span[1]")

    def __init__(self, driver):
        self.driver = driver

    def get_dashboard_title(self):
        return self.driver.find_element(*DashboardPage.dashboard_title)

    def click_profile(self):
        return self.driver.find_element(*DashboardPage.profile)

    def click_sign_out(self):
        return self.driver.find_element(*DashboardPage.sign_out)

    def get_menu_list(self):
        return self.driver.find_elements(*DashboardPage.menu_list)

    def get_menu(self):
        self.driver.find_element(*DashboardPage.menu).click()
        new_application_page = NewApplication(self.driver)
        return new_application_page
