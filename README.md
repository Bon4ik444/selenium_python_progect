# Проэкт по использованию python, selenium or pytest
Пошаговая инструкция.
1. Создать файл с названием проекта.
2. Создать папку README.md
    1. Заходим в гит и делаем иницилизацию ветки мастер(master)
    ```
    git init
    ```
    2. Проверка файла реадми
    ```
    git status
    ```
    3. Загрузить файл и коммитнуть
    ```
    git add (имя фвйлф или . который все загрузит)

    git commit -m "message commit"

    git status(просто проверка)
    ```
3. Заходим в git bash
    1. Если нет мастера то:
    ```
    git init
    ```
    2. Установка вирт окруж
    ```
    python -m venv venv-(имя венва может быть любым(Чтото-venv))
    ```
    3. Если версия пайтона не тот то можно поменять его:
    ```
    python3.13 -m venv venv
    or
    python -3.13 -m venv venv 
    ```
    4. Активируем вирт окруж.
    ```
    source name_venv/Scripts/activate
    ```
    5. Устанавливаем нужные вещи.
    ```
    pip install (то что хочешь загрузить)
    ```
    6. Создаем файл requirements.txt
    ```
    pip freeze > requirements.txt
    ```
    7. Загружаем файл и делаем коммит.
    ```
    git add requirements.txt

    git commit -m "add requirements.txt"
    ```
