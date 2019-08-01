# coding:utf-8
from util.read_ini import ReadIni
from appium import webdriver  # pip install appium-python-client

class LocateElement:
    '''
    从配置文件ini中读取元素并返回找到的元素
    '''
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, key):
        read_ini = ReadIni()
        value = read_ini.get_value(key)
        if value != None:
            value_list = value.split('>')
            by = value_list[0]
            by_value = value_list[1]
            if by == 'id':
                return self.driver.find_element_by_id(by_value)
            elif by == 'class':
                return self.driver.find_element_by_class_name(by_value)
            else:
                return self.driver.find_element_by_xpath(by_value)
        else:
            return None

# if __name__ == '__main__':
#     locate = LocateElement()
#     print(locate.find_element('username'))