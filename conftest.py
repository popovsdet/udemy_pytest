import pytest



@pytest.fixture(autouse=True)
def set_up(set_up2):
    print("11111")
    yield
    print("22222")


@pytest.fixture()
def set_up2():
    print("0.1")
    yield
    print("0.2")
