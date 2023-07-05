## Как запустить проект:
- 1 Склонировать репозиторий - `git clone`
- 2 Установить зависимости `pip install -r requirements.txt`
- 3 Выполнить миграции
- - `py manage.py makemigrations`
- - `py manage.py migrate`
- 4 Получить репозитории организации `py manage.py get_repos`
- 5 Запустить проект `py manage.py runserver`

#### Спецификация API доступна по адресу - `http://127.0.0.1:8000/api/v1`