import logging
import time

import pytest

from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.PlaceOrderPage import PlaceOrderPage
from Pages.ProductsPage import ProductsPage
from Pages.ShoppinCartPage import ShoppingCartPage
from Tests.test_base import BaseTest

#inherited the BaseTest

class Test_Home(BaseTest):

    def test_flipkart_application_end_to_end(self):
        self.home_page = HomePage(self.driver)         #creating home page object
        self.home_page.click_on_close_popup()          #using home_page object reference calling the methods

        self.home_page.hover_on_fashion()

        self.home_page.hover_on_watches_accessories()

        count_of_ele = self.home_page.get_all_elements_count()
        assert count_of_ele == TestData.COUNT_OF_ELEMENTS      # validating the count

        list_of_ele = self.home_page.get_all_elements()
        print(list_of_ele)

        self.home_page.click_on_wallets()

        self.products_page = ProductsPage(self.driver)        #product page object is created

        self.products_page.click_on_brand_dropdown()          #product_page object reference is used to call the methods
        self.products_page.send_fastrack_text_to_search_box()
        self.products_page.click_on_checkbox()

        self.products_page.click_on_brand_dropdown()
        self.products_page.clear_text_on_search_box()
        self.products_page.send_wrogn_text_to_search_box()
        self.products_page.click_on_checkbox()

        self.products_page.click_on_brand_dropdown()
        self.products_page.clear_text_on_search_box()
        self.products_page.send_jsn_text_to_search_box()
        self.products_page.click_on_checkbox()

        self.products_page.select_third_product()


        self.products_page.switch_to_handle()


        self.products_page.click_on_add_to_cart()


        self.shopping_cart_page = ShoppingCartPage(self.driver)   #shoping cart page object is created

        actual_positive_count = self.shopping_cart_page.increase_quantity_of_product()
        expected_positive_count = self.shopping_cart_page.original_count_of_products()
        assert str(actual_positive_count) == str(expected_positive_count)

        actual_negative_count = self.shopping_cart_page.decrease_quantity_of_products()
        expected_negative_count = self.shopping_cart_page.original_count_of_products()
        assert str(actual_negative_count) == str(expected_negative_count)

        self.shopping_cart_page.click_on_place_order()

        self.place_order_page = PlaceOrderPage(self.driver)
        self.place_order_page.send_invalid_email()
        self.place_order_page.submit_button()
        invalid_text = self.place_order_page.return_invalid_message()
        assert invalid_text == TestData.VALIDATE_INVALID_MESSAGE

        self.place_order_page.clear_user_name_text()
        self.place_order_page.send_valid_number()
        self.place_order_page.submit_button()
        self.place_order_page.send_password()
        self.place_order_page.submit_button()











