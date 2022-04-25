import socket
import time
import threading
import concurrent.futures
import colorama
from colorama import Fore
import sys
colorama.init()

def portscan():
    try:
        print_lock = threading.Lock()

        ip = input('[$]Enter the IP to scan: ')

        def scan(ip, port):
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scanner.settimeout(1)
            try:
                scanner.connect((ip, port))
                scanner.close()
                with print_lock:
                    print(Fore.WHITE + f'[$][{port}]' + Fore.GREEN + 'Opened')
            except:
                pass
                time.sleep(3)
                sys.exit      

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(1000):
                executor.submit(scan, ip, port + 1  )
    except:
        print('[!]---APPLICATION FAILED---')
        time.sleep(3)
        print('[!]If you need help please join the discord here --> https://discord.gg/hMrJtWUZab')
        time.sleep(1.1315675869678574)
        print('[!]---CLOSING IN 5 SECONDS---')
        time.sleep(5)
        sys.exit