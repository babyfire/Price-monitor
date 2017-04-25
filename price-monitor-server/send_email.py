# -*- coding: utf-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class SendEmail(object):
    # 发送邮箱设置(之后需要设置在txt中以保障密码安全性)
    from_addr = '3120611047@ujs.edu.cn'
    password = '931102s'
    smtp_server = 'mail.ujs.edu.cn'

    def __init__(self, text, sender, receiver, subject, address):
        self.text = text
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.address = address
        self.to_addr = address
        # 从上到下依次是: 邮件内容,邮件发送者昵称,邮件接收者昵称,邮件主题
        self.msg = MIMEText(self.text, 'plain', 'utf-8')
        self.msg['From'] = self._format_addr(self.sender + '<' + self.from_addr + '>')
        self.msg['To'] = self._format_addr(self.receiver + '<' + self.to_addr + '>')
        self.msg['Subject'] = Header(self.subject, 'utf-8').encode()

    # 编写了一个函数_format_addr()来格式化一个邮件地址
    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send(self):
        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()

# sendemail = SendEmail('111', 'wo', 'ni', 'zhuti', 'yangzd1993@foxmail.com')
# sendemail.send()