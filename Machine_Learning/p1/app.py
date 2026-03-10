import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pickle
import numpy as np

# Load model
with open("D:\git\depi\DEBI-ONL4_AIS2_S2\Machine_Learning\p1\model.pkl", "rb") as f:
    model = pickle.load(f)

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.H1("🏠 Boston House Price Predictor", 
            style={'textAlign': 'center'}),

    html.Label("Average Number of Rooms (RM)"),
    dcc.Slider(
        id='rm',
        min=3,
        max=9,
        step=0.1,
        value=6,
        marks={i: str(i) for i in range(3,10)}
    ),

    html.Br(),

    html.Label("Lower Status Population % (LSTAT)"),
    dcc.Slider(
        id='lstat',
        min=1,
        max=40,
        step=1,
        value=10,
        marks={i: str(i) for i in range(0,41,5)}
    ),

    html.Br(),

    html.Label("Pupil Teacher Ratio (PTRATIO)"),
    dcc.Slider(
        id='ptratio',
        min=12,
        max=22,
        step=0.5,
        value=18
    ),

    html.Br(),

    html.Div(id='prediction',
             style={
                 'fontSize':30,
                 'textAlign':'center',
                 'marginTop':40
             })

])


@app.callback(
    Output('prediction', 'children'),
    Input('rm', 'value'),
    Input('lstat', 'value'),
    Input('ptratio', 'value')
)

def predict_price(rm, lstat, ptratio):

    features = np.array([[rm, lstat, ptratio]])
    prediction = model.predict(features)[0]

    return f"💰 Predicted House Price: ${prediction*1000:,.0f}"


if __name__ == '__main__':
    app.run(debug=True)