import flask


add = flask.Blueprint(
    name = "add",
    import_name= "app",
    template_folder= "add_page/templates",
    static_folder= "add_page"
)