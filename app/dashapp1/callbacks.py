from datetime import datetime as dt
import pandas as pd
# import yfinance as yf
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from flask_login import current_user
import pandas_datareader as pdr
import numpy
import talib
import plotly.graph_objects as go
from twelvedata import TDClient
prevIndex = ""
def register_callbacks(dashapp):
    @dashapp.callback(
        Output('my-graph', 'figure'),
        Input('my-dropdown', 'value'),
        Input('my-timeframe', 'value'),
        Input('my-indicator', 'value'),
        Input('checkbox','value'),
        Input('graph-update', 'n_intervals'),        
        State('user-store', 'data'))
    def update_graph1(selected_dropdown_value,timeframe,indicator,rangeslider,n, data):
        global prevIndex
        td = TDClient(apikey="140b16b51ae44d3ab483ffe1bcefbd9d")
        ts = td.time_series(
            symbol=selected_dropdown_value,
            outputsize=100,
            interval=timeframe,
        )
        df = ts.as_pandas()
        print(df)
        # df = pd.read_csv(selected_dropdown_value + ".csv")
        if (df.index[-1] != prevIndex):
            prevIndex = df.index[-1]
            fig_data = []
            fig_data.append(
                go.Scatter(
                    x=df.index,
                    y=eval(indicator)(df.close),
                )
            )        
            fig_data.append(
                go.Candlestick(x=df.index,
                    open=df.open,
                    high=df.high,
                    low=df.low,
                    close=df.close)
            )
            #                rangemode="tozero",
            figure = go.Figure(
            data=fig_data,
            layout=go.Layout(
                xaxis=dict(zeroline=False,rangeslider_visible=True),
                yaxis=dict(
                    title=dict(
                        text=selected_dropdown_value,
                        font=dict(
                            family='"Open Sans", "HelveticaNeue", "Helvetica Neue",'
                            " Helvetica, Arial, sans-serif",
                            size=12,
                        ),
                    ),
                    type="log",
                    rangemode= "tozero",
                    zeroline=False,
                    showticklabels=False,
                ),
                margin=dict(l=40, r=30, b=50, t=50),
                showlegend=False,
                height=294,
                paper_bgcolor="rgb(245, 247, 249)",
                plot_bgcolor="rgb(245, 247, 249)",
            ),
            )
            figure.update_layout(xaxis_rangeslider_visible=False)
            figure.update_layout(
            title='Class 691',
            yaxis_title=selected_dropdown_value +' Stock',
            # shapes = [dict(
            # x0='2020-08-09', x1='2020-08-09', y0=0, y1=1, xref='x', yref='paper',
            # line_width=2)],
            # annotations=[dict(
            # x='2020-08-09', y=0.05, xref='x', yref='paper',
            # showarrow=False, xanchor='left', text='Increase Period Begins')]
            )
            return figure
        else:
            raise dash.exceptions.PreventUpdate()
    # @dashapp.callback(
    #     Output('my-graph1', 'figure'),
    #     Input('my-dropdown', 'value'),
    #     Input('my-timeframe', 'value'),
    #     Input('my-indicator', 'value'),
    #     Input('checkbox','value'),
    #     State('user-store', 'data'))
    # def update_graph2(selected_dropdown_value,timeframe,indicator,rangeslider, data):
    #     td = TDClient(apikey="140b16b51ae44d3ab483ffe1bcefbd9d")
    #     ts = td.time_series(
    #         symbol=selected_dropdown_value,
    #         outputsize=100,
    #         interval=timeframe,
    #     )
    #     df = ts.as_pandas()
    #     fig_data = []
    #     fig_data.append(
    #         go.Bar(
    #             x=df.index,
    #             y=df.volume,orientation='v'
    #         )
    #     )        
    #     figure = go.Figure(
    #     data=fig_data,
    #     layout=go.Layout(
    #         xaxis=dict(zeroline=False),
    #         yaxis=dict(
    #             title=dict(
    #                 text="Volume",
    #                 font=dict(
    #                     family='"Open Sans", "HelveticaNeue", "Helvetica Neue",'
    #                     " Helvetica, Arial, sans-serif",
    #                     size=12,
    #                 ),
    #             ),
    #             type="log",
    #             rangemode="tozero",
    #             zeroline=False,
    #             showticklabels=False,
    #         ),
    #         margin=dict(l=40, r=30, b=50, t=50),
    #         showlegend=False,
    #         height=150,
    #         paper_bgcolor="rgb(245, 247, 249)",
    #         plot_bgcolor="rgb(245, 247, 249)",
    #     ),
    #     )
    #     return figure
    
    @dashapp.callback(
        Output('user-store', 'data'),
        Input('my-dropdown', 'value'),
        State('user-store', 'data'))
    def cur_user(args, data):
        if current_user.is_authenticated:
            return current_user.username

    @dashapp.callback(Output('username', 'children'), Input('user-store', 'data'))
    def username(data):
        if data is None:
            return ''
        else:
            return f'Hello {data}'





