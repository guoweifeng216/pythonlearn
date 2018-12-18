#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2018/12/17 14:02
@filename:Welcome_Email_by_SendGrid

"""
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("751836589@qq.com")
to_email = Email("782388110@qq.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)