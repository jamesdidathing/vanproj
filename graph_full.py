# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html

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

print(dfv.tail(1))
print(dfv[' Van'].values[-1:])
print(dfv[' Leisure'].values[-1:])

latestVanVoltage = (dfv[' Van'].values[-1:])
latestLeisureVoltage = (dfv[' Leisure'].values[-1:])
print (latestVanVoltage)
print (latestLeisureVoltage)

#------------- Plotly Bit --------------------
# Create graphs
backgroundColour='#F3F0F0'
paperColour='#E1FA9F'

graph_gas = go.Figure(
data=[
        go.Scatter(x=df["Time"], y=df[" Air Quality"], name=" Air Quality", line_color='red'),
        ],
    layout={
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Air Quality (Raw Data)"},
		"plot_bgcolor":backgroundColour,
        "paper_bgcolor":paperColour,
    },
)
graph_solar = go.Figure(
data=[
        go.Scatter(x=dfs["Time"], y=dfs["Voltage"], name="Voltage", line_color='orange'),
        ],
    layout={
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Voltage"},
		"plot_bgcolor":backgroundColour,
        "paper_bgcolor":paperColour,
    },
)
graph_pressure = go.Figure(
data=[
        go.Scatter(x=dfp["Time"], y=dfp[" Pressure MBar"], name="Air Pressure", line_color='blue'),
        ],
    layout={
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Air Pressure MBar"},
		"plot_bgcolor":backgroundColour,
        "paper_bgcolor":paperColour,
    },
)
graph_airq = go.Figure(
data=[
        go.Scatter(x=dfq["Time"], y=dfq["Air Quality"], name="Air Quality", line_color='green'),
        ],
    layout={
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Air Quality - Adjusted for Temp"},
		"plot_bgcolor":backgroundColour,
        "paper_bgcolor":paperColour,
    },
)
# +++++++++++++  Multi Y-Series Graphs +++++++++++++++
batteries = go.Figure(
    data=[
        go.Scatter(x=dfv["Time"], y=dfv[" Leisure"], name="Leisure"),
        go.Scatter(x=dfv["Time"], y=dfv[" Van"], name="Van"),
    ],
    layout={
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Voltage"},
		"plot_bgcolor":backgroundColour,
        "paper_bgcolor":paperColour,
    },
)
conditions = go.Figure(
    data=[
        go.Scatter(x=dfth["Time"], y=dfth[" Humidity %"], name=" Humidity %"),
        go.Scatter(x=dfth["Time"], y=dfth[" Temp C"], name=" Temp C"),
    ],
    layout={
        "xaxis": {"title": "Time"},
        "yaxis": {"title": "Temperature / Humidity"},
		"plot_bgcolor":backgroundColour,
        "paper_bgcolor":paperColour,
    },
)
#------------- Dash Bit --------------------
# Create dashboard layout
app = dash.Dash(__name__)
app.layout = html.Div(className='row',children =[

#----------------------------------DASHBOARD:---------------------------------
    html.Div([
	html.H1(children='Van Conditions',
		style={'font-family':'courier','color':'blue','text-decoration': 'underline','textAlign':'center',}),

# Variable Diplay Section - NEEDS SORTING OUT
    html.Label("Current Van Battery Voltage:", style={'display':'inline-block'}),
    html.H3(latestVanVoltage),
    html.H2("Current Leisure Battery Voltage:"),
    html.H3(latestLeisureVoltage),
#----------------------------------------------
#Temp & Humidity Graph    
    dcc.Graph(id='line-graph1', figure=conditions, style={'display':'inline-block'}),
#Voltages Graph:
	dcc.Graph(id='line-graph2', figure=batteries, style={'display':'inline-block'}),]),
#----------------------------------------------
#Solar Graph:
	html.Div([
	dcc.Graph(id='line-graph3', figure=graph_solar, style={'display':'inline-block'}),
#Air Pressure Graph
	dcc.Graph(id='line-graph4', figure=graph_pressure, style={'display':'inline-block'}),]),
#------------------------------------------------
#Gas Sensor Graph:
	html.Div([
	dcc.Graph(id='line-graph5', figure=graph_gas, style={'display':'inline-block'}),
#Air Quality Graph
	dcc.Graph(id='line-graph6', figure=graph_airq, style={'display':'inline-block'}),]),
])
#===================================================

# Run the dashboard

# CHANGE IP BELOW TO 127.0.0.1 TO ACCESS ON THE LOCAL PC.
# POINT YOUR BROWSER TO HTTP://127.0.0.1:8050 AND THE WEB PAGE SHOULD BE DISPLAYED.


if __name__ == '__main__':
    app.run_server(host= '127.0.0.1',debug=False)

