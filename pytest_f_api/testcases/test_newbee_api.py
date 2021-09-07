import pytest
from pytest_f_api.common.functions import get_params,send_request,result_status

caseid=['Newb_001']
#casemodule=['首页']
@pytest.mark.parametrize('caseid',caseid)
def test_userinfo_api(caseid):
    data=get_params(1,caseid)
    try:
        expectvalues=data[4]
        resp=send_request(data)
        assert expectvalues in resp.text
        print("测试用例成功")
        result_status(1,caseid,"Passed")
    except AssertionError:
        print("测试用例失败")
        result_status(1, caseid, "Failed")


if __name__=='__main__':
    pytest.main()





