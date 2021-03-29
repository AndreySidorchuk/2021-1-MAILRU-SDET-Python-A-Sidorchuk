from selenium.webdriver.common.keys import Keys

from ui.pages.BasePage import BasePage
from ui.locators.locators import AuthorizationLocators


class AuthorizationPage(BasePage):
    locators = AuthorizationLocators()

    def authorize(self, email, password):
        self.click(self.locators.LOGIN_BUTTON)
        email_field = self.find(self.locators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)
        password_field = self.find(self.locators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
