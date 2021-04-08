import pytest
from tests.base import BaseCase
import time
from creds.creds import EMAIL, PASSWORD


class Test(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.authorization_page.authorize(EMAIL, PASSWORD)
        succses = self.authorization_page.find(self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert succses is not None, 'Авторизация не выполнена'

    @pytest.mark.UI
    def test_logout(self, authorized_page):
        self.authorized_page = authorized_page
        self.authorized_page.logout()
        succses = self.authorization_page.find(self.authorization_page.locators.CHECK_AUTH_SUCCESS)
        assert succses is None, 'Logout не выполнен'

    @pytest.mark.UI
    def test_correct_contact_information(self, authorized_page):
        self.authorized_page = authorized_page
        data = self.authorized_page.correct_contact_information()
        assert data['new_fio'] != data['old_fio'] and data['new_number'] != data['old_number']

    @pytest.mark.UI
    @pytest.mark.parametrize('categ, title', [['statistic', 'statistics/summary'], ['tool', 'tools/feeds']])
    def test_parametrize(self, authorized_page, categ, title):
        self.authorized_page = authorized_page
        time.sleep(2)
        self.authorized_page.parametrize_page(categ)
        assert self.authorized_page.search(title)
