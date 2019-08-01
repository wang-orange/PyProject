#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
    global user
    global password
    global smtp_host
    user = "wangyunju0419@163.com"
    password = "orange@0419"
    smtp_host = "smtp.163.com"

    def send_email(self,user_list,subject,content):
        '''不带附件
        '''
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = subject
        message['From'] = user
        message['To'] = ';'.join(user_list)
        server = smtplib.SMTP(smtp_host)
        server.login(user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_email_attachment(self,user_list,subject,content,attachment):
        '''带附件
        '''
        # 构造附件
        attach = MIMEText(open(attachment,'rb').read(),_charset='utf-8')
        attach['Content-Type'] = "application/octet-stream"
        attach['Content-Disposition'] = 'attachment; filename=result.xls'
        # 邮件正文
        content = MIMEText(content,_subtype='plain',_charset='utf-8')
        message = MIMEMultipart(_subtype='mixed')
        message.attach(content)
        message.attach(attach)
        message['Subject'] = subject
        message['From'] = user
        message['To'] = ';'.join(user_list)
        # 连接邮件服务器并发送邮件
        server = smtplib.SMTP(smtp_host)
        server.login(user,password)
        print(type(message))
        server.sendmail(user,user_list,message.as_string())  # 必须得转成str
        server.close()

    def send_main(self,pass_num,fail_num):
        send_list = ["376904489@qq.com", "18600407736@163.com"]
        subject = "接口自动化测试结果"
        nums = pass_num + fail_num
        pass_percent = "%.2f%%" %(pass_num/nums*100)
        fail_percent = "%.2f%%" %(fail_num/nums*100)
        content = "本次测试，共执行用例%d个，成功%d个，失败%d个，成功率%s，失败率%s" \
                  %(nums, pass_num, fail_num, pass_percent, fail_percent)
        attach = '../config/cases.xls'
        self.send_email_attachment(send_list, subject, content, attach)

if __name__ == "__main__":
    email = SendEmail()
    email.send_main(2,7)



