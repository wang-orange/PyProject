#coding:utf-8
import json

class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
        判断字符串str_one是否在另一个字符串str_two中
        '''
        str_two = str_two.content
        str_two = str_two.decode('unicode-escape')
        print(str_one)
        print(str_two)
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag
