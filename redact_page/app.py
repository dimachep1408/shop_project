import flask


redact = flask.Blueprint(
    name = "redact",
    import_name= "app",
    template_folder= "redact_page/templates",
    static_folder= "redact_page"
)