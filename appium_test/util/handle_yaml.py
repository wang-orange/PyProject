# coding:utf-8
import yaml  # python 3.x -- pip install pyyaml

class HandleYaml:
    '''
    操作yaml文件
    '''
    def __init__(self, file_path = None):
        if file_path == None:
            self.path = '../config/devices.yaml'
        else:
            self.path =file_path

    def read_yaml(self, i):
        '''
        读取yaml文件，得到第i个设备的信息
        '''
        try:
            with open(self.path) as fp:
                fi = yaml.load(fp)
            return fi.get('user_info_' + str(i))
        except:
            return None

    def get_value(self, i, key):
        '''
        通过关键字，获取设备的名称和端口
        '''
        try:
            return self.read_yaml(i)[key]
        except:
            return None

    def write_yaml(self, i, bp, device, port):
        '''
        向yaml文件写入设备信息
        '''
        data = self.collect_data(i, bp, device, port)
        with open(self.path, 'a') as fp:
            yaml.dump(data, fp)

    def collect_data(self, i, bp, device, port):
        data = {
            'user_info_'+str(i): {'bp': bp, 'deviceName': str(device), 'port': port}
        }
        return data

    def clear_yaml(self):
        '''
        清空yaml文件
        '''
        with open(self.path, 'w') as fp:
            fp.truncate()


if __name__ == '__main__':
    h = HandleYaml()
    print(h.get_value(0, 'port'))
    # h.write_yaml(4, 4333, 'test_name', 7777)
    # h.clear_yaml()