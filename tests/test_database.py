import pytest

from settings import OPERATIONS
from src.models.database import Data


@pytest.fixture
def data():
    return Data(OPERATIONS)


def test_get_data(data):
    assert len(data.get_data()) > 0


def test_get_operations(data):
    operations = data.get_operations(data.get_data())
    assert len(operations) > 0


def test_get_five_operations(data):
    operations = data.get_operations(data.get_data())
    five_operations = data.get_five_operations(operations)
    assert len(five_operations) <= 5


def test_get_result(data):
    assert data.get_result(data.get_data()) == True
