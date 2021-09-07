import pytest
import requests
import json
from pytest_f_api.config.testconfig import api_url
from pytest_f_api.common.functions import get_params

@pytest.fixture(scope='session')
def test_get_token():
    url=api_url+'/api/v1/user/login'
    headers={"Content-Type":"application/json"}
    payload={
        "loginName": "18361104557",
        "passwordMd5": "25D55AD283AA400AF464C76D713C07AD"
    }
    r=requests.post(url=url,data=payload,headers=headers)
    json_data=r.json()
    token_value=json_data.get('data')
    return token_value

@pytest.fixture(scope='session')
def header():
    head={'Content-Type':'application/json'}
    return head



if __name__=='__main__':
    test_get_token()