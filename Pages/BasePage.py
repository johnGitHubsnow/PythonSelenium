from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver      #constructor-- for calling the driver

    def click_on_element(self, by_locator):      # clicking on webelement
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).click()

    def send_text(self, by_locator, text):       # sending text to webelement
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_text(self, by_locator):            # clearing the text
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(by_locator)).clear()

    def get_title(self, title):                  # getting page title
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    def mouse_hover(self, by_locator):           # mouse hovering on elements
        action = ActionChains(self.driver)
        mouse_act = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(by_locator))
        action.move_to_element(mouse_act).perform()

