import base64
import requests
from bs4 import BeautifulSoup
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import time
import json
import random



with requests.session() as session:

    def get_header():
        file = open('user-agents.txt', 'r').read().splitlines()
        random_agent = random.choice(file).strip('\n')
        header = {'User-Agent': random_agent}
        return header


    def enc_pass(response,password):
        key_mod = int(str(response["publickey_mod"]), 16)
        key_exp = int(str(response["publickey_exp"]), 16)
        rsa_key = RSA.construct((key_mod, key_exp))
        cipher = PKCS1_v1_5.new(rsa_key)
        password_enc = base64.b64encode(cipher.encrypt(str(password.strip('\n')).encode(encoding="utf-8")))
        return password_enc


    def login(username,password,header):

        print('[*] Getting RSA Key...')

        key_data = {'username': username,
                    'donotcache': str(int(time.time() * 1000)),
                    }
        response = json.loads(session.post(url='https://steamcommunity.com/login/getrsakey/', headers=header, data=key_data).text)

        time.sleep(1)
        print('[+] Get Key Success !!')

        time.sleep(1)
        print('[*] Loging in...')

        password_enc = enc_pass(response, password)
        login_data = {
            'username': username,
            'password': password_enc,
            'emailauth': '',
            'loginfriendlyname': '',
            'captchagid': '-1',
            'captcha_text': '',
            'emailsteamid': '',
            'rsatimestamp': response['timestamp'],
            'remember_login': False,
            'donotcache': str(int(time.time() * 1000)) }

        response = json.loads(session.post(url='https://steamcommunity.com/login/dologin/', data=login_data, headers=header).text)
        return response


    def report(victim_id,report_reason,header):

        print('[*] Reporting...')
        time.sleep(1)
        print('[*] Reason: ' + report_reason)

        session.get(url='https://steamcommunity.com/actions/ReportProfile/' + victim_id, headers=header)

        data = {
            'sessionID': session.cookies['sessionid'],
            'step': '12',
            'steamid': victim_id
        }
        session.post(url='https://steamcommunity.com/actions/AjaxGetReportProfileStep/', data=data,
                     headers=header)

        data = {
            'sessionid': session.cookies['sessionid'],
            'json': '1',
            'abuseID': victim_id,
            'eAbuseType': '10',
            'abuseDescription': report_reason,
            'ingameAppID': '730'  # steam_appID=753 csgo_appID=730
            }

        response = session.post(url='https://steamcommunity.com/actions/ReportAbuse/', headers=header,
                                data=data).text
        return response

    def get_id(victim_profile,header):
        response = session.get(url=victim_profile,headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.select('a[onclick*="ReportProfile"]')
        for i in soup:
             victim_id = (i['onclick'].strip("ReportProfile( '").strip("; HideMenu( 'profile_action_dropdown_link', 'profile_action_dropdown' ); return false;").strip('\n'))

        print("[+] ID Gotten Successfully !! ID="+victim_id)
        return victim_id