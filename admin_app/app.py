import flask


admin = flask.Blueprint(
    name = "admin",
    import_name= "app",
    template_folder= "admin_app/templates",
    static_folder= "admin_app"
)