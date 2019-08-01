# coding:utf-8
import os

class ExcuteCmd:
    '''
    执行dos命令
    '''
    def excute_cmd_result(self, command):
        '''
        获取执行命令的结果
        '''
        list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            list.append(i.strip())
        return list

    def excute_cmd(self, command):
        os.system(command)

if __name__ == '__main__':
    cmd = ExcuteCmd()
    print(cmd.excute_cmd_result('adb devices'))