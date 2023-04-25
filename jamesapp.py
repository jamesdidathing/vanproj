# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

app = Dash(external_stylesheets=[dbc.themes.LUX])
load_figure_template('SLATE')

# Load data
gas = pd.read_csv('gas.csv')
solar = pd.read_csv('solar.csv')
voltages = pd.read_csv('vanvolt.csv')
pressure = pd.read_csv('vanpress1.csv')
airq = pd.read_csv('AirQ.csv')
temphumid = pd.read_csv('vandata.csv')

#------------- Pandas Bit --------------------
#Create Dataframe
df = pd.DataFrame(gas)
dfs = pd.DataFrame(solar)
dfv = pd.DataFrame(voltages)
dfp = pd.DataFrame(pressure)
dfq = pd.DataFrame(airq)
dfth = pd.DataFrame(temphumid)

latestVanVoltage = (dfv[' Van'].values[-1:])
latestLeisureVoltage = (dfv[' Leisure'].values[-1:])

#------------- Plotly Bit --------------------
# Create graphs
backgroundColour='#111111'
text='#7FDBFF'


airq_fig = px.scatter(df, x="Time", y=" Air Quality", hover_data=" Air Quality", title='Air Quality')
airq_fig.update_layout(
    plot_bgcolor=backgroundColour,
    paper_bgcolor=backgroundColour,
    font_color=text,
)

solar_fig = px.scatter(dfs, x="Time", y="Voltage", hover_data="Voltage", title='Solar Voltage')
solar_fig.update_layout(
    plot_bgcolor=backgroundColour,
    paper_bgcolor=backgroundColour,
    font_color=text,
)

app.layout = html.Div(style={'backgroundColor': backgroundColour}, children=[
    html.H1("VanProj Graphs", style={'textAlign': 'center', 'color': text
    }),

    dcc.Graph(
        id='air-quality',
        figure=airq_fig,
        ),

        dcc.Graph(
        id='solar-voltage',
        figure=solar_fig,
        ),

        
])



if __name__ == '__main__':
    app.run_server(debug=True)