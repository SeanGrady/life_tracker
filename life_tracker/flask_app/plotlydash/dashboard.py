from dash import Dash
from .callbacks import register_callbacks
from .layout import layout as dash_layout
from flask_login import login_required


def create_dashboard(server):
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
    )

    dash_app.layout = dash_layout
    register_callbacks(dash_app)
    _protect_dash_views(dash_app)

    return dash_app.server


def _protect_dash_views(dash_app):
    for view_func in dash_app.server.view_functions:
        if view_func.startswith(dash_app.config.routes_pathname_prefix):
            dash_app.server.view_functions[view_func] = login_required(dash_app.server.view_functions[view_func])
