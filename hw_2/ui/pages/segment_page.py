from time import sleep
from .base_page import BasePage
from ui.locators.locators import SegmentPageLocators


class SegmentPage(BasePage):
    locators = SegmentPageLocators()

    def create_segment(self, name: str):
        try:
            self.find(self.locators.CREATE_SEGMENT).click()
        except:
            self.click(self.locators.CREATE_SEGMENT_BUTTON)
        self.click(self.locators.SEGMENT_TYPE_GAMES)
        self.click(self.locators.SEGMENT_CHECKBOX)
        self.click(self.locators.SEGMENT_ADD_BUTTON)
        self.find(self.locators.SEGMENT_NAME_INPUT_FIELD).clear()
        self.input(self.locators.SEGMENT_NAME_INPUT_FIELD, name)
        self.click(self.locators.FINAL_BUTTON)
        self.find(self.locators.TABLE_HEADER)

    def delete_segment(self, name: str):
        elem = self.find(self.locators.created_segment_name_node(name))
        elem = elem.find_element(*self.locators.DELETE_SEGMENT_BUTTON)
        elem.click()
        self.click(self.locators.DELETE_SEGMENT)
