import requests
import json
from common.commonData import CommonData

class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers = {'Content-Type': 'application/json;charset=UTF-8'}

    def post(self,path,data):

        proxies = CommonData.proxies        #获取全局变量proxies
        host = CommonData.host
        data_json = json.dumps(data)            #jiang将data转成json   格式
        if CommonData.token is not None:     #判断token是否为空，不为空赋值，为空不加
            self.headers["token"]= CommonData.token
        resp_login = self.http.post(url=host+path,   #发起post请求
                     proxies=proxies,
                     data=data_json,
                     headers=self.headers)
        assert resp_login.status_code == 200   #校验返回码是否为200
        resp_json = resp_login.text             #
        resp_dict = json.loads(resp_json)
        return resp_dict

# proxies={'http':'http://localhost:9999'}
# # headers={}
# # headers['Content-Type']='application/json;charset=UTF-8'
# headers={'Content-Type':'application/json;charset=UTF-8'}
# http = requests.session()
# resp=http.post(url="http://192.168.1.203:8083/sys/login",
#                    proxies=proxies,
#                    data='{"userName": "15735518063","password": "123456"}',
#                    headers=headers)
#
# resp_dict = json.loads(resp.text)  #将json转python dict
# token = resp_dict['object']['token']#  获取token
# headers['token']=token #将token加到headers dict里
# data ={'token':token}  #创建了一个data的dict，添加了token数据
# data_json = json.dumps(data)   #jaing将python对象转成json
#
# resp=http.post(url="http://192.168.1.203:8083/sys/getUserInfo",
#                    proxies=proxies,
#                    # data='{"token":"'+token+'"}',
#                    data=data_json,
#                    headers=headers)


# print(resp.text)
# print(resp.headers)
# print(resp.encoding)#编码
# print(resp.status_code)#zhuan状态码
# print(resp.cookies)
# print(resp.elapsed)
# print(resp.raw)
# print(resp.request)