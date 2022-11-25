import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class ShoppingCartPage(BasePage):

    INCREASE_COUNT = (By.XPATH, "//button[normalize-space()='+']")
    DECREASE_COUNT = (By.XPATH, "//button[text()='–']")
    COUNT_TEXT = (By.XPATH, "//input[@class = '_253qQJ']")
    PLACE_ORDER = (By.XPATH, "//span[text()='Place Order']")

    def __init__(self, driver):
        super().__init__(driver)

    def increase_quantity_of_product(self):
        count_positive = 0
        for i in range(1, 4):
            self.click_on_element(self.INCREASE_COUNT)
            count_positive += 1
        return count_positive

    def original_count_of_products(self):
        original_count = self.driver.find_element(*ShoppingCartPage.COUNT_TEXT).get_attribute("value")
        return original_count

    def decrease_quantity_of_products(self):
        count_negative = 4
        for i in range(1, 4):
            self.click_on_element(self.DECREASE_COUNT)
            time.sleep(3)
            count_negative -= 1
        return count_negative

    def click_on_place_order(self):
        self.click_on_element(self.PLACE_ORDER)











