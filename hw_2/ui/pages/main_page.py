from .base_page import BasePage
from .dashboard_page import DashboardPage
from ui.locators.locators import MainPageLocators


class MainPage(BasePage):

    URL = 'https://target.my.com/'
    locators = MainPageLocators()

    def login(self, login, password):
        """Авторизация (логин)"""
        self.click(self.locators.LOGIN_BUTTON)
        self.input(self.locators.EMAIL_INPUT_FIELD, login)
        self.input(self.locators.PASSWORD_INPUT_FIELD, password)
        self.click(self.locators.ENTER_TO_PROFILE)
