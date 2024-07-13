import pytest
from fastapi.testclient import TestClient

from ngpd_manager.app import app


@pytest.fixture
def client():
    return TestClient(app)
