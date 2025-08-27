import time

from helper.po_utils import PageObjectUtils as utils


class Main_functions_poo(utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__button_locator = "//*[self::button or self::a or @role='button'][contains(normalize-space(.), '{}')]"
        self.__button_locator_submit = "//button[self::button or self::a or @class='action submit primary'][contains(normalize-space(.), '{}')]"
        self.__form_fields = "//*[self::label or self:: span][contains(normalize-space(.), '{}')]/following::input"

    def open_url(self, url):
        try:
            self.driver.get(f'https://{url}')

        except Exception as e:
            raise ValueError(f"It was an error opening the url:{e}")

    def click_on_button(self, button_name):
        try:
            button_locator = self.wait_until_clickable(self.__button_locator.format(button_name))
            self.highlight(button_locator)
            button_locator.click()
        except Exception as e:
            raise ValueError(f"It was an error clicking the button:{button_name}")

    def fill_form(self, field_name, value):
        try:
            field = self.wait_until_presence_of_element(self.__form_fields.format(field_name))
            self.highlight(field)
            field.send_keys(value)
        except Exception as e:
            raise ValueError(f"It was an error locating the field: {value}")

    def click_on_button_submit(self, button_name):
        try:
            button_locator = self.wait_until_clickable(self.__button_locator_submit.format(button_name))
            self.highlight(button_locator)
            button_locator.click()
        except Exception as e:
            raise ValueError(f"It was an error clicking the button:{button_name}")


