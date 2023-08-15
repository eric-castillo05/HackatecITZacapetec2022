import dash
from dash import html
from dash import dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv('data/Exceso_Mortalidad_MX_2022_Historico_Aleatorios.csv')

x = data[['ENTIDAD_REG', 'MUNICIPIO_REG', 'SEXO', 'POSIBLE-COVID19']]
y = data['EDAD']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.3, test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)

# Select a random sample of 30 rows from the test data and predictions
sample = x_test.sample(30)
sample_predictions = predictions[sample.index]

# Create a 3D scatter plot of the actual vs predicted values for the sample
fig = go.Figure(data=[
    go.Scatter3d(
        x=sample['ENTIDAD_REG'],
        y=sample['MUNICIPIO_REG'],
        z=sample_predictions,
        mode='markers')])

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Graph(figure=fig)
    ]
)
if __name__ == '__main__':
    app.run_server(debug=True)