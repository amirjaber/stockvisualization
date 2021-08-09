import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(id='main', children=[
    html.H1(id='username'),html.Div(id='checkbox',children=[
    dcc.Checklist(
    options=[{'label': 'Range slider', 'value': "True"}],
    value="True")]), html.Div(id='both', children=[
    html.Div(id='tickers', children=[html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'EUR/USD', 'value': "EUR/USD"},
            {'label': 'Coke', 'value': "COKE"},
            {'label': 'Tesla', 'value': "TSLA"},
            {'label': 'Apple', 'value': "AAPL"},
            {'label': 'Amzon', 'value': "AMZN"}
        ],
        value='EUR/USD'
    )], style=dict(width='20%')),
    html.Div(id='timeframe', children=[html.H1('TimeFrame'),dcc.Dropdown(
        id='my-timeframe',
        options=[
            {'label': '1week', 'value': "1week"},
            {'label': '1day', 'value': "1day"},
            {'label': '4hr', 'value': "4h"},
            {'label': '1hr', 'value': "1h"},
            {'label': '1m', 'value': "1min"}
        ],
        value='1min'
    )], style=dict(width='20%')),
    html.Div(id='indicator', children=[html.H1('Indicators'),dcc.Dropdown(
        id='my-indicator',
        options=[
            {'label': 'EMA', 'value': 'talib.EMA'},
            {'label': 'MACD', 'value': 'talib.MACD'},
            {'label': 'RSI', 'value': 'talib.RSI'}
        ],
        value='talib.EMA'
    )], style=dict(width='20%'))],style={"display":"flex", "justify-content":"space-around","margin": "auto"}),
    dcc.Graph(id='my-graph',animate=True),
    # dcc.Graph(id='my-graph1',animate=True),
    dcc.Interval(id='graph-update',interval=60000,n_intervals = 0),
    dcc.Store(id='user-store'),
], style=dict(width=1000))
