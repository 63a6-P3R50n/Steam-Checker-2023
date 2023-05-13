# Steam-Checker-2023
### About
This is a very simple steam account checker, written by me as my first python project. It uses multi-threading and http/https proxy in format http://{ip}:{port} .
On this checker I tested my knowledge of the python language, therefore, those who know do not swear much.
### Requirements
- requests
- rsa
- base64
- time
- random
- io
- certifi
- threading
- fake_headers
- bs4
- colorama
### Features
- Multithreading (but because of my little knowledge of multithreading, it came out cringe)
- HTTP/HTTPS Proxy
- Generating Headers for request
- Debug Mode
- Games parsing bypass (I realise this through a request to saves on steam cloud and parsing the names of the games)
### Known problems
- 429 Steam Error at third request (I still don't know how bypass this, so I added just a repeat request after 60 seconds)
- Steam games parsing is not via https://steamcommunity.com/id.../games /?tab=all (I do not know how to realise this, because when i send request to this link, the html code is not contains list of games)
- Some problems with parsing VAC and Games
### PS
If you can explain to me or suggest your changes in my code, then please contact me by email: dr9256228@gmail.com
