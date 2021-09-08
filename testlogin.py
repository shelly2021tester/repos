import pytest
import requests

class TestCases:
    def test_login_api(self):
        url="http://newbee.pansaifei.com/api/v1/user/login"
        headers = {"Content-Type": "application/json"}
        payload = {
            "loginName": "13915501234",
            "passwordMd5": "E10ADC3949BA59ABBE56E057F20F883E"
        }
        r = requests.post(url=url, data=payload, headers=headers)
        json_data = r.json()
        token_value = json_data.get('data')
        print(f"\n打印出respons的值为：{json_data},\ntoken值为：{token_value}")

if __name__=='__main__':
    pytest.main(['-sv','testlogin.py::TestCases'])
