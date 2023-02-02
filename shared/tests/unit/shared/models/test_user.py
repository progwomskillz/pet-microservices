import pytest
from mock import Mock

from src.shared.models import User


@pytest.fixture
def email():
    return "test@email.com"


@pytest.fixture
def sut(email):
    return User(email)


def test_init(sut, email):
    assert sut.email == email
