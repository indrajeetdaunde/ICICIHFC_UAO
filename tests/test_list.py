import pytest
from selenium.webdriver.support.select import Select
from page_objects.login_page import LoginPage
from test_data.new_application_page_data import NewApplicationPageData
from utility.base_class import BaseClass


class TestList(BaseClass):

    def test_list(self, get_application_data):
        log = self.get_logger()
        login_page = LoginPage(self.driver)

        # clear username field and enter username
        login_page.get_username().clear()
        login_page.get_username().send_keys(get_application_data["username"])

        # clear password field and enter password
        login_page.get_password().clear()
        login_page.get_password().send_keys(get_application_data["password"])

        # click login button
        dashboard_page = login_page.click_login_button()

        # wait till the time dashboard page appears
        self.verify_link_presence("h3[class='mb-0 mt-3']")

        assert self.driver.title == "Dashboard - Unified Account Opening"
        for menu_list in dashboard_page.get_menu_list():
            menu_name = menu_list.text
            if menu_name == "New Application":
                new_application_page = dashboard_page.get_menu()
                self.verify_link_presence(".kt-subheader__title")
                assert new_application_page.get_page_title().text == "New Application"
                break

        log.info("Enter Applicant Name")
        new_application_page.get_applicant_name().send_keys(get_application_data["applicant_name"])

        log.info("Enter Applicant Email ID")
        new_application_page.get_applicant_email().send_keys(get_application_data["applicant_email"])

        log.info("Enter Applican Mobile Number")
        new_application_page.get_applicant_mobile().send_keys(get_application_data["applicant_mobile"])

        log.info("Choose Applicant type as Individual")
        customer_type = Select(new_application_page.get_customer_type())
        customer_type.select_by_visible_text("Individual")

        log.info("Get list of branches")
        branches = []
        for branch in new_application_page.get_branch_list():
            branches.append(branch.text)

        log.info("Choose Branch as Thane-B")
        branch_name = Select(new_application_page.get_branch())
        branch_name.select_by_visible_text("THANE-B")
        print(branches)

        log.info("Get List of searched locations")
        new_application_page.get_location().click()
        self.verify_text_presence("//li[text()='NAGTHANE']")
        locations_list = new_application_page.get_searched_location_list()
        locations = []
        for location in locations_list:
            locations.append(location.text)
        print(locations)

        log.info("Choose Anand Nagar Location")
        new_application_page.get_search_location_text().send_keys(get_application_data["search_location"])
        self.verify_text_presence("//li[text()='NAGTHANE']")
        location_name_list = new_application_page.get_searched_location_list_xpath()
        i = 0
        for i in range(0, len(location_name_list)):
            i = i + 1
            location_name = new_application_page.get_searched_location_list_xpath()[i]
            if location_name.text == "NAGTHANE":
                location_name.click()
                break

        log.info("Get list of Brokers")
        new_application_page.get_broker().click()
        self.verify_text_presence("//li[text()='AK2010202']")
        brokers_list = new_application_page.get_searched_broker_list()
        brokers = []
        for broker in brokers_list:
            brokers.append(broker.text)
        print(brokers)

        log.info("Choose AK2010202 broker")
        new_application_page.get_search_location_text().send_keys(get_application_data["search_broker"])
        self.verify_text_presence("//li[text()='AK2010202']")
        m = 0
        broker_name_list = new_application_page.get_searched_broker_list_xpath()
        for m in range(0, len(broker_name_list)):
            m = m + 1
            broker_name = new_application_page.get_searched_broker_list_xpath()[m]
            if broker_name.text == 'AK2010202':
                broker_name.click()
                break

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
