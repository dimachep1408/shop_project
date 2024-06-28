import flask  # Імпорт бібліотеки Flask / Import the Flask library

# Створення нового Blueprint під назвою 'add'
# Create a new Blueprint named 'add'
add = flask.Blueprint(
    name="add",  # Ім'я Blueprint / Name of the Blueprint
    import_name="app",  # Імпортне ім'я додатка / Import name of the app
    template_folder="add_page/templates",  # Папка з шаблонами для Blueprint / Template folder for the Blueprint
    static_folder="add_page"  # Папка зі статичними файлами для Blueprint / Static folder for the Blueprint
)