from pathlib import Path
from time import sleep

from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .segment_page import SegmentPage
from ui.locators.locators import DashboardPageLocators


IMAGE_PATH = Path.cwd() / 'test_data' / 'airplans.jpg'


class DashboardPage(BasePage):
    locators = DashboardPageLocators()
    URL = 'https://target.my.com/dashboard'

    def go_to_segments(self):
        self.click(self.locators.AUDITORS)
        return SegmentPage(self.driver)

    def create_campaign(self, name: str, url: str = 'airplans.com', path_to_image: str = str(IMAGE_PATH)) -> None:
        try:
            self.click(self.locators.CREATE_CAMPAIGN, 5)
        except TimeoutException:
            self.click(self.locators.CREATE_CAMPAIGN_BUTTON)
        self.click(self.locators.CHOOSE_TYPE_BUTTON)
        self.input(self.locators.INPUT_URL, url)
        sleep(3)
        self.input(self.locators.CAMPAIGN_NAME_INPUT, name)
        sleep(2)
        self.click(self.locators.AD_TYPE_BANNER_BUTTON)
        sleep(2)
        self.input(self.locators.UPLOAD_INPUT, path_to_image)
        self.click(self.locators.IMAGE_CROPPER_SAVE_BUTTON)
        sleep(1)
        self.click(self.locators.FINAL_BUTTON)
        self.find(self.locators.TABLE_ELEMENT)
