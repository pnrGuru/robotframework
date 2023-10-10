# finance_page.py
class FinancePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_link = "xpath=//a[text()='Sign in']"

    def click_sign_in_link(self):
        self.driver.click_element(self.sign_in_link)

