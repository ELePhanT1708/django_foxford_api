# django-foxford-api

## Intro 
Проект является тестовым. 
Задание https://docs.google.com/document/d/18PU6sS7l71cXKW6wRw9q6ovcswMSEHL31lO1aTkbAos/edit

Проект использует Django, djangorestframework and postgres with adminer in docker image


Джанго сервер запускается как обычно , база данных запускается в контейнере для удобства

Особенность в том, что есть django-template-rendering как небольшой UI для работы с сущностями без АПИ 
Также реализована АПИ на django_rest_framework с помощью вьюсетов



## To launch the system
1. Clone the repo 
2. Launch docker desktop
3. Open powershell or etc in project directory 'django_foxford_api'
4. In cloned directory from powershell or something similar write:
    - 'docker-compose up --build' : поднимится сервер с базой данных и графическим интерфейсом adminer для него
5. In other window of powershell in the same directory call: py .\foxford_api\manage.py runserver


##
That's all !!
----
     
