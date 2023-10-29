import unittest

import pytest
from selenium import webdriver

from Config.properties import TestProperties


@pytest.mark.usefixtures("web_driver")
class TestBase(unittest.TestCase):

    @pytest.fixture(scope="class")
    def web_driver(self, request):
        driver = webdriver.Chrome()
        driver.get(TestProperties.url)
        request.cls.driver = driver
        yield
        driver.close()
