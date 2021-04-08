import random
from selenium.webdriver.common.by import By
import time
from ui.pages.BasePage import BasePage
from ui.locators.locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait


class AuthorizedPage(BasePage):
    locatorsBP = BasePageLocators()
    NEWFIO = ["Андрей Сергеевич Сидорчук", "Андрей", "Andrew", "Андрей Сидорчук"]
    NEW_NUMBERS = ['89648653867', '89000000000', '87999999990', '82976677777']

    def logout(self):
        self.click(self.locatorsBP.WRAP_BUTTON)
        time.sleep(1)
        self.click(self.locatorsBP.LOGOUT_BUTTON)

    def correct_contact_information(self):
        self.click(self.locatorsBP.PROFILE_BUTTON)
        time.sleep(1)
        fio = self.find(self.locatorsBP.FIO)
        old_fio = self.click_input_info(fio)
        fio.send_keys(self.NEWFIO[random.randint(0, 3)])
        number = self.find(self.locatorsBP.NUMBER)
        old_number = self.click_input_info(number)
        number.send_keys(self.NEW_NUMBERS[random.randint(0, 3)])
        time.sleep(1)
        save = self.find(self.locatorsBP.SAVE)
        save.click()
        data = {'old_fio': old_fio, 'old_number': old_number, 'new_fio': self.NEWFIO, 'new_number': self.NEW_NUMBERS}
        return data

    def click_input_info(self, sections):
        meaning = self.find(self.locatorsBP.FIO)
        old_meaning = meaning.text
        time.sleep(1)
        meaning.clear()
        return old_meaning

    def parametrize_page(self, categ):
        self.driver.find_element(By.CSS_SELECTOR, f'a[href="/{categ}s"]').click()
        time.sleep(3)

    def search(self, title):
        WebDriverWait(self.driver, 2)
        statistic_instrumental = (By.CSS_SELECTOR, f'a[href="/{title}"]')
        page = self.find(statistic_instrumental)
        return page
