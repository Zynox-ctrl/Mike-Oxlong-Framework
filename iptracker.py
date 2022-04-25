import json
import requests
import time

def iptrack():
    target_ip = input("[$]Enter The IP You Want To Track: ")
    api = "http://ip-api.com/json/"

    res = requests.get(api + target_ip)

    data = res.json()

    print("[!]IP Country Is: ", data["country"])
    print('[!]IP Region is: ', data['regionName'])
    print('[!]IP City is: ', data['city'])
    print('[!]IP ZIP is: ', data['zip'])
    print('[!]IP Latitude is: ', data['lat'])
    print('[!]IP Longtitude is: ', data['lon'])
    print('[!]IP Timezone is: ', data['timezone'])
    print('[!]IP ISP is: ', data['isp'])
    print('[!]IP Org is: ', data['org'])
    print('[!]---CLOSING IN 5 MINUTES---')
    time.sleep(300)