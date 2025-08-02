import os
import requests
from hashlib import md5
from time import time
import random
import re
import threading

# Color definitions for terminal output
R1 = '\x1b[38;5;51m'  # Cyan
R2 = '\x1b[38;5;214m' # Orange
R3 = '\x1b[38;5;165m' # Purple
R4 = '\x1b[38;5;87m'  # Light blue
R5 = '\x1b[38;5;197m' # Pink
R6 = '\x1b[38;5;226m' # Yellow

from cfonts import render
import sys
import time
import webbrowser

password = 'armaan'
pss = input('\x1b[1;32m PASSWORD : ')

def colorful_loader():
    colors = [
        '\x1b[1;91m',  # Light red
        '\x1b[1;92m',  # Light green
        '\x1b[1;93m',  # Light yellow
        '\x1b[1;94m',  # Light blue
        '\x1b[1;95m',  # Light magenta
        '\x1b[1;96m',  # Light cyan
        '\x1b[1;97m',  # White
    ]
    
    bar_length = 50
    for i in range(bar_length + 1):
        bar = "▓" * i
        color = colors[i % len(colors)]
        sys.stdout.write("\r" + color + bar + "\x1b[0m" + "░" * (bar_length - i))
        sys.stdout.flush()
        time.sleep(0.1)
    
    print() 

colorful_loader()
os.system('clear') 

if pss == password:
    print('\x1b[1;32m⠀⠀ \n\n\n                         CORRECT PASSWORD ✅ ')
    time.sleep(2)
    os.system('clear')
else:
    sys.exit('\x1b[1;31m           WRONG PASSWORD❌ ')

