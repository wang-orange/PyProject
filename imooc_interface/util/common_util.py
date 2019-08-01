#coding:utf-8

class CommonUtil:
    def is_contains(self, str_one, str_two):
        ''' 判断str_one是否包含在str_two内
        '''
        # flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag