import pytest


def hello_world():
    return "hello world!"


@pytest.mark.hello_world
def test_hello_world():
    assert hello_world() == "hello world!"
