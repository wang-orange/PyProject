# coding:utf-8
from configparser import ConfigParser  # pip install configparser

class ReadIni:
    '''
    读取ini文件，从中得到关键字的值
    '''
    def __init__(self, file_path=None):
        if file_path == None:
            self.path = '../config/LoginPage.ini'
        else:
            self.path = file_path

    def read_ini(self):
        cfg = ConfigParser()
        cfg.read(self.path)
        return cfg

    def get_value(self, key, section=None):
        if section == None:
            section = 'login'
        try:
            value = self.read_ini().get(section, key)
        except:
            return None
        return value

if __name__ == '__main__':
    re = ReadIni()
    print(re.read_ini())
    print(re.get_value('username'))
    print(re.get_value('ff', 'a'))
    print(re.get_value('aa'))
    print(re.get_value('test1', 'test'))

