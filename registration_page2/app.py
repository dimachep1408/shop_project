import flask


registration2 = flask.Blueprint(
    name = "registration2",
    import_name= "app",
    template_folder= "registration_page2/templates",
    static_folder= "registration_page2"
)