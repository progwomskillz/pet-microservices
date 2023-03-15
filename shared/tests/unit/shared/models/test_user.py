import pytest
from mock import Mock

from src.shared.models import User


id = "test_id"
email = "test@email.com"
password_hash = "test_password_hash"
tokens_pair_mock = Mock()
tokens_pairs_mock = [tokens_pair_mock]
profile_mock = Mock()


@pytest.fixture
def sut():
    return User(id, email, password_hash, tokens_pairs_mock, profile_mock)


def test_init(sut):
    assert sut.id == id
    assert sut.email == email
    assert sut.password_hash == password_hash
    assert sut.tokens_pairs == tokens_pairs_mock
    assert sut.profile == profile_mock


def test_on_create(sut):
    new_id = "test_new_id"

    sut.on_create(new_id)

    assert sut.id == new_id
    sut.profile.set_user_id.assert_called_once_with(new_id)
