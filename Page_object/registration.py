# registration_page.py
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = "id=first_name"
        self.last_name_field = "id=last_name"


    def fill_registration_form(self, first_name, last_name, email, password):
        self.driver.input_text(self.first_name_field, first_name)
        self.driver.input_text(self.last_name_field, last_name)
       

    def submit_registration_form(self):
        self.driver.click_button("xpath=//button[@type='submit']")
