from dash import Dash
from .callbacks import register_callbacks
from .layout import layout as dash_layout


def create_dashboard(server):
    dash_app = Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
    )

    dash_app.layout = dash_layout
    register_callbacks(dash_app)

    return dash_app.server
