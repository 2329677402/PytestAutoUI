#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/12/1 下午8:06
@ Author      : Poco Ray
@ File        : test_app_login.py
@ Description : App login test.
"""
import pytest
from tests.test_base_case import BaseCaseApp
from utils.log_tool.log_control import INFO, ERROR
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestAppLogin(BaseCaseApp):
    """ Test App login """

    @pytest.mark.app
    @pytest.mark.login
    def test_app_login(self):
        """ Test App login """
        try:
            INFO.logger.info("Start testing the App login function...")
            self.login()
        except Exception as e:
            ERROR.logger.error(f"Failed to test the App login function, error message: {str(e)}")
            self.take_screenshot("login_failed")
            raise
