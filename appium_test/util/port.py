# coding:utf-8
from excute_cmd import ExcuteCmd

class Port:
    '''
    判断port是否被占用
    '''
    def port_is_used(self, port):
        cmd = ExcuteCmd()
        list = cmd.excute_cmd_result('netstat -ano | findstr '+str(port))
        if len(list) > 0:
            return True
        else:
            return False

if __name__ == '__main__':
    port = Port()
    print(port.port_is_used(1234))
