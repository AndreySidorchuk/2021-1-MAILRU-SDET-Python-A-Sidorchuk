from ui.fixtures import *
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.segment_page import SegmentPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.dashboard_page: DashboardPage = request.getfixturevalue('dashboard_page')
        self.segment_page: SegmentPage = request.getfixturevalue('segment_page')
