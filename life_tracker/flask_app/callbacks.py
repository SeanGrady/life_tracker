from flask import current_app as app


@app.teardown_appcontext
def shutdown_session(exception=None):
    app.session.remove()
