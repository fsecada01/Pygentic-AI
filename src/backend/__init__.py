from fastapi import FastAPI


def create_app(debug: bool = False, settings_obj=None):
    """

    :param debug:
    :param settings_obj:
    :return:
    """
    app = FastAPI(
        title="API Service for 525 Ocean Parkway's Cooperative Board",
        debug=debug,
    )
    if settings_obj:
        app.settings = settings_obj

    return app
