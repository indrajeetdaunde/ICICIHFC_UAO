import pytest

from page_objects.login_page import LoginPage
from test_data.upload_documents_page_data import UploadDocumentsPageData
from utility.base_class import BaseClass


class TestUploadDocuments(BaseClass):

    def test_upload_documents(self, get_data):
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
        document_upload_page = login_page.click_login_button()
        self.verify_link_presence(".page-title")
        document_upload_page_title = document_upload_page.get_document_upload_page_title().text
        assert "Upload Documents" in document_upload_page_title

    @pytest.fixture(params=UploadDocumentsPageData.proof_of_identity_page_data)
    def get_data(self, request):
        return request.param

