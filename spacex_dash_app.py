"""IBM SpaceX launch dashboard — Plotly Dash lab tasks 1–4.

Requires spacex_launch_dash.csv in the same directory.
Install dependencies: python -m pip install pandas dash plotly
Run: python spacex_dash_app.py
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_PATH = Path(__file__).with_name('spacex_launch_dash.csv')
spacex_df = pd.read_csv(DATA_PATH)
min_payload, max_payload = 0, 10000
app = Dash(__name__)

app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] + [
            {'label': site, 'value': site}
            for site in spacex_df['Launch Site'].dropna().unique()
        ],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True,
    ),
    html.Br(),
    dcc.Graph(id='success-pie-chart'),
    html.P('Payload range (Kg):'),
    dcc.RangeSlider(
        id='payload-slider', min=0, max=10000, step=1000,
        marks={i: str(i) for i in range(0, 10001, 2500)},
        value=[min_payload, max_payload],
    ),
    html.Br(),
    dcc.Graph(id='success-payload-scatter-chart'),
])

@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value'),
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        successful = spacex_df[spacex_df['class'] == 1]
        return px.pie(successful, names='Launch Site', title='Total Success Launches by Site')

    site_data = spacex_df[spacex_df['Launch Site'] == entered_site]
    counts = site_data['class'].value_counts().reindex([0, 1], fill_value=0).reset_index()
    counts.columns = ['class', 'count']
    counts['outcome'] = counts['class'].map({0: 'Failure', 1: 'Success'})
    return px.pie(counts, values='count', names='outcome',
                  title=f'Launch Outcomes for {entered_site}')

@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('payload-slider', 'value'),
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low)
        & (spacex_df['Payload Mass (kg)'] <= high)
    ]
    if entered_site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == entered_site]
    return px.scatter(
        filtered, x='Payload Mass (kg)', y='class',
        color='Booster Version Category',
        title='Correlation between Payload and Success',
    )

if __name__ == '__main__':
    app.run(debug=True)
