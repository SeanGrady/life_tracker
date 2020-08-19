import dash_core_components as dcc
import dash_html_components as html
from .callbacks import metric_checklist_kwargs

layout = html.Div(
    children=[
        html.H1(children='Dashboard'),
        dcc.Checklist(id='metric-checklist', **metric_checklist_kwargs),
        dcc.Graph(id='metric-graph'),
    ],
)
