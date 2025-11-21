import pytest


@pytest.fixture(scope="session")
def preSetupwork():
    print("I Setup browser instance")