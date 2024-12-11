#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 12/11/2024 5:07 PM
@ Author      : Administrator
@ File        : page_app_login.py
@ Description : App login page.
"""
update_btn = '//android.widget.TextView[@resource-id="android:id/alertTitle"]'
username_el = '//android.webkit.WebView[@text="pages/login/login[3]"]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText'
password_el = '//android.webkit.WebView[@text="pages/login/login[3]"]/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View/android.view.View/android.widget.EditText'
login_btn = '//android.widget.TextView[@text="登录"]'


class PageAppLogin:
    """ App login page. """

    @classmethod
    def app_login(cls, driver, username, password):
        """ App login. """
        driver.sleep(2)
        if driver.find_element(update_btn):
            driver.driver.switch_to.alert.accept()
        driver.type(username_el, username)
        driver.type(password_el, password)
        driver.find_element(login_btn).click()
