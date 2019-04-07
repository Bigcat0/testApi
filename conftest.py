import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonData
#scope="class"/session/module/function
#autouse=True/False
http = HttpUtil()
@pytest.fixture(scope="session",autouse=True)
def session_fixture():
    # proxies = {'http': 'http://localhost:9999'}
    # headers = {'Content-Type': 'application/json;charset=UTF-8'}
    path = "/sys/login"
    data = {
        'userName': CommonData.mobile,
        'password': CommonData.password
    }
    resp_login = http.post(path,data)
    CommonData.token=resp_login['object']['token']
    print("登录成功")







    # resp_login = http.post(url="http://192.168.1.203:8083/sys/login",
    #                  proxies=proxies,
    #                  data='{"userName": "15735518063","password": "123456"}',
    #                  headers=headers)
    # resp_dict = json.loads(resp_login.text)  # 将json转python dict
    # token = resp_dict['object']['token']  # 获取token
    #
    # assert resp_login.status_code==200
    # print("登录成功。。。")
    # yield
    # headers['token'] = token
    # resp = http.post(url="http://192.168.1.203:8083/sys/logout",
    #                  proxies=proxies,
    #                  # data='{"token":"'+token+'"}',
    #                  data=None,
    #                  headers=headers)
    # assert resp.status_code==200
    # print("退出成功")