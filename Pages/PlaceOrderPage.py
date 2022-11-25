from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class PlaceOrderPage(BasePage):
    USERNAME = (By.XPATH, "//input[@type='text']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    INVALID_MESSAGE = (By.XPATH, "//span[contains(text(),'Please "
                                 "enter valid Email ID/Mobile number')]")

    def __init__(self, driver):
        super().__init__(driver)

    def send_invalid_email(self):
        self.send_text(self.USERNAME, TestData.INVALID_EMAIL)

    def submit_button(self):
        self.click_on_element(self.SUBMIT_BUTTON)

    def send_valid_number(self):
        self.send_text(self.USERNAME, TestData.VALID_NUMBER)

    def send_password(self):
        self.send_text(self.PASSWORD, TestData.VALID_PASSWORD)

    def return_invalid_message(self):
        return self.driver.find_element(*PlaceOrderPage.INVALID_MESSAGE).get_attribute("innerText")

    def clear_user_name_text(self):
        self.clear_text(self.USERNAME)
