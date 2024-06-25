import flask


order = flask.Blueprint(
    name = "order",
    import_name= "app",
    template_folder= "order_page/templates",
    static_folder= "order_page"
)