import flask


login2 = flask.Blueprint(
    name = "login2",
    import_name= "app",
    template_folder= "login_page2/templates",
    static_folder= "login_page2"
)