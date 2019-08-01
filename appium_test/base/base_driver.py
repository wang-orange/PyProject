# coding:utf-8
from appium import webdriver
from util.handle_yaml import HandleYaml

class BaseDriver:
    def get_driver(self, i):
        handle_yaml = HandleYaml()
        device = handle_yaml.get_value(i,'deviceName')
        port = handle_yaml.get_value(i, 'port')
        caps = {
            'platformName': 'Android',
            'deviceName':device,
            'app': '../app/mukewang.apk',
            'noRest':True
        }
        driver = webdriver.Remote('http://127.0.0.1:'+str(port)+'/wd/hub', caps)
        return driver

# if __name__ == '__main__':
#     # driver = BaseDriver().get_driver(1)