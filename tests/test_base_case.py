#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/09/2024 5:24 PM
@ Author      : Administrator
@ File        : test_base_case.py
@ Description : Web-side test base class and App-side test base class.
"""
import pytest
from selenium.webdriver.remote.webelement import WebElement

from utils.api_tool.base_case import BaseCase
from pages.page_app.page_app_login import PageAppLogin
from pages.page_web.page_web_login import PageWebLogin


class BaseCaseWeb(BaseCase):
    """ Web-side test base class """

    @pytest.fixture(autouse=True)
    def setup_web_test(self, web_driver) -> None:
        """
        Set up the Web test environment.

        :param web_driver: Web driver instance.
        """
        self.driver = web_driver
        self.setup_actions()
        yield

    def login(self, url="http://113.194.201.66:8092/login", username="admin", password="admin123"):
        """ Web login implementation. """
        PageWebLogin.web_login(self, url, username, password)


class BaseCaseApp(BaseCase):
    """ App-side test base class """

    @pytest.fixture(autouse=True)
    def setup_app_test(self, app_driver):
        """
        Set up the App test environment.

        :param app_driver: App driver instance.
        """
        self.driver = app_driver
        self.setup_actions()
        yield

    def login(self, username="admin", password="admin123"):
        """ App login implementation. """
        PageAppLogin.app_login(self, username, password)

    # TODO: Implement the following methods in the BaseCase class.
    def get_dept_data(self) -> list[str]:
        """
        Get department data.

        :return: Department data.
        """
        pass