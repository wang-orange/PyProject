#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMail:
    '''发送邮件
    '''
    global send_user
    global email_host
    global password
    send_user = "18600407736@163.com"
    password = "orange@0419"
    email_host = "smtp.163.com"

    def send_email(self,user_list,subject,content):
        ''' 发送邮件,不带附件
        '''
        user = "wangyunju0419" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = subject
        message['From'] = user
        message['To'] = ';'.join(user_list)
        # message['Cc'] = send_user  # 抄送
        print(message)
        # 连接并登录邮箱服务器
        server = smtplib.SMTP(email_host)
        # server.connect(email_host)
        server.login(send_user,password)
        # 发送邮件
        server.sendmail(send_user,user_list,message.as_string())
        # server.close()
        server.quit()

    def send_email_attachment(self,to_list,subject,content,filename=None):
        ''' 发送邮件,带附件
        '''
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = send_user
        msg['To'] = ';'.join(to_list)
        # 邮件正文
        content = MIMEText(content,_subtype='plain',_charset='utf-8')
        msg.attach(content)
        # 构造附件
        if filename == None:
            filename = '../report/TestReport.html'
        attachment= MIMEText(open(filename,'rb').read(), 'base64', 'utf-8')
        attachment["Content-Type"] = 'application/octet-stream'
        attachment["Content-Disposition"] = 'attachment; filename="result.xls"' # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(attachment)
        server = smtplib.SMTP(email_host)
        server.login(send_user,password)
        server.sendmail(send_user,to_list,msg.as_string())
        server.close()

    def send_main(self, pass_count, fail_count):
        '''将测试结果邮件发送
        '''
        user_list = [ "376904489@qq.com", "wangyunju0419@163.com"]
        sub = "接口自动化测试"
        case_count = pass_count + fail_count
        pass_percent = "%.2f%%" %(float(pass_count)/float(case_count)*100)
        fail_percent = "%.2f%%" %(float(fail_count)/float(case_count)*100)
        print(pass_percent,fail_percent)
        content = "此次一共执行用例%d个，通过%d个，失败%d个，通过率%s，失败率%s" \
                  %(case_count,pass_count,fail_count,pass_percent,fail_percent)
        print(content)
        report_file = '../report/TestReport.html'
        result = '../config/interface.xls'
        # self.send_email(user_list,sub,content)
        # self.send_email_attachment(user_list,sub,content,report_file)
        self.send_email_attachment(user_list,sub,content,result)


if __name__ == '__main__':
    send = SendMail()
    send.send_main(2,7)