import re

mail_string = 'awesome_mail@GMAIL.COM'.lower()

domain = mail_string[mail_string.find("@"):]
username = mail_string[: mail_string.find("@")]

print(f'Username is {username} and domain is {domain}')