import pytest


#Fixtures
@pytest.fixture(scope="module")
def prework():
    print("I Setup module1 instance")
    return "pass"

@pytest.fixture(scope="function")
def secondwork():
    print("I Setup module2 instance")
    yield
    print("tear down validation")

@pytest.mark.smoke
def test_initialcheck(prework, secondwork):
    print("This is first test")
    assert prework == "pass"


@pytest.mark.skip
def test_secondcheck(preSetupwork, secondwork):
    print("This is second test")
