# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
df = pd.read_csv('static/Pokemon.csv')
# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='L2 Exercise 2'),

    # set the description underneath the heading
    html.Div(children='''
        This scatter plot was created to see whether Pokemon's attack points 
        effected the amount of defense points they could gain and vice versa. My hypothesis is
        that the creators of Pokemon will try to balance these stats out, so that if one were to 
        increase, the other will decrease. After observing this data, it seems that there is only a slight
        positive correlation between the two, meaning that Pokemon with higher attack points also have higher 
        defense points, but again this correlation is not very strong. 
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=df['Attack'],
                    y=df['Defense'],
                    mode='markers',
                    text=df['Name'],# This line sets the vehicle name as the points' labels.
                    marker={
                        'size': 8,
                        'opacity': .6,  # By making the points a bit transparent, it can alleviate the occlusion issue
                        'color': 'green'
                    }
                )
            ],
            'layout': {
                'title': 'Pokemon Attack Points vs. Defense Points',
                # It is always a good practice to have axis labels.
                # This is especially important in this case as the numbers are not trivial
                'xaxis': {'title': 'Attack Points'},
                'yaxis': {'title': 'Defense Points'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)