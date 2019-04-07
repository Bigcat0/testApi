# import pytest
# from common.commonData import CommonData
# from conftest import http
# #
# #
# def test_login():
#     path = '/sys/getUserInfo'
#     data = {'token':CommonData.token}
#     resp = http.post(path,data)
#     print(resp)









# @pytest.fixture()
# def my_fixtures():
#     print("spec start")
#     yield
#     print("spec end")
# class Test_class:
#
#     def test_myfirst(this):
#         print("我的第一个pytest 用例")
#         assert 1!=2
#
#     @pytest.mark.debug
#     # @pytest.mark.usefixtures("my_fixtures")
#     def test_secend(this):
#         print("我的第二个pytest 用例")
#         assert 2==2
#
#     @pytest.mark.debug
#     # @pytest.mark.usefixtures("my_fixtures")
#     def test_three(this):
#         print("我的第三个pytest用例")
#         assert "a" in "ab"
#     # @pytest.mark.usefixtures("my_fixtures")
#     def test_fore(this):
#         print("我的第四个pytest用例")
#         b=[1,2,3,4]
#         assert 2 in b
#
#     def test_five(this):
#         print("我的第五个pytest用例")
#         assert True



# if __name__ == '__main__':
#     pytest.main('-s')