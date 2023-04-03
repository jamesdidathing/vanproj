# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

# Load data - you'll need to change your paths back to wherever these are located
gas = pd.read_csv("gas.csv")
solar = pd.read_csv("solar.csv")
voltages = pd.read_csv("vanvolt.csv")

# ------------- Pandas Bit --------------------
# Create Dataframe
df = pd.DataFrame(gas)
dfs = pd.DataFrame(solar)
dfv = pd.DataFrame(voltages)


# ------------- Plotly Bit --------------------

# Create graphs
backgroundColour = "#F3F0F0"
paperColour = "#E1FA9F"

graph_gas = px.line(df, x=df["Time"], y=df[" Air Quality"])
graph_gas.update_traces(line_color="red")
graph_gas.update_layout(plot_bgcolor=backgroundColour, paper_bgcolor=paperColour)

graph_solar = px.line(dfs, x=dfs["Time"], y=dfs["Voltage"])
graph_solar.update_traces(line_color="orange")
graph_solar.update_layout(plot_bgcolor=backgroundColour, paper_bgcolor=paperColour)

# Leisure and Van voltage on same graph, can change the axis titles but the colours I'm not sure. Haven't looked though
f1 = go.Figure(
    data=[
        go.Scatter(x=dfv["Time"], y=dfv[" Leisure"], name="Leisure"),
        go.Scatter(x=dfv["Time"], y=dfv[" Van"], name="Van"),
    ],
    layout={
        "xaxis": {"title": "x axis"},
        "yaxis": {"title": "y axis"},
        "title": "My title",
    },
)

# ------------- Dash Bit --------------------

# Create dashboard layout
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        # Air Quality Graph:
        html.Div(
            [
                html.H1(
                    children="Air Quality",
                    style={
                        "font-family": "courier",
                        "color": "blue",
                        "text-decoration": "underline",
                        "textAlign": "center",
                    },
                ),
                html.Div(
                    children="Normal is less than 10k",
                    style={
                        "font-family": "courier",
                        "color": "blue",
                        "text-decoration": "underline",
                    },
                ),
                dcc.Graph(id="line-graph", figure=graph_gas),
            ]
        ),
        # Solar Graph:
        html.Div(
            [
                html.H1(
                    children="Solar Panel Voltage",
                    style={
                        "font-family": "courier",
                        "color": "blue",
                        "text-decoration": "underline",
                        "textAlign": "center",
                    },
                ),
                dcc.Graph(id="line-graph2", figure=graph_solar),
            ]
        ),
        # Volatages Graph:
        # 	html.Div([
        # 	html.H1(children='Battery Voltages',
        # 		style={'font-family':'courier','color':'blue','text-decoration': 'underline','textAlign':'center'}),
        # 	dcc.Graph(id='line-graph3', figure=graph_voltages),]),
    ]
)

# Run the dashboard
if __name__ == "__main__":
    app.run_server(host="192.168.0.38", debug=False)
