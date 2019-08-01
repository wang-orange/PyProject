#coding:utf-8
from mock import mock

# 模拟mock封装
def mock_test(request_data,url,method,response_data):
    mock_func = mock.Mock(return_value=response_data)
    res = mock_func(url,method,request_data)
    return res