# shop_project

## Учасники команди

- [Renat Belei](https://github.com/username_renat)  
- [Mihail Barilo](https://github.com/username_mihail)

## Опис проекту

Цей проект є інтернет магазином з красивим мінімалістичним дизайном. Тут є функція реєстрації, авторизації, всі дані зберігаються у базі даних. Є функція адміністратора, який може видаляти, змінювати, додавати нові товари. Також є телеграм бот, у якому адміністратор може переглядати всі товари, додавати нові товари, переглядати всіх користувачів.

## Інтерактивна демоверсія

[Перейти до демоверсії](#)

## Корисність проекту

Проект "shop_project" є корисним для багатьох категорій користувачів. Він забезпечує просту і зручну платформу для покупок в інтернеті, дозволяючи користувачам реєструватися, авторизуватися та взаємодіяти з широким асортиментом товарів.

### Для новачків у програмуванні
Цей проект є цінним інструментом для новачків у веб-розробці, оскільки він охоплює всі необхідні аспекти створення повноцінного вебсайту. Під час роботи над проектом, ви дізнаєтеся, як реалізувати функції реєстрації та авторизації, працювати з базами даних, а також створювати адміністраторські панелі для управління контентом сайту.

### Можливості для замовника
Проект має всі необхідні функції для створення повноцінного інтернет-магазину, включаючи:
- Зручний інтерфейс для покупців
- Надійна система зберігання даних
- Функції адміністратора для керування товарами
- Інтеграція з Telegram ботом для зручного керування магазином

Цей проект демонструє можливість створення професійного та функціонального вебсайту, що є корисним як для розробників, так і для кінцевих користувачів.

## Початок роботи

### Вимоги

Для запуску проекту необхідно встановити наступні модулі:

- **Flask**: 
    Цей модуль є базою для всього проекту. Всі веб-сторінки та зв'язок з HTML кодом відбувається через Flask.
- **Flask-Migrate**: 
    Цей підмодуль потрібен для проведення "міграцій" (оновлення) змін у базі даних. Наприклад, якщо ви додали новий стовбчик до моделі (таблиці), він автоматично не додасться до пам'яті бази даних, тому потрібно власноруч оновлювати зміни.
- **Flask-SQLAlchemy**: 
    Цей підмодуль потрібен для зв'язку з базою даних.
- **pandas**: 
    Цей модуль потрібен для зв'язку та обробки даних.
- **telebot**: 
    Цей модуль використовується для створення та контролю телеграм бота, в якому адміністратор може переглядати всіх зареєстрованих користувачів та всі товари, а також додавати товари.

### Інструкція по запуску

#### Локально

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/yourusername/shop_project.git
Перейдіть до директорії проекту:
   ```bash
   cd shop_project
Створіть віртуальне середовище та активуйте його:
   ```bash
    python -m venv venv
source venv/bin/activate
Встановіть залежності:
bash
Копировать код
pip install -r requirements.txt
Запуск веб-сайта
Запустіть проект:
bash
Копировать код
python manage.py
Запуск телеграм бота
Відкрийте термінал у папці bot_app та запустіть бот:
bash
Копировать код
python main.py
Віддалено (на PythonAnywhere)
Увійдіть у свій акаунт на PythonAnywhere.
Перейдіть на вкладку "Web" і створіть новий веб-додаток, вибравши опцію Flask.
Виберіть версію Python, яку ви використовуєте для свого проекту.
Завантажте свій проект на PythonAnywhere. Ви можете використати scp для завантаження файлів, або завантажити файли вручну через веб-інтерфейс.
Відкрийте консоль Bash на PythonAnywhere і перейдіть до директорії вашого проекту:
bash
Копировать код
cd ~/path/to/your/project
Створіть віртуальне середовище та активуйте його:
bash
Копировать код
python -m venv venv
source venv/bin/activate
Встановіть необхідні залежності:
bash
Копировать код
pip install -r requirements.txt
Налаштуйте конфігураційні файли для вашого проекту. Відредагуйте файл wsgi.py, щоб він містив наступний код:
python
Копировать код
import sys
import os

# Вказуємо шлях до проекту
project_home = u'/home/yourusername/path/to/your/project'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Встановлюємо змінну середовища для Flask
os.environ['FLASK_APP'] = 'your_app.py'

# Імпортуємо додаток
from your_app import app as application
Налаштуйте веб-додаток на PythonAnywhere, вказавши шлях до вашого wsgi.py файлу.
Перейдіть на вкладку "Web" і натисніть "Reload" для перезапуску вашого веб-додатку.
Ваш проект тепер має бути доступний за посиланням, наданим PythonAnywhere.
