from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

def get_data():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
    return df, "US -DEMO-"  

def draw_map():
    df, map_name = get_data()
    US_map = go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df['total exports'].astype(float), # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = 'Reds',
            colorbar_title = "Millions USD",
    )    
    layout = go.Layout(
            autosize=True,
            geo = dict(
                scope='usa',
                projection=go.layout.geo.Projection(type = 'albers usa'),
                showlakes=True,
                lakecolor='rgb(255, 255, 255)'
                ),
    )

    fig = go.Figure(data=[US_map], layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)

    return plot_div, map_name
