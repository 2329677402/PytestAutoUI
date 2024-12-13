#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/11/2024 7:31 PM
@ Author      : Poco Ray
@ File        : test_web_login.py
@ Description : Web login test case.
"""

import pytest
from tests.test_base_case import BaseCaseWeb
from utils.log_tool.log_control import INFO, ERROR


class TestWebLogin(BaseCaseWeb):
    """ Web login test case. """

    @pytest.mark.web
    @pytest.mark.login
    def test_web_login(self):
        """ Success login test case. """
        try:
            INFO.logger.info("Start testing the Web login function...")
            self.login()
            self.assert_title("仰立新材料管理系统")
            self.take_screenshot("after_login")
            self.click("li:contains('特殊作业全过程')")
            self.sleep(1)

        except Exception as e:
            ERROR.logger.error(f"Failed to test the Web login function, error message: {str(e)}")
            self.take_screenshot("login_failed")
            raise
