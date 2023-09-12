# Steam Checker 2023
![alt text](https://github.com/Fsocguy/Steam-Checker-2023/blob/main/Preview.png)
### About
ENG:
This is a very simple Steam account checker, written by me as my first python project. It's more stable than version 1.0 
I've updated the design of the script, so it looks neater and more user friendly.
I have rewritten the code of the first version and now it is more readable, some functions are reworked and simplified, due to this the script works a little faster and gives more correct information.

As of 07/29/23, I have released version 2.0 with all fixes and changes, as well as modified Readme.md and added requirements.txt to make the script easier to use.
I removed multithreading since based on the captcha problem, it will be useless...

RU:
Это очень простой скрипт для проверки аккаунтов Steam, написанный мной в качестве моего первого проекта на python. Он более стабилен, чем версия 1.0. 
Я обновил дизайн скрипта, теперь он выглядит более аккуратным и удобным.
Я переписал код первой версии и теперь он стал более читабельным, некоторые функции переработаны и упрощены, благодаря чему скрипт работает немного быстрее и выдает более корректную информацию.

По состоянию на 29.07.23 я выпустил версию 2.0 со всеми исправлениями и изменениями, а также изменил Readme.md и добавил requirements.txt, чтобы сделать скрипт более удобным в использовании.
Я убрал многопоточность, так как, судя по проблеме с капчей, она будет бесполезна...

### Features
ENG:
- Stability
- HTTP/S Proxy support (In format: {proxy type}://{ip}:{port})
- Parsing detailed account information (Nickname, Level, Balance, KT, VAC, Limit, Games and more...)
- Repeating the request in case of an error (except for the case with captcha)

RU:
- Стабильность
- Поддержка HTTP/S прокси (В формате: {proxy type}://{ip}:{port})
- Парсинг более подробной информации об аккаунте (Никнейм, Уровень, Баланс, Бан сообщества, ВАК Бан, Лимит, Игры и многое другое...)
- Повтор запроса в случае ошибки (кроме случая с капчей)
### Known problems
ENG:
- Captcha 
- Parser bugs are possible if the account is blocked in the community

RU:
- Капча
- Баги парсера, в случае если аккаунт имеет бан сообщества

### In addition
ENG:
Since I am a beginner python developer, I may not know many things, so if you are interested in this code and have suggestions on how I can improve it, or want to point out my mistakes, please contact me: dr9256228@gmail.com

RU:
Поскольку я начинающий python-разработчик, я могу не знать многих вещей, поэтому если вас заинтересовал этот код и у вас есть предложения, как я могу его улучшить, или вы хотите указать на мои ошибки, пожалуйста, свяжитесь со мной: dr9256228@gmail.com
