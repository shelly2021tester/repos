import pytest
import requests


def test_login_api():
    url="http://newbee.pansaifei.com/api/v1/user/login"
    headers = {"Content-Type": "application/json"}
    payload = {
        "loginName": "18361104557",
        "passwordMd5": "25D55AD283AA400AF464C76D713C07AD"
    }
    r = requests.post(url=url, data=payload, headers=headers)
    json_data = r.json()
    token_value = json_data.get('data')
    print(token_value)

if __name__=='__main__':
    pytest.main(['-sv','repos/testlogin.py'])
