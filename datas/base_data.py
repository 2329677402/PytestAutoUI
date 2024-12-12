#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@ Date        : 2024/12/12 上午12:23
@ Author      : Poco Ray
@ File        : base_data.py
@ Description : 功能描述
"""
import requests
import json


class ApiData:
    def __init__(self, _base_url):
        self.base_url = _base_url

    @staticmethod
    def get_data(url, params=None, headers=None):
        """
        Fetch data

        :param url: Request URL
        :param params: Request parameters
        :param headers: Request headers
        :return: Response data
        """
        response = requests.get(url, params=params, headers=headers)
        return response.json()

    @staticmethod
    def post_data(url, data=None, headers=None):
        """
        Submit data

        :param url: Request URL
        :param data: Request data
        :param headers: Request headers
        :return: Response data
        """
        response = requests.post(url, data=data, headers=headers)
        return response.json()

    def get_token(self, username, password, registration_id=""):
        url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": username,
            "password": password,
            "registrationId": registration_id
        })
        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json',
        }
        _token = self.post_data(url=url, headers=headers, data=payload).get("token", [])
        return _token

    def get_dept_data(self, _token) -> list[str]:
        """获取部门数据"""
        url = f"{self.base_url}/system/dept/option/tree"
        headers = {
            'Authorization': f'Bearer {_token}',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
        data = self.get_data(url=url, headers=headers).get("data", [])
        return self.extract_labels(data)

    @staticmethod
    def extract_labels(data):
        labels = []
        for item in data:
            labels.append(item.get("label"))
            if "children" in item:
                labels.extend(ApiData.extract_labels(item["children"]))
        return labels

    def get_type_data(self, _token) -> list[str]:
        """特殊作业类型"""
        url = f"{self.base_url}/system/dict/data/type/special_task_ticket_type"
        headers = {
            'Authorization': f'Bearer {_token}',
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
        data = self.get_data(url=url, headers=headers).get("data", [])
        return data


# Example usage
if __name__ == "__main__":
    api_data = ApiData("http://113.194.201.66:8899")
    token = api_data.get_token("admin", "yl123456")

    # Get department data
    if token:
        dept_list = api_data.get_dept_data(token)
        type_list = api_data.get_type_data(token)
        print(type_list)
