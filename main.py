import dash
from dash import html
from dash import dcc
import pandas as pd
app.layout = html.Div(
    children=[
        dcc.Graph(figure=None)
    ]
)
app = dash.Dash(__name__)
if __name__ == '__main__':
    app.run_server(degub=True)