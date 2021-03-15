# coding:utf-8
import smtplib
from email.mime.text import MIMEText

global send_user
global email_host
global password


class SendEmail:

    def send_mail(self, user_list, sub, content):
        send_user = "767067326@qq.com"
        email_host = "smtp.qq.com"
        password = "znifxjqxmwcvbbha"
        user = "唐顺意" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())

    def send_main(self, pass_list, fail_list):
        pass_num = len(pass_list)
        fail_num = len(fail_list)
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num / count_num * 100)
        fail_result = "%.2f%%" % (fail_num / count_num * 100)
        user_list = ['1063712856@qq.com']
        sub = "接口自动化测试"
        content = "此次一共运行接口个数为%s个, 通过个数为%s, 失败个数为%s, 通过率为%s, 失败率为%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)



