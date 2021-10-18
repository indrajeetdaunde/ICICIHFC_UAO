import pytest
from page_objects.login_page import LoginPage
from test_data.new_application_page_data import NewApplicationPageData
from utility.base_class import BaseClass


class TestNewApplication(BaseClass):

    def test_new_application(self, get_data):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        log.info("Enter Username")
        login_page.get_username().clear()
        login_page.get_username().send_keys(get_data["username"])
        usr = login_page.get_username().get_attribute('value')
        log.info("Enter Password")
        login_page.get_password().clear()
        login_page.get_password().send_keys(get_data["password"])
        log.info("Click Login button")
        dashboard_page = login_page.click_login_button()
        self.verify_link_presence("h3[class='mb-0 mt-3']")
        dashboard_title = dashboard_page.get_dashboard_title().text
        print(dashboard_title)
        assert "Dashboard" == dashboard_title
        assert "Dashboard" in self.driver.title
        if dashboard_title == "Dashboard":
            for menu_list in dashboard_page.get_menu_list():
                menu_name = menu_list.text
                if menu_name == "New Application":
                    new_application_page = dashboard_page.get_menu()
                    page_title = new_application_page.get_page_title().text
                    assert page_title == "New Application"
                    break
        dashboard_page.click_profile().click()
        log.info("Click Logout")
        dashboard_page.click_sign_out().click()
        self.verify_link_presence("h3[class='m-t-20 text-center']")
        login_title = login_page.get_login_title().text
        print(login_title)
        assert "Unified Account Opening" == login_title
        assert "Unified Account Opening" == login_title

    @pytest.fixture(params=NewApplicationPageData.test_new_application_page_data)
    def get_data(self, request):
        return request.param
