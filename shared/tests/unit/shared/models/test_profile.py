import pytest

from src.shared.models import Profile


id = "test_id"
user_id = "test_user_id"
first_name = "test_first_name"
last_name = "test_last_name"


@pytest.fixture
def sut():
    return Profile(id, user_id, first_name, last_name)


def test_init(sut):
    assert sut.id == id
    assert sut.user_id == user_id
    assert sut.first_name == first_name
    assert sut.last_name == last_name


def test_on_create(sut):
    new_id = "test_new_id"

    sut.on_create(new_id)

    assert sut.id == new_id


def test_set_user_id(sut):
    new_user_id = "test_new_user_id"

    sut.set_user_id(new_user_id)

    assert sut.user_id == new_user_id
