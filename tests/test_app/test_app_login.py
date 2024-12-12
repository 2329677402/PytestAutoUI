#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/11/2024 7:49 PM
@ Author      : Poco Ray
@ File        : test_app_login.py
@ Description : App login test case.
"""
import allure
import pytest
from tests.test_base_case import BaseCaseApp
from utils.log_tool.log_control import INFO, ERROR
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
@allure.epic("项目名称: 仰立App自动化测试")
@allure.feature("登录模块")
@pytest.mark.app
@pytest.mark.login
class TestAppLogin(BaseCaseApp):
    """ Test App login """
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("登录成功(账号存在+密码正确)")
    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_app_login_success(self):
        """ Success login test case. """
        try:
            INFO.logger.info("Start testing the App login function...")
            self.login()
        except Exception as e:
            ERROR.logger.error(f"Failed to test the App login function, error message: {str(e)}")
            self.take_screenshot("login_failed")
            raise

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("登录失败(账号存在+密码错误)")
    def test_app_login_fail(self):
        """ Failed login test case. """
        try:
            INFO.logger.info("Start testing the App login function...")
            self.login(username="admin", password="admin1234")
        except Exception as e:
            ERROR.logger.error(f"Failed to test the App login function, error message: {str(e)}")
            self.take_screenshot("login_failed")
            raise
