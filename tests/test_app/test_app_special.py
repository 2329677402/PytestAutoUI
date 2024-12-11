#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/11/2024 5:30 PM
@ Author      : Administrator
@ File        : test_app_special.py
@ Description : 功能描述
"""
import pytest
from tests.test_base_case import BaseCaseApp
from utils.log_tool.log_control import ERROR, INFO

# 特殊作业
special_task = '//android.widget.TextView[@text="特殊作业"]'
# 作业票预约
ticket_reservation = '(//android.widget.TextView[@text="作业票预约"])[2]'
# 作业票处理
ticket_processing = '//android.widget.TextView[@text="作业票处理"]'
# 添加按钮
add_btn = '//android.widget.TextView[@text="+  "]'
# 作业申请单位选择框
task_unit_list = '//android.webkit.WebView[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
# 作业申请单位输入框
input_task_unit = '//android.webkit.WebView[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText'
# 作业地点选择框
task_location_list = '//android.webkit.WebView[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
# 作业地点输入框
input_task_location = '//android.webkit.WebView[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
# 作业详细地点输入框
task_detail_location = '//android.webkit.WebView[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'


class TestAppSpecial(BaseCaseApp):
    """ Test App special function """

    def test_app_special(self):
        """ Test App special function """
        try:
            INFO.logger.info("Start testing the App special function...")
            self.login()
            self.click(special_task)
            self.click(ticket_reservation)
            self.take_screenshot("作业预约页面")
            self.click(add_btn)
            self.take_screenshot("添加作业票详情")
            self.click(task_unit_list)

        except Exception as e:
            ERROR.logger.error(f"Failed to test the App special function, error message: {str(e)}")
            self.take_screenshot("special_failed")
            raise
