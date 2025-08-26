from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from telnetlib import EC


class Main_functions_poo:
    def __init__(self, driver):
        self.driver = driver
        self.__button_locator = "//button[.//*[normalize-space(text())='{}']]"

    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            raise ValueError(f"It was an error opening the url:{e}")

    def click_on_button(self, button_name):
        try:
            button_locator = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.__button_locator.format(button_name)))
            )
            button_locator.click()
        except Exception as e:
            raise ValueError(f"It was an error clicking the button:{e}")

