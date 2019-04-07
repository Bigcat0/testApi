from common.commonData import CommonData
from conftest import http
import pytest
import allure

@allure.feature('修改密码模块')
class Test_ChangePwd(object):
    @allure.story('修改密码成功')
    @pytest.mark.usefixtures("recoveryPwd")
    def test_changePwd_success(self):
        newPwd='123456'
        data = {
            'userId':135,
            'userName': CommonData.mobile,
            'oldPwd':CommonData.password,
            'password': newPwd
        }
        resp = http.post('/sys/changePwd',data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'


@pytest.fixture()
def  recoveryPwd():
    newPwd='123456'
    yield
    data = {
        'userId': 135,
        'userName': CommonData.mobile,
        'oldPwd': CommonData.password,
        'password': CommonData.password
    }
    resp = http.post('/sys/changePwd', data)

#旧密码不正确
#     def test_changePwd_fail(this):
#         data = {
#             'userName': CommonData.mobile,
#             'oldPwd':1515313,
#             'password':'123456'
#         }
#         resp = http.post('/sys/changePwd',data)
#         assert resp['code'] == 411
#         assert resp['msg'] == '旧密码错误'
#
#
# #旧密码为空
#     def test_changePwd_fail_two(this):
#         data = {
#             'userName': CommonData.mobile,
#             'oldPwd':'',
#             'password':'123456'
#         }
#         resp = http.post('/sys/changePwd',data)
#         assert resp['code'] == 411
#         assert resp['msg'] == '旧密码错误'

#将密码该为空
    # def test_changePwd_fail_three(this):
    #     data = {
    #         'userName': CommonData.mobile,
    #         'password': CommonData.password,
    #         'oldPwd': CommonData.password,
    #         'password':''
    #     }
    #     resp = http.post('/sys/changePwd',data)
    #     assert resp['code'] == 411
    #     assert resp['msg'] == '密码不能为空'          #可以整