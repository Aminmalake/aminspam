import requests,uuid,secrets

from time import sleep

uid = uuid.uuid4()

r = requests.Session()

cookie = secrets.token_hex(8)*2

print( "         ")

print( "         ")

print( " \033[1;92m║══▒═✺═▒═✺═▒═══¤═¤═¤════════════¤═══║")

print( " \033[1;96m║✯ Creator ✯ AMIN MALAKE        ║")

print( " \033[1;98m║✯       𓆩 𝖆 𝖒 𝖎 𝖓 𓆪            ║")

print( " \033[1;96m║✯ instagram : i4m.amin         ║")

print( " \033[1;92m║══▒═✺═▒═✺═▒═══¤═¤═¤════════════¤═══║")

print( "          ")

print( "          ")

username = input('\033[1;96mnawe instakat:')

print( "          ")

password = input('password instakat:')

print( "          ")

target = input('nawe awkasay reporte akay:')

print( "          ")

sle = int(input('xeraye reportaka:'))

def login():

    global username

    global password

    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125                   >

    data = {'username':username,

            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),

            'queryParams': '{}',

            'optIntoOneTap': 'false',}

    req_login = r.post(url,headers=headers,data=data)

    if ("userId") in req_login.text:

        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})

        print('\033[1;93minstakat krayawa ✅')

        url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)

        req_id = r.get(url_id).json()

        user_id = str(req_id['logging_page_id'])

        idd = user_id.split('_')[1]

        done = 1

        while True:

            url_report = 'https://www.instagram.com/users/{}/report/'.format(idd)

            datas = {'source_name':'','reason_id':1,'frx_context':''} #spam

            report = r.post(url_report,data=datas)

            print('\033[1;92mspam ✅ {}'.format(done))

            sleep(sle)

            done += 1

    else:

        print('instakat nakrayawa ❌')

        exit()

login()
