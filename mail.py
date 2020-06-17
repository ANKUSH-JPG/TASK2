#!/usr/bin/env python

import smtplib
file=open('error.txt','r')


error=file.read()
file.close()

Text="The page isnt working . HTTP ERROR "

message=Text+" "+error
s=smtplib.SMTP(host='smtp.gmail.com',port=587)

s.starttls()
s.login("forallchallenge@gmail.com","Ankush@12345")

s.sendmail("forallchallenge@gmail.com","forallchallenge@gmail.com",message)
s.quit()





