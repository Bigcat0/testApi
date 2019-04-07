from common.commonData import CommonData
from conftest import http
import allure
@allure.feature('登录模块')
class Test_Login():
    @allure.story('登录成功')
    def test_login_success(this):
        data = {
            'userName': CommonData.mobile,
            'password': CommonData.password
        }
        resp = http.post('/sys/login',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        assert resp['object']['userId'] == 135
#密码错误
    @allure.story('密码错误')
    def test_login_fail(this):
        data = {
            'userName': CommonData.mobile,
            'password': '123456789'
        }
        resp = http.post('/sys/login',data)
        assert resp['code'] == 410
        assert resp['msg'] == '用户名或密码错误'
#yong用户名超过15位
    @allure.story('用户名超过15位')
    def test_login_fail_two(this):
        data = {
            'userName': '1513131hhhbbhhbh',
            'password':  CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

#用户名不存在
    @allure.story('用户名不存在')
    def test_login_fail_three(this):
        data = {
            'userName':'13656963656',
            'password': CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'
#无参数
    @allure.story('无参数')
    def test_login_fail_fore(this):
        data = {}
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'
#用户名为空
    @allure.story('用户名为空')
    def test_login_fail_five(this):
        data = {
            'userName':'',
            'password': CommonData.password
        }
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'                           #有误，抓包是存在的
        # assert resp['code'] == 3010
        # assert resp['msg'] == '此账户禁止登录'