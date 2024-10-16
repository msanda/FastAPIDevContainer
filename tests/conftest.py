import pytest

from api.main import app as api_app

@pytest.fixture()
def app():
    app = api_app
    return app