#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/11/2024 5:30 PM
@ Author      : Administrator
@ File        : test_app_special.py
@ Description : 功能描述
"""
import allure
import pytest
from tests.test_base_case import BaseCaseApp
from utils.log_tool.log_control import ERROR, INFO

width, height = 900, 1600  # self.get_window_size()
# 特殊作业
special_task = '//*[@text="特殊作业"]'
# 作业票预约
ticket_reservation = '(//*[@text="作业票预约"])[2]'
# 作业票处理
ticket_processing = '//*[@text="作业票处理"]'
# 添加按钮
add_btn = '//*[@text="+  "]'
# 作业申请单位选择框
task_unit_option_pos = (width * 0.5, height * 0.15)
# 作业申请单位输入框
input_task_unit = '//*[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText'
# 部门选项选择
select_option = '(//*[@text="研发部"])[2]'
# 确认按钮
confirm_btn = '//*[@text="确定"]'
# 作业地点选择框
task_location_list = '//android.webkit.WebView[@text="pages/working/appointment/addForm[4]"]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
# 作业地点输入框
input_task_location = '//*[@text="pages/working/appointment/addForm[3]"]/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[1]/android.view.View/android.view.View'
# 地点选项选择
select_location_option = '//*[@text="临时停车区2"]'
# 作业详细地点输入框
task_detail_location = '//*[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'


@allure.feature("特殊作业")
@pytest.mark.app
@pytest.mark.special
class TestAppSpecial(BaseCaseApp):
    """ Test App special function """

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("处理特殊作业")
    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    def test_app_special(self):
        """ Test App special function """
        try:
            INFO.logger.info("Start testing the App special function...")
            self.login()
            self.sleep(2)
            self.click(special_task)
            self.click(ticket_reservation)
            self.click(add_btn)
            self.tap(pos=[task_unit_option_pos])
            self.type(input_task_unit, '研发部')
            self.click(select_option)
            self.click(confirm_btn)
            self.click(task_location_list)
            self.type(input_task_location, '临时停车区2')
            self.click(select_location_option)
            self.click(confirm_btn)
            self.type(task_detail_location, '测试数据')
            print(self.contexts)


        except Exception as e:
            ERROR.logger.error(f"Failed to test the App special function, error message: {str(e)}")
            self.take_screenshot("special_failed")
            raise
