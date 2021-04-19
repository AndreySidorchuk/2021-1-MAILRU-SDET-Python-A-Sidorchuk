import random
import string
from tests.base import BaseCase
import pytest

@pytest.fixture
def generate_random_string(length: int = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class TestTargetApi(BaseCase):

    @pytest.mark.API
    def test_create_segment(self, generate_random_string):
        """Тест на создание сегмента"""
        name = generate_random_string
        assert self.target_client.create_segment(name).status_code == 200
        assert self.target_client.check_segment(name)

    @pytest.mark.API
    def test_delete_segment(self, generate_random_string):
        """Тест на удаление сегмента"""
        name = generate_random_string
        assert self.target_client.create_segment(name).status_code == 200
        assert self.target_client.delete_segment(name).status_code == 204
        with pytest.raises(AssertionError):
            assert self.target_client.check_segment(name)

    @pytest.mark.API
    def test_create_campaign(self, generate_random_string):
        """Тест на создание кампании"""
        name = generate_random_string
        assert self.target_client.create_campaign(name).status_code == 200
        assert self.target_client.check_campaign(name)
        assert self.target_client.delete_campaign(name).status_code == 204

