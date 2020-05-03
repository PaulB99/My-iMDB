
"""
Created on Sun May  3 01:00:15 2020

@author: paulb
"""

#A data visualisation of my top 100 films on imdb as of 03/05/20

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#Import data
data = pd.read_csv("ratings.csv", encoding= 'ansi')

#Drop tv episodes
indexNames = data[ data['Title Type'] == 'tvEpisode' ].index
data.drop(indexNames , inplace=True)

#Drop tv shows
indexNames = data[ data['Title Type'] == 'tvSeries' ].index
data.drop(indexNames , inplace=True)

#Drop miniseries
indexNames = data[ data['Title Type'] == 'tvMiniSeries' ].index
data.drop(indexNames , inplace=True)

#Drop video games
indexNames = data[ data['Title Type'] == 'videoGame' ].index
data.drop(indexNames , inplace=True)

#Sort by score
data.sort_values(by='Your Rating', ascending=False ,inplace = True)

#Get top 100
data100 = data.head(100)

print(data100.head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='My top 100',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A breakdown of my top 100 films on imdb as of 03/05/20', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=data100[data100['Genres'] == i]['IMDb Rating'],
                    y=data100[data100['Genres'] == i]['Runtime (mins)'],
                    text=data100[data100['Genres'] == i]['Title'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in data100.Genres.unique()
            ],
            'layout': dict(
                xaxis={'title': 'IMDb Rating'},
                yaxis={'title': 'Runtime'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)