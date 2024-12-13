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
            width, height = self.get_window_size().values()

            # 特殊作业
            special_task = '//*[@text="特殊作业"]'
            self.click(special_task, 'xpath')

            # 作业票预约
            ticket_reservation = '(//*[@text="作业票预约"])[2]'
            self.click(ticket_reservation)

            # 添加按钮
            add_btn = '//*[@text="+  "]'
            self.click(add_btn)

            # 作业申请单位选择框
            task_unit_option_pos = (width * 0.5, height * 0.15)
            self.tap(pos=[task_unit_option_pos])

            # 作业申请单位输入框
            input_task_unit = '//*[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[5]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText'
            self.type(input_task_unit, '研发部')

            # 部门选项选择
            select_option = '(//*[@text="研发部"])[2]'
            self.click(select_option)

            # 确认按钮
            confirm_btn = '//*[@text="确定"]'
            self.click(confirm_btn)

            # 作业地点选择框
            task_location_list = (width * 0.5, height * 0.28)
            self.tap([task_location_list])
            self.sleep(1)

            # 作业地点输入框
            self.tap([(width * 0.5, height * 0.43)])
            self.sleep(1)
            print(self.contexts)
            input_task_location = '//*[@text="pages/working/appointment/addForm[3]"]/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
            el = self.find_element(input_task_location)
            print(el)
            el.send_keys('临时停车区2')

            # 地点选项选择
            select_location_option = '(//*[@text="临时停车区2"])[2]'
            self.click(select_location_option)

            self.click(confirm_btn)

            # 作业详细地点输入框
            task_detail_location = '//*[@text="pages/working/appointment/addForm[6]"]/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
            self.type(task_detail_location, '测试数据')
            print(self.contexts)

            # 提交按钮
            submit_btn = '//*[@text="提交"]'
            self.click(submit_btn)

        except Exception as e:
            ERROR.logger.error(f"Failed to test the App special function, error message: {str(e)}")
            self.take_screenshot("special_failed")
            raise
