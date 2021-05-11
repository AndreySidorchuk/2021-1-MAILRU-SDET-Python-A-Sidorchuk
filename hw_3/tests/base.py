from api.my_target_client import MyTargetClient
from conftest import Settings, config
import pytest

class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.config: Settings = config
        self.target_client: MyTargetClient = request.getfixturevalue('target_client')
