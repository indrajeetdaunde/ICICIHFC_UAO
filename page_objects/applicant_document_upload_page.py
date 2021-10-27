from selenium.webdriver.common.by import By


class ApplicantDocumentUploadPage:
    list_of_upload_buttons = (By.XPATH, "//div[@id='vapp']/div/div[1]/div")
    document_upload_page_title = (By.CSS_SELECTOR, '.page-title')

    def __init__(self, driver):
        self.driver = driver

    def get_list_of_upload_button(self):
        return self.driver.find_elements(*ApplicantDocumentUploadPage.list_of_upload_buttons)

    def get_document_upload_page_title(self):
        return self.driver.find_element(*ApplicantDocumentUploadPage.document_upload_page_title)
