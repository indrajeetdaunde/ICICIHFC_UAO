import pytest
from selenium.webdriver.support.select import Select
from page_objects.login_page import LoginPage
from test_data.new_application_page_data import NewApplicationPageData
from utility.base_class import BaseClass


class TestCreateNewApplication(BaseClass):

    def test_create_new_application(self, get_application_data):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        log.info("Enter Username")
        login_page.get_username().clear()
        login_page.get_username().send_keys(get_application_data["username"])
        usr = login_page.get_username().get_attribute('value')
        log.info("Enter Password")
        login_page.get_password().clear()
        login_page.get_password().send_keys(get_application_data["password"])
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

        log.info("Enter Applicant Name")
        new_application_page.get_applicant_name().clear()
        new_application_page.get_applicant_name().send_keys(get_application_data["applicant_name"])

        log.info("Enter Applicant Email Id")
        new_application_page.get_applicant_email().clear()
        new_application_page.get_applicant_email().send_keys(get_application_data["applicant_email"])

        log.info("Enter Applicant Mobile Number")
        new_application_page.get_applicant_mobile().clear()
        new_application_page.get_applicant_mobile().send_keys(get_application_data["applicant_mobile"])

        log.info("Choose Customer type")
        customer_type = Select(new_application_page.get_customer_type())
        customer_type.select_by_visible_text("Individual")

        log.info("Choose branch")
        branch = Select(new_application_page.get_branch())
        branch.select_by_visible_text("THANE-B")

        log.info("Choose Location")
        new_application_page.get_location().click()

        log.info("Choose Search Location")
        self.verify_link_presence(".select2-search__field")
        new_application_page.get_search_location_text().send_keys(get_application_data["search_location"])
        self.verify_link_presence(".select2-results__option--highlighted")
        log.info("Choose searched location")
        location_list = new_application_page.get_searched_location_list()

        for location in location_list:
            if location.text == "NAGTHANE":
                location.click()
                break

        log.info("Choose Broker")
        new_application_page.get_broker().click()

        log.info("Choose Search Broker")
        self.verify_link_presence(".select2-search__field")
        new_application_page.get_search_broker_text().send_keys(get_application_data["search_broker"])
        self.verify_link_presence(".select2-results__option--highlighted")
        log.info("Choose searched Broker")
        broker_list = new_application_page.get_searched_broker_list()
        for broker in broker_list:
            if broker.text == "AK2010202":
                broker.click()
                break
        application_form = new_application_page.click_save_application_button()
        self.verify_link_presence(".page-title")
        application_form_title = application_form.get_page_title_text().text
        assert 'Upload Documents' in application_form_title
        dashboard_page.click_profile().click()
        log.info("Click Logout")
        dashboard_page.click_sign_out().click()
        self.verify_link_presence("h3[class='m-t-20 text-center']")
        login_title = login_page.get_login_title().text
        print(login_title)
        assert "Unified Account Opening" == login_title

    @pytest.fixture(params=NewApplicationPageData.test_new_application_page_data)
    def get_application_data(self, request):
        return request.param