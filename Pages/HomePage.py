from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

#inherited the BasePage
class HomePage(BasePage):
    # By locators
    CLOSE_MARK = (By.XPATH, "//button[@class = '_2KpZ6l _2doB4z']")
    FASHION_CATEGORY = (By.XPATH, "//div[contains(text(),'Fashion')]")
    WATCHES_ACCESSORIES = (By.XPATH, "//a[normalize-space()='Watches and Accessories']")
    All_ELEMENTS_IN_WATCHES_ACCESSORIES = (By.XPATH, "//div[@class = '_3XS_gI']/a")
    WALLETS = (By.XPATH, "//a[@class='_6WOcW9 _3YpNQe'][normalize-space()='Wallets']")

    # constructor to call the driver
    def __init__(self, driver):
        super().__init__(driver)  ##super() is used to call the parent class constructor
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    # user actions are created using below methods

    def click_on_close_popup(self):
        self.click_on_element(self.CLOSE_MARK)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def hover_on_fashion(self):
        self.mouse_hover(self.FASHION_CATEGORY)

    def hover_on_watches_accessories(self):
        self.mouse_hover(self.WATCHES_ACCESSORIES)

    def get_all_elements_count(self):
        elements = self.driver.find_elements(*HomePage.All_ELEMENTS_IN_WATCHES_ACCESSORIES)
        return len(elements)

    def get_all_elements(self):
        list_elements = []
        elements = self.driver.find_elements(*HomePage.All_ELEMENTS_IN_WATCHES_ACCESSORIES)
        for element in elements:
            text = element.text
            list_elements.append(text)
        return list_elements

    def click_on_wallets(self):
        self.click_on_element(self.WALLETS)
