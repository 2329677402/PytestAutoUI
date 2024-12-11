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

# TODO: Implement the following methods in the BaseCase class.
class ApiHelper:
    """ API Helper class """

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


class ApiClient:
    """ API 客户端类 """

    def __init__(self, _base_url):
        self.base_url = _base_url

    def login(self, username, password, registration_id=""):
        url = f"{self.base_url}/login"
        payload = json.dumps({
            "username": username,
            "password": password,
            "registrationId": registration_id
        })
        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)
        return response.json()

    def get_dept_data(self, _token) -> list[str]:
        """获取部门数据"""
        url = f"{self.base_url}/system/dept/option/tree"
        headers = {
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Authorization': f'Bearer {_token}'
        }
        response = requests.get(url, headers=headers)
        data = response.json().get("data", [])
        return self.extract_labels(data)

    @staticmethod
    def extract_labels(data):
        labels = []
        for item in data:
            labels.append(item.get("label"))
            if "children" in item:
                labels.extend(ApiClient.extract_labels(item["children"]))
        return labels


# Example usage
if __name__ == "__main__":
    base_url = "http://113.194.201.66:8899"
    api_client = ApiClient(base_url)

    # Login
    login_response = api_client.login("123456789", "123456")
    print(login_response)

    # Get special ticket ID
    token = login_response.get("token")
    # Get department data
    if token:
        dept_data = api_client.get_dept_data(token)
        print(dept_data)
