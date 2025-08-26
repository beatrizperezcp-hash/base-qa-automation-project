class PageObjectUtils:
    def __init__(self, driver):
        self.driver = driver

    def highlight(self, element):
        self.driver.execure_script("argument[0].style.border = '5px solid yellow'", element)
