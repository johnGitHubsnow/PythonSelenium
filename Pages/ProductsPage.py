from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ProductsPage(BasePage):

    BRAND_DROP_DOWN = (By.XPATH, "//div[contains(text(),'Brand')]")
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Search Brand']")
    CHECKBOX = (By.XPATH, "//div[@class='_24_Dny']")
    PRODUCTS = (By.XPATH, "//img[@class='_2r_T1I']")
    ADD_TO_CART = (By.XPATH, "//button[normalize-space()='ADD TO CART']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_brand_dropdown(self):
        self.click_on_element(self.BRAND_DROP_DOWN)

    def send_fastrack_text_to_search_box(self):
        self.send_text(self.SEARCH_FIELD, "fastrack")

    def click_on_checkbox(self):
        self.click_on_element(self.CHECKBOX)

    def clear_text_on_search_box(self):
        self.clear_text(self.SEARCH_FIELD)

    def send_wrogn_text_to_search_box(self):
        self.send_text(self.SEARCH_FIELD, "wrogn")

    def send_jsn_text_to_search_box(self):
        self.send_text(self.SEARCH_FIELD, "jsn")

    def select_third_product(self):
        products = self.driver.find_elements(*ProductsPage.PRODUCTS)
        for i in range(10):
            if i == 2:
                self.click_on_element(products[i])
                break

    def switch_to_handle(self):
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        print("current handle", current_handle)
        print("all handles", all_handles)
        for handle in all_handles:
            print(self.driver.title)
            if not handle == current_handle:
                self.driver.switch_to.window(handle)
                break

    def click_on_add_to_cart(self):
        self.click_on_element(self.ADD_TO_CART)