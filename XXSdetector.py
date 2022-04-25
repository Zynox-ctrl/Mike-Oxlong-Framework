import requests
import time
def xxsdetect():
    target = input("[$]Target URL: ")
    payload = ("*script* alert('XSS'); /*script* ")
    req = requests.post(target + payload)
    if payload in req.text:
        print ("")
        print ("XSS Vulnerablity discovered!")
        print ("")
        print ("Refer to XSS payloads for further escalation")
        print("")
        time.sleep(10)
    else:
        print("Secure")
        time.sleep(10)