import pytest
from mock import Mock

from src.shared.models import TokensPair


id = "test_id"
access = "test_access"
refresh = "test_refresh"


@pytest.fixture
def sut():
    return TokensPair(id, access, refresh)


def test_init(sut):
    assert sut.id == id
    assert sut.access == access
    assert sut.refresh == refresh


def test_on_create(sut):
    new_id = "test_new_id"

    sut.on_create(new_id)

    assert sut.id == new_id
