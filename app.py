from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='GATECH-FIL RECRUITMENT TASK', style={'textAlign':'center'}),
    dcc.Dropdown(['MSFT','GOOGL','AAPL'], 'MSFT', id='ticker'),
    html.H3(children='Assets', style={'textAlign':'center'}),
    dcc.Graph(id='assets'),
    html.H3(children='EPS', style={'textAlign':'center'}),
    dcc.Graph(id='eps'),
    html.H3(children='Liabilities', style={'textAlign':'center'}),
    dcc.Graph(id='liabilities'),
    html.H3(children='Expenses', style={'textAlign':'center'}),
    dcc.Graph(id='expenses')
])

@callback( Output('assets', 'figure'), Input('ticker', 'value'))
def update_assets(ticker):

    df=pd.read_csv(f'{ticker}.csv')

    return px.line(df, x='year', y='assets')

@callback( Output('eps', 'figure'), Input('ticker', 'value'))
def update_eps(ticker):

    df=pd.read_csv(f'{ticker}.csv')

    return px.line(df, x='year', y='eps')

@callback( Output('liabilities', 'figure'), Input('ticker', 'value'))
def update_liabilities(ticker):

    df=pd.read_csv(f'{ticker}.csv')

    return px.line(df, x='year', y='liabilities')

@callback( Output('expenses', 'figure'), Input('ticker', 'value'))
def update_expenses(ticker):

    df=pd.read_csv(f'{ticker}.csv')

    return px.line(df, x='year', y='expenses')



if __name__ == '__main__':
    app.run(debug=True)
