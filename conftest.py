#Fixtures y estructuras que podrían volverse repetitivas.

import pytest
from utils.helpers import chrome_driver

@pytest.fixture
def driver():
    driver = chrome_driver()
    yield driver
    driver.quit()
