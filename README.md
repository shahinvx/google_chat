## Run This Django app (instructions)

- `Take a live demo`  [Click Here](https://google-log-chat.herokuapp.com/ "Heroku APP Demo") `or go google-log-chat.herokuapp.com`
- `YouTube link` [Click for YoyTube](https://youtu.be/6L3esKB2I48 "For Video demo") 
- `git clone github.com/shahinvx/google_chat.git`
- `cd google_chat`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- `open http://127.0.0.1:8000/ in your browser` or [Click Here](https://google-log-chat.herokuapp.com/ "Heroku APP Demo")
- `Admin/Login user : shahinvx | pass : shahin `

## All API in Swagger Documentation

- `http://127.0.0.1:8000/swagger/` or `google-log-chat.herokuapp.com/swagger` [Click Here](https://google-log-chat.herokuapp.com/swagger "Swagger API DOC")

## About this APP

You Both can Chat by just Log-In with your Google Account.

- User
  - Get user info from Google API.
  - Chat with currently login users.
  
- Chat
  - Implement chat using `AsyncWebsocketConsumer` and JS `WebSocket`
  - `CHANNEL_LAYERS` BACKEND: `channels.layers.InMemoryChannelLayer`
  - `ASGI_APPLICATION` is `routing.application`
  
- Authentication
  - Google Authentication by Django all-auth
  
- Additional INFO
  - DRF (Django Rest Framework)
  - Swagger and Redoc for Documentation
  - Django Templates with ajax and javascript, Django all-auth, Django Channels

- Resources
  -  `Django all-auth`  [Click Here](https://django-allauth.readthedocs.io/en/latest/ "all-auth") or go `django-allauth.readthedocs.io`
  -  `Django Channels`  [Click Here](https://channels.readthedocs.io/en/latest/index.html "channels") or go `channels.readthedocs.io`

## Deployment Issues and Solve
- You can visit login with your Google account but The chat messages are not delivered to other person, because i use `InMemoryChannelLayer` for this App
- You can solve this issue by using `Daphne and RedisChannelLayer` (I will use those for my next `asgi` App)

## Swegger Documentation preview

![Swegger Documentation](/Screen_Doc/swagger.png)

## Gif of this Google Chat
<img src="/Screen_Doc/g_chat_app.gif" width="995" height="460"> 

## All View inside APP
<img src="/Screen_Doc/1.png" width="412" height="235"> <img src="/Screen_Doc/1.png" width="412" height="235">
<img src="/Screen_Doc/2.jpg" width="412" height="235"> <img src="/Screen_Doc/3.jpg" width="412" height="235">
<img src="/Screen_Doc/4.png" width="412" height="235"> <img src="/Screen_Doc/5.png" width="412" height="235">
<img src="/Screen_Doc/6.png" width="412" height="235"> <img src="/Screen_Doc/7.png" width="412" height="235">
<img src="/Screen_Doc/8.png" width="412" height="235"> <img src="/Screen_Doc/9.png" width="412" height="235">
<img src="/Screen_Doc/10.png" width="412" height="235"> <img src="/Screen_Doc/11.png" width="412" height="235">
<img src="/Screen_Doc/12.png" width="995" height="460"> 

#
### The MIT License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
