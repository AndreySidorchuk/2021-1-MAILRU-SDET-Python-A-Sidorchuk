import allure
import pytest
import string
import random

from tests.base import BaseCase
from ui.pages.segment_page import SegmentPage
from ui.pages.base_page import NoSuchElementException
from ui.pages.dashboard_page import DashboardPage
from creds.creds import EMAIL, PASSWORD


@pytest.fixture
def generate_random_name_segment_company(length: int = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.mark.UI
class Test(BaseCase):

    @pytest.fixture
    def test_auth_fixture(self):
        self.main_page.login(EMAIL, PASSWORD)
        return DashboardPage(self.driver)

    @allure.feature('UI tests')
    @allure.story('Негативный тест на авторизацию 1')
    @allure.severity(allure.severity_level.BLOCKER)
    def test1_auth_negative(self):
        self.main_page.login('Andrew', '654321')
        assert self.main_page.URL == self.driver.current_url

    @allure.feature('UI tests')
    @allure.story('Негативный тест на авторизацию 2')
    @allure.severity(allure.severity_level.BLOCKER)
    def test2_auth_negative(self):
        self.main_page.login('Andrey', '123456')
        check_auth = self.main_page.find(self.main_page.locators.CHECK_FAIL_AUTH)
        assert check_auth is None

    @allure.feature('UI tests')
    @allure.story('Тест на создание кампании')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_campaign_creation(self, test_auth_fixture, generate_random_name_segment_company):
        page = test_auth_fixture
        page.create_campaign(generate_random_name_segment_company)
        assert page.content_check(page.locators.CAMPAIGN, generate_random_name_segment_company)

    @allure.feature('UI tests')
    @allure.story('Тест на создание сегмента')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_segment(self, test_auth_fixture, generate_random_name_segment_company):
        page = test_auth_fixture.go_to_segments()
        page.create_segment(generate_random_name_segment_company)
        assert page.check_segment_company(page.locators.NEW_SEGMENT, generate_random_name_segment_company)

    @allure.feature('UI tests')
    @allure.story('Тест на удаление сегмента')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_delete_segment(self, test_auth_fixture, generate_random_name_segment_company):
        page = test_auth_fixture.go_to_segments()
        page.create_segment(generate_random_name_segment_company)
        page.delete_segment(generate_random_name_segment_company)
        with pytest.raises(NoSuchElementException):
            page.find_segment_company(page.locators.NEW_SEGMENT_NAME)
