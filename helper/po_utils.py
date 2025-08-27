from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObjectUtils:
    def __init__(self, driver):
        self.driver = driver

    def highlight(self, element, duration=800):
        script = """
            const el = arguments[0];
            const prev = el.style.border;
            el.style.border = '5px solid yellow';
            setTimeout(() => { el.style.border = prev; }, arguments[1]);
        """
        self.driver.execute_script(script, element, duration)

    def wait_until_clickable(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        return element

    def wait_until_presence_of_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element
