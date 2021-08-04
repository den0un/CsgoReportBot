import time
import os
import random
import defs

victim_profile = input("give victim's profile URL:")

with open('accounts.txt', 'r') as file:
    
    for creds in file:
        
        os.system('cls')
        username, password = creds.strip('\n').split(':')

        report_reason = random.choice(
            ['he has cheats wallhack', 'he is cheating its obvious radar hack', 'aimboting on mm ? why VAC',
             'just fucking ban this kid he is ranging with cheats !!',
             'just going to commit suicide cuz of these cheaters',
             'spin bot cheat very clear'])

        print('[*] Account name: "' + username + '"...')
        time.sleep(1)

        header = defs.get_header()

        login = defs.login(username, password, header)

        if login["success"]:

            print("[+] Logged in !!")
            time.sleep(1)

            print("[*] Getting Victim's ID...")

            time.sleep(1)
            victim_id = defs.get_id(victim_profile, header)

            time.sleep(1)
            report_code = defs.report(victim_id, report_reason, header)

            if report_code == '1':

                print('[+] Profile Reported Successfully !!')
                time.sleep(2)

            elif report_code == '25':

                print('[*] Profile already Reported !!')
                time.sleep(2)

            else:

                print('[-] Error something wrong happened !!')
                break

        else:

            print("[-] Error, could not login:", login["message"])
            break
