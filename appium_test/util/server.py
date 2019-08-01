# coding:utf-8
from excute_cmd import ExcuteCmd
from port import Port
import threading

class Server:
    '''
    appium server
    '''
    def __init__(self):
        self.cmd = ExcuteCmd()
        # self.devices = self.get_devices()
        self.devices = ['device1', 'device2']

    def start_server(self, i):
        '''
        启动appium服务
        '''
        command = self.get_command(i)
        if command != None:
            self.cmd.excute_cmd(command)

    def get_command(self, i):
        '''
        根据devices个数，得到命令列表
        '''
        # appium -p 1234 -bp 3455 -U device  --no-reset --session-override
        port = self.get_port(4700)
        bp_port = self.get_port(4900)
        command_list = []
        if self.devices != None:
            for i in range(len(self.devices)):
                command = 'appium -p '+str(port[i])+' -bp '+str(bp_port[i])+' -U '+self.devices[i]+\
                    ' --no-reset --session-override'
                # command_list.append(command)
            return command
        else:
            return None

    def get_devices(self):
        '''
        获取设备
        '''
        # ['List of devices attached', '8c76cc8f\tdevice', 'P1QRM974FV\tdevice']
        device_list = []
        result = self.cmd.excute_cmd_result('adb devices')
        if len(result)>1:
            for i in result:
                if 'List' in i:
                    continue
                elif 'device' in i:
                    device = i.split('\t')[0]
                    device_list.append(device)
            return device_list
        else:
            return None

    def get_port(self, start_port):
        '''
        通过devices得到可用的port列表
        '''
        port = Port()
        port_list = []
        if self.devices != None:
            while(len(port_list) != len(self.devices)):
                flag = port.port_is_used(start_port)
                if flag == True:
                    pass
                else:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            return None


if __name__ == '__main__':
    server = Server()
    # print(server.get_devices())
    # print(server.get_port(1211))
    if server.devices != None:
        for i in range(len(server.devices)):
            appium_start = threading.Thread(target=server.start_server, args=(i,))
            appium_start.start()



