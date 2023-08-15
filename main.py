import dash
from dash import html
from dash import dcc
import pandas as pd
app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        dcc.Graph(figure=None)
    ]
)
if __name__ == '__main__':
    app.run_server(degub=True)