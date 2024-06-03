import flask


main2 = flask.Blueprint(
    name = "main2",
    import_name= "app",
    template_folder= "main_page2/templates",
    static_folder= "main_page2"
)