# Steam-Checker-2023
### About
This is a very simple steam account checker, written by me as my first python project. It uses multi-threading and http/https proxy in format http://{ip}:{port} .
On this checker I tested my knowledge of the python language, therefore, those who know do not swear much.
### Features
- Multithreading (but because of my little knowledge of multithreading, it came out cringe)
- HTTP/HTTPS Proxy
- Generating Headers for request
- Debug Mode
### Known problems
- 429 Steam Error at third request (I still don't know how bypass this, so I added just a repeat request after 60 seconds)
- Steam games parsing is not via https://steamcommunity.com/id.../games /?tab=all (I do not know how to implement this, because when you request this link, the html code of the games is not output)