webbrowser.open('https://instagram.com/@efkzw')
print("\033[91m")
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⣠⣴⣿⣁⣠⣤⣶⣶⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣶⣶⣶⡶⠂⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠀⠀⠀
⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡇⠀⠀⠀
⠀⠀⣿⣿⣿⡏⠉⠉⠀⠁⠀⠀⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣠⠀⠀⠀
⠀⠀⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⢸⠏⣹⡿⢻⣿⣿⣿⣿⣿⠃⠀⠀⠀
⠀⠀⢸⣿⣿⡿⢤⣌⡀⠀⠀⠀⢸⠹⣿⡇⢸⣿⣿⣿⣿⣿⠛⠁⠀⠀
⠀⠀⢸⣿⣿⡇⠈⠿⠇⠀⠀⠀⠀⠀⠈⣴⣿⣿⣿⣿⣿⡿⠟⠂⠀⠀
⠀⠀⠸⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⢿⣆⠀⠀⠀
⠀⠀⠀⣿⡟⣿⣷⡀⠀⠀⠀⠄⠤⠄⠀⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀
⠀⠀⠀⢻⠃⢿⡟⡇⢠⠆⡤⢀⠀⠀⠐⠯⡈⢿⢿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠸⠀⠁⠀⡠⡎⠀⠀⠀⠀⠀⢸⣿⣦⡈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠊⢀⠀⠀⡆⠀⠀⣠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠌⠀⠀⢸⠀⢠⡇⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠔⠁⠀⠀⠀⠘⠀⣾⣷⣤⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⡀⠁⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⣠⣎⠀⠀⠀⠀⠀⣠⣶⣄⢂⢀⣼⣿⣿⣿⣿⡏⠀⠀⠈⠂⠀⠀⠀⠀⠀
⠙⠛⢷⣦⣀⢠⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⡏⠀⠀⠈⠂⡀⠀⠀⠀⠀
⠀⠀⠀⠈⡻⠿⠛⠋⠉⣁⣀⠠⠤⠤⡤⢌⣀⡉⠁⠐⠂⡀⠀⠀⠀⠀
⠀⠀⢠⡊⠀⠒⠁⢈⣀⣀⣤⣤⣤⣤⣤⣤⣤⡀⢀⠈⠠⠀⠀⠀⠀⠀
⠀⢠⣿⠇⢀⣴⣿⠟⢋⣭⣿⣿⣌⡉⠻⣿⣿⣷⡄⡀⠀⠀⠀⠀⠀⠀
⠀⡎⢫⣶⣿⠟⣡⣶⣿⣿⣿⣿⣿⢿⣦⣄⡙⠿⣷⣌⡐⠨⢶⣦⣤⡀
⠀⠣⢼⠟⣡⣾⣿⣿⣿⣿⠿⠃⠀⠀⠉⠛⠿⣷⣿⣿⣿⡔⠠⠄⠁⠀
⠀⠀⠘⣶⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣦⣄⠄⠀
⠀⠀⠀⢻⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⡇⠀⠀
⠀⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⠀⠀
⢀⣴⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⡄
⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠃
""")
print("\033[0m")

def typewriter(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

text = "Telegram ==> @armtrn   instagram ==> @efkzw"
typewriter(text, 0.2)
print()
text = "Good usage.. Armaan's regards to you."
typewriter(text, 0.1)
print()
os.system('clear')

class InstagramReporter:
    def __init__(self):
        self.success_count = 0
        self.failure_count = 0
        self.unknown_count = 0       
        self.session = requests.Session()
        self.csrftoken = self.get_csrf_token()
        self.sessionid = input("Enter SessionID: ")
        self.cookies = {'sessionid': self.sessionid}
        
        # Validate session
        response = self.session.get(
            'https://i.instagram.com/api/v1/accounts/current_user/?edit=true',
            headers={
                'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-app-id': '936619743392459'
            },
            cookies=self.cookies
        ).text   
        
        if 'primary_profile_link_type' in response:
            pass        	
        else:
            print('Session ID is incorrect or expired. Get a new one')
            exit()                 
            
    def get_csrf_token(self):
        response = self.session.get(
            "https://i.instagram.com/api/v1/accounts/login/",
            headers={
                "User-Agent": "Instagram 64.0.0.11.97 Android (21/5.0.2; 240dpi; 540x886; LGE/lge; LG-D618; g2mds; g2mds; pt_BR)"
            }
        )
        return response.cookies.get("csrftoken")
    
    def get_user_id(self, username):
        url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
        headers = {'x-ig-app-id': '936619743392459'}
        try:
            response = self.session.get(url, headers=headers)
            user_data = response.json().get('data', {}).get('user', {})
            user_id = user_data.get('id')        
        except:
            print('Invalid username')
            exit()
        return user_id
        
    def get_story_id(self, user_id):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': str(random.randint(30000, 79999)),
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax': str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }    	
        
        data = {
            'fb_api_req_friendly_name': 'PolarisStoriesV3ReelPageGalleryQuery',
            'variables': f'{{"initial_reel_id":"{user_id}","reel_ids":["{user_id}","65467266760"],"first":1}}',
            'server_timestamps': 'true',
            'doc_id': '8481088891928753'
        }
        
        response = self.session.post(
            'https://www.instagram.com/graphql/query',
            cookies=self.cookies,
            headers=headers,
            data=data
        ).text   
        
        if 'organic_tracking_token' in response:
            pattern = r'"pk":"(\d{19})"'
            match = re.search(pattern, response)
            object_id = match.group(1)   
        else:    		
            print('No stories found on this account or account is private')
            exit()
        return object_id
        
    def get_report_info(self, object_id):    
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': str(random.randint(30000, 79999)),
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax': str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }
        
        data = {
            'container_module': 'StoriesPage',
            'entry_point': '1',
            'location': '4',
            'object_id': object_id,
            'object_type': '1',
            'frx_prompt_request_type': '1'
        }
        
        response = self.session.post(
            'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
            headers=headers,
            data=data,
            cookies=self.cookies
        )    
        
        response_json = response.json()
        report_info = response_json.get('response', {}).get('report_info', {})
        context = response_json.get('response', {}).get('context', {})
        object_id = report_info.get("object_id", "").strip('"')       
        reporter_id = report_info.get("reporter_id", "").strip('"')
        responsible_id = report_info.get("responsible_id", "").strip('"')   
        return object_id, context
        
    def show_report_menu(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{R1}╔════════════════════════════╗")
        print(f"{R1}║       REPORT MENU          ║")
        print(f"{R1}╠════════════════════════════╣")
        print(f"{R2}║  [1] I don't like this    ║")
        print(f"{R3}║  [2] Harassment/Bullying  ║")
        print(f"{R5}║  [3] Suicide/Self-harm    ║")
        print(f"{R6}║  [4] Violence/Hate         ║")
        print(f"{R2}║  [5] Sale/Promotion       ║")
        print(f"{R3}║  [6] Nudity/Sexual        ║")
        print(f"{R5}║  [7] Scam/Spam            ║")
        print(f"{R6}║  [8] False Information     ║")
        print(f"{R1}╚════════════════════════════╝")
        print('')              
        choice = input(f"{R4}➤ Make your choice: ")
        
        if choice == '1':
            self.report_tag = 'ig_i_dont_like_it_v3'
        elif choice == '2':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R2}║  [1] Nude Image Threat    ║")
            print(f"{R3}║  [2] Harassment/Abuse     ║")
            print(f"{R5}║  [3] Misleading/Spam      ║")
            print(f"{R1}╚════════════════════════════╝")
            choice2 = input(f"{R4}➤ Make your choice: ")
            if choice2 == '1':
                self.report_tag = 'adult_content-threat_to_share_nude_images-u18-yes'
            elif choice2 == '2':
                self.report_tag = 'adult_content-threat_to_share_nude_images-u18-yes'
            elif choice2 == '3':
                self.report_tag = 'adult_content-threat_to_share_nude_images-u18-yes'
            else:
                exit()        	       		
        elif choice == '3':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R5}║  [1] Suicide/Self-harm    ║")
            print(f"{R6}║  [2] Eating Disorders     ║")
            print(f"{R1}╚════════════════════════════╝")
            choice3 = input(f"{R4}➤ Make your choice: ")
            if choice3 == '1':
                self.report_tag = 'suicide_or_self_harm_concern-suicide_or_self_injury'
            elif choice3 == '2':
                self.report_tag = 'suicide_or_self_harm_concern-eating_disorder'
            else:
                exit()
        elif choice == '4':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R2}║  [1] Credible Threat       ║")
            print(f"{R3}║  [2] Terrorism/Org. Crime  ║")
            print(f"{R5}║  [3] Exploitation         ║")
            print(f"{R6}║  [4] Incitement to Violence║")
            print(f"{R2}║  [5] Hate Speech           ║")
            print(f"{R3}║  [6] Graphic Violence     ║")
            print(f"{R5}║  [7] Animal Abuse          ║")
            print(f"{R1}╚════════════════════════════╝")
            choice4 = input(f"{R4}➤ Make your choice: ")
            if choice4 == '1':
                self.report_tag = 'violent_hateful_or_disturbing-terrorism_or_organized_crime'
            elif choice4 == '2':
                self.report_tag = 'violent_hateful_or_disturbing-terrorism_or_organized_crime'
            elif choice4 == '3':
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"{R1}╔════════════════════════════╗")
                print(f"{R1}║        SUBMENU             ║")
                print(f"{R1}╠════════════════════════════╣")
                print(f"{R2}║  [1] Human Trafficking     ║")
                print(f"{R3}║  [2] Sexual Exploitation   ║")
                print(f"{R1}╚════════════════════════════╝")
                choice5 = input(f"{R4}➤ Make your choice: ")
                if choice5 == '1':
                    self.report_tag = 'human_trafficking'
                elif choice5 == '2':
                    self.report_tag = 'violence_hate_or_exploitation-sexual_exploitation-yes'
                else:
                    exit()        		    
            elif choice4 == '4':
                self.report_tag = 'violent_hateful_or_disturbing-violence'
            elif choice4 == '5':
                self.report_tag = 'violent_hateful_or_disturbing-promotes_hate-hate_speech_or_symbols'
            elif choice4 == '6':
                self.report_tag = 'violent_hateful_or_disturbing-violence_death_or_severe_injury'
            elif choice4 == '7':
                self.report_tag = 'violent_hateful_or_disturbing-animal_abuse'
            else:
                exit()      	
        elif choice == '5':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R2}║  [1] Drugs                 ║")
            print(f"{R3}║  [2] Weapons               ║")
            print(f"{R5}║  [3] Animals               ║")
            print(f"{R1}╚════════════════════════════╝")
            choice6 = input(f"{R4}➤ Make your choice: ")
            if choice6 == '1':
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"{R1}╔════════════════════════════╗")
                print(f"{R1}║        SUBMENU             ║")
                print(f"{R1}╠════════════════════════════╣")
                print(f"{R2}║  [1] High-Risk Drugs      ║")
                print(f"{R3}║  [2] Prescription Drugs    ║")
                print(f"{R5}║  [3] Other Drugs           ║")
                print(f"{R1}╚════════════════════════════╝")
                choice7 = input(f"{R4}➤ Make your choice: ")
                if choice7 == '1':
                    self.report_tag = 'selling_or_promoting_restricted_items-drugs-high-risk'
                elif choice7 == '2':
                    self.report_tag = 'selling_or_promoting_restricted_items-drugs-prescription'
                elif choice7 == '3':
                    self.report_tag = 'selling_or_promoting_restricted_items-drugs-other'
                else:
                    exit()
            elif choice6 == '2':
                self.report_tag = 'selling_or_promoting_restricted_items-weapons'
            elif choice6 == '3':
                self.report_tag = 'selling_or_promoting_restricted_items-animals'
            else:
                exit()
            
        elif choice == '6':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R2}║  [1] Nude Image Threat    ║")
            print(f"{R3}║  [2] Prostitution          ║")
            print(f"{R5}║  [3] Sexual Exploitation   ║")
            print(f"{R6}║  [4] Nudity/Sexual        ║")
            print(f"{R1}╚════════════════════════════╝")
            choice8 = input(f"{R4}➤ Make your choice: ")
            if choice8 == '1':
                self.report_tag = 'adult_content-threat_to_share_nude_images-u18-yes'
            elif choice8 == '2':
                self.report_tag = 'adult_content-prostitution'
            elif choice8 == '3':
                self.report_tag = 'violence_hate_or_exploitation-sexual_exploitation-yes'
            elif choice8 == '4':
                self.report_tag = 'adult_content-nudity_or_sexual_activity'
            else:
                exit()
                
        elif choice == '7':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R2}║  [1] Fraud/Scam           ║")
            print(f"{R3}║  [2] Spam/Annoying        ║")
            print(f"{R1}╚════════════════════════════╝")
            choice9 = input(f"{R4}➤ Make your choice: ")
            if choice9 == '1':
                self.report_tag = 'misleading_annoying_or_scam-fraud_or_scam'
            elif choice9 == '2':
                self.report_tag = 'misleading_annoying_or_scam-annoying_or_spam'
            else:
                exit()
        elif choice == '8':
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f"{R1}╔════════════════════════════╗")
            print(f"{R1}║        SUBMENU             ║")
            print(f"{R1}╠════════════════════════════╣")
            print(f"{R2}║  [1] Health                ║")
            print(f"{R3}║  [2] Politics              ║")
            print(f"{R5}║  [3] Social Issues         ║")
            print(f"{R6}║  [4] Digital Content       ║")
            print(f"{R1}╚════════════════════════════╝")
            choice10 = input(f"{R4}➤ Make your choice: ")
            if choice10 == '1':
                self.report_tag = 'misleading_annoying_or_scam-false_information-health'
            elif choice10 == '2':
                self.report_tag = 'misleading_annoying_or_scam-false_information-politics'
            elif choice10 == '3':
                self.report_tag = 'misleading_annoying_or_scam-false_information-social_issues'
            elif choice10 == '4':
                self.report_tag = 'ig_deepfake'
            else:
                exit()
        else:
            exit()
        
        return self.report_tag
        
    def check_session_status(self):
        response = requests.get(
            'https://i.instagram.com/api/v1/accounts/current_user/?edit=true',
            headers={
                'User-Agent': 'Instagram 136.0.0.34.124 Android (23/6.0.1; 640dpi; 1440x2560; samsung; SM-G935; hero2lte; samsungexynos8890; en_US; 208061712)',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ig-app-id': '936619743392459'
            },
            cookies=self.cookies
        ).text
        
        if 'login_required' in response:
            self.session_valid = False
        else:
            self.session_valid = True    	  		
        
    def submit_report(self, object_id, context):
        headers = {
            'accept-language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
            'x-asbd-id': str(random.randint(30000, 79999)),
            'x-csrftoken': self.csrftoken,
            'x-ig-app-id': str(random.randint(1000,3337)),
            'x-ig-www-claim': 'hmac.AR1qzeEVPBuPPsJxBMlPlU19lLRm0LG3bSnly_p3mz0aRW2P',
            'x-instagram-ajax': str(random.randint(100, 3939)),
            'x-requested-with': 'XMLHttpRequest'
        }
        
        data = {
            'container_module': 'StoriesPage',
            'entry_point': '1',
            'location': '4',
            'object_id': object_id,
            'object_type': '1',
            'context': context,
            'selected_tag_types': f'["{self.report_tag}"]',
            'frx_prompt_request_type': '2',
        }
    
        response = self.session.post(
            'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
            headers=headers,
            data=data,
            cookies=self.cookies
        )       
        if '"text":"Done"' in response.text:
            self.success_count += 1
        elif 'Try Again Later' in response.text:
            print('Get a new Session ID')   
        else:
            self.failure_count += 1        
            
        self.check_session_status()                        
        os.system('clear' if os.name == 'posix' else 'cls')                
        print(f'''\r{R4}{"="*90}
{" "*25}{R4}{"="*5}  
Successful: {self.success_count}  
{R3}Failed: {self.failure_count}  
{"="*5}
{"="*90}\r''')
     
        
    def start_reporting(self):
        username = input('Enter username: ')
        os.system('clear' if os.name == 'posix' else 'cls')
        user_id = self.get_user_id(username)
        object_id = self.get_story_id(user_id)
        object_id2, context = self.get_report_info(object_id)
        self.show_report_menu()
        while True:
            self.submit_report(object_id2, context)
     
reporter = InstagramReporter()
reporter.start_reporting()