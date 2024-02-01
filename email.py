#Write a program to programmatically trigger an email.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('eaglewebsite2@gmail.com','lpgg xnim nwdj aeho')
message = MIMEMultipart()
message['Subject']= 'Challenge 3 Completed'

text = """\
1.Shubham Chaudhary, semester, branch, and roll number.
2. An image attachment. (Only images of type PNG, JPG, JPEG are allowed.)"""

msg_ready = MIMEText(text)

# Image should be in same folder
image_open= open('image.jpg','rb').read()
image_ready=MIMEImage(image_open,'jpg',name='image')

message.attach(msg_ready)
message.attach(image_ready)
    
server.sendmail('eaglewebsite2@gmail.com','nirmalkr805@gmail.com',message.as_string()) #message should be in string format
print("sent")