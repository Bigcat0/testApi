from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('获取登录信息')
class Test_getUserInfo():
    @allure.story('获取用户信息')
    def test_getUserInfo(this):
        data = {
           "token":CommonData.token

        }
        resp = http.post('/sys/getUserInfo',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
