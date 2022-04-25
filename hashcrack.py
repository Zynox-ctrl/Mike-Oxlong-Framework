import hashlib
import sys
import time

def crackhash():
    pass_hash = input('[$]Enter MD5 Hash: ')

    wordlist = input('[$]Wordlist File Name: ')

    try:
        pass_file = open (wordlist, 'r')
    except:
        print('[!]No file found')
        time.sleep(1)
        print('[!]---CLOSING---')
        time.sleep(1)
        sys.exit
    for word in pass_file:

        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()

        if digest == pass_hash:
            print('[!]Password Found')
            time.sleep(0.4574)
            print('[!]Password is ' + word)
            flag = 1
            time.sleep(20)
            print('[!]Closing in 10 seconds')
            break
        

    if flag == 0:
        print('[!]Password is not on the list')
        time.sleep(5)
        print('[!]---CLOSING---')