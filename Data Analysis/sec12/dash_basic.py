from dash import Dash, dcc, html
from dash.dependencies import Input, Output


app = Dash(__name__)

app.layout = html.Div([
    html.Button("Submit", id="number"),
    dcc.Input(placeholder = "Enter a valid number",
              id="Data", type="number", value=''),
    html.H1(id="Result")])

@app.callback(
    Output("Result", "children"),
    Input("number", "n_clicks"))

def plat_data(n, data):
    if n:
        return f"You have entered: {data}"
    return "Click the button to submit your data."

app.run(debug=True)