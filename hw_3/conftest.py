import random
import string
from dataclasses import dataclass
from api.my_target_client import MyTargetClient
import pytest

@pytest.fixture
def generate_random_string(length: int = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@dataclass
class Settings:
    USERNAME: str = None
    PASSWORD: str = None

@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings(
        USERNAME='andrew.sidorchuk@mail.ru',
        PASSWORD='andrew24061996'
        )

    return settings


@pytest.fixture(scope='function')
def target_client(config):
    return MyTargetClient(config.USERNAME, config.PASSWORD)
