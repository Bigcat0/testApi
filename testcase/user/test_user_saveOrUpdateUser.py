#新建用户
from common.commonData import CommonData
from conftest import http
import random
import allure
@allure.feature('新建用户')
class Test_SaveOrUpdateUser():
    nickname = str(random.randint(10000000, 100000000))
    mobile = '157' + nickname

    @allure.story('新建用户成功')
    def test_saveOrUpdateUser_success(self):

        data = {
            "nickName":self.nickname,
            "userName": self.mobile,
            "telNo": "",
            "email": "",
            "address": "",
            "roleIds": "1",
            "regionId": 1,
            "regionLevel": 1
        }
        resp = http.post('/user/saveOrUpdateUser', data)

    @allure.story('登录成功')
    def test_login(self):
        path='/sys/login'
        data = {
            'userName':self.mobile ,
            'password': '123456'
        }
        resp = http.post(path, data)
        CommonData.token=resp['object']['token']
        id=resp['object']['userId']
        print(id)
        return id

    @allure.story('获取列表成功')
    def test_loadUserList(self):
        path='/user/loadUserList'
        data={
            "pageCurrent": 1,
            "pageSize": 1,
            "nickName": "",
            "userName": "",
            "regionId": 1
            }
        resp = http.post(path,data)
        assert resp['object']['list'][0]['id']==self.test_login()
        return resp['object']['list'][0]['id']

    @allure.story('获取信息成功')
    def test_loadUserInfo(self):
        path='/user/loadUserInfo'
        data={
            "id":self.test_loadUserList()
        }
        resp = http.post(path,data)
        assert resp['code']==200
        assert resp['msg'] == '操作成功'

