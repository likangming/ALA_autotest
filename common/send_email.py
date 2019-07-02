#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/6/14 20:39
@Author   : Damon
@Email    : kangming40@163.com
@File     : send_email.py
@Software : PyCharm
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from ALA_WeChat_1.common.config import conf
from ALA_WeChat_1.common.contants import report_dir


class Sendemail:
    """
    自定义发送email类：
    """
    # 第三方SMTP服务
    # mail_host = 'smtp.exmail.qq.com'
    # mail_user = 'kevin.li@alavening.com'
    # mail_pw = 'P0ssW@rd'
    mail_host = conf.get('email', 'mail_host')
    mail_user = conf.get('email', 'mail_user')
    mail_pw = conf.get('email', 'mail_pw')

    sender = 'kevin.li@alavening.com'
    receivers = ['kevin.li@alavening.com', '359027585@qq.com']

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['from'] = 'kevin.li@alavening.com'  # 发送者，最好要与发送者一致，其他可能出错哦
    message['to'] = 'kevin.li@alavening.com, 359027585@qq.com'  # 接收者，最好也要一致: 应该是要以邮件后缀名结束，前面名字不影响
    subject = '测试发送邮件带附件5'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文
    message.attach(MIMEText('这是测试正文', 'plain', 'utf-8'))

    # 构造附件1：传送当前目录下的report.html文件   要添加多个文件，重复该不在则可
    att1 = MIMEText(open(report_dir + r'/report.html', 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    # 这里的filename写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename尽量还是写要发送的文件及其格式
    message.attach(att1)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user, mail_pw)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print('邮件发送成功')
        smtpObj.quit()
    except smtplib.SMTPException:
        print('Error:无法发送邮件')


send_email = Sendemail()
# if __name__ == '__main__':
#     send_email
