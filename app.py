import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


from dash import Dash,html,dcc
from dash.dependencies import Input,Output

import dash_bootstrap_components as dbc

from datacleaning import cleanedsales_df,cleanedexpense_df,total_customers,merged_df


cols = cleanedsales_df.columns[[0,2,3]]

options = []

for col in cols:
    options.append({'label':'{}'.format(col),'value':col})




app = Dash(__name__,meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])

server = app.server


app.layout = html.Div(children=[

    html.H1('Roast N Sizzle Dashboard',style = {'color': 'white'}),

    dcc.Dropdown(id = 'change_graphs',options=options,
                value='date',
    
                style={'width':'55%'},
                placeholder='select time period...'
                ),

    dcc.Interval(id='interval_comp',interval=10*1000,n_intervals=0),

    dcc.Tabs(children=[
                dcc.Tab(label = 'Metrics',children=[
                    dbc.Row([
                    
                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Sales For Period',style = {'color': 'white'}),
                                        html.H2(id = "salecard",children=[],style={'color':'green'}),
                                        dcc.Graph(id = 'sale_change',figure = {},style={'height':50,'width':100})
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),
                    
                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Expenses For Period',style = {'color': 'white'}),
                                        html.H2(id = "expcard",children=[],style={'color':'red'}),
                                        dcc.Graph(id = 'exp_change',figure = {},style={'height':50,'width':100})
                                        
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),
                    
                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Orders For Period',style = {'color': 'white'}),
                                        html.H2(id = "orders",children=[],style={'color':'grey'}),
                                        dcc.Graph(id = 'orders_change',figure = {},style={'height':50,'width':100})
                                        
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),

                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Burgers Sold For Period',style={'color':'white'}),
                                        html.H2(id = "burgers",children=[],style = {'color':'grey'}),
                                        dcc.Graph(id = 'burger_change',figure = {},style={'height':50,'width':100})
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),
                    ],justify = 'center'),

                    dbc.Row([
                    
                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Reorder Rate Percentage (Monthly)',style = {'color': 'white'}),
                                        html.H2(id = "reorder_card",children=[],style={'color':'green'}),
                                        dcc.Graph(id = 'reorder_change',figure = {},style={'height':50,'width':100})
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),
                    
                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Average Sale Per Order (Monthly)',style = {'color': 'white'}),
                                        html.H2(id = "avg_order_card",children=[],style={'color':'green'}),
                                        dcc.Graph(id = 'avg_order_change',figure = {},style={'height':50,'width':100})
                                        
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),
                    
                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Average Sale Per Customer (Monthly)',style = {'color': 'white'}),
                                        html.H2(id = "avg_cust_card",children=[],style={'color':'grey'}),
                                        dcc.Graph(id = 'avg_cust_change',figure = {},style={'height':50,'width':100})
                                        
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),

                    dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('New Customers Acquired (Monthly)',style={'color':'white'}),
                                        html.H2(id = "new_customers",children=[],style = {'color':'grey'}),
                                        dcc.Graph(id = 'new_customers_change',figure = {},style={'height':50,'width':100})
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),
                    ],justify = 'center'),

                    dbc.Row([

                        dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Total Sales',style = {'color': 'white'}),
                                        html.H2(id = "total_sales",children=[],style={'color':'green'})
                                        
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),

                        dbc.Col(dbc.Card([

                                    dbc.CardBody([
                                        html.H4('Total Expenses',style = {'color': 'white'}),
                                        html.H2(id = "total_exp",children=[],style={'color':'red'})
                                        
                                    ])
                                ],className = 'create_container2 three columns'),width = 4),

                        dbc.Col(dbc.Card([

                                        dbc.CardBody([
                                            html.H4('Total Burgers Sold',style={'color':'white'}),
                                            html.H2(id = "total_burgers",children=[],style = {'color':'grey'})
                                    
                                        ])
                                    ],className = 'create_container2 three columns'),width = 4),

                        dbc.Col(dbc.Card([

                                        dbc.CardBody([
                                            html.H4('Total Customers',style = {'color': 'white'}),
                                            html.H2( total_customers,style={'color':'grey'})
                                        ])

                                            ],className = 'create_container2 three columns'),width = 4)],justify = 'center')
            
            ],className='create_container2'),
                
                
                dcc.Tab(label = 'Graphs',children = [
                    html.Div([
                        html.Div([
                                html.H3('Orders'),
                                dcc.Graph(id = "ordergraph",figure = {})
                                
                            ],className = "create_container2 twelve columns"),
                        
                        html.Div([
                                html.H3('Reorder Rate Percentage'),
                                dcc.Graph( id = "reorder_graph",figure = {})
                                ],className = "create_container2 twelve columns"),

                        html.Div([
                                html.H3('Sales'),
                                dcc.Graph(id = "salesgraph",figure = {})
                                
                            ],className = "create_container2 twelve columns"),

                        html.Div([
                                html.H3('Expenses'),
                                dcc.Graph(id = "expgraph",figure = {})
                                ],className = "create_container2 twelve columns"),

                        html.Div([
                                html.H3('Average Sale Per Order'),
                                dcc.Graph( id = "avg_order_graph",figure = {})
                                ],className = "create_container2 twelve columns"),

                        

                        html.Div([
                                html.H3('Average Sale Per Customer'),
                                dcc.Graph( id = "avg_cust_graph",figure = {})
                                ],className = "create_container2 twelve columns"),

                        html.Div([
                                html.H3('Total Customers'),
                                dcc.Graph( id = "customer_growth",figure = {})
                                ],className = "create_container2 twelve columns"),

                        html.Div([
                                html.H3('Burgers Sold'),
                                dcc.Graph( id = "burgergraph",figure = {})
                                ],className = "create_container2 twelve columns")
                        
                        
                        ])

                    ],className='create_container2')
            ],className='create_container2'),

  

    ])




@app.callback([Output('salecard','children'),
               Output('expcard','children'),
               Output('burgers','children'),
               Output('burgergraph','figure'),
               Output('salesgraph','figure'),
               Output('expgraph','figure'),
               Output('burger_change','figure'),
               Output('sale_change','figure'),
               Output('exp_change','figure'),
               Output('total_sales','children'),
               Output('total_exp','children'),
               Output('total_burgers','children'),
               Output('orders','children'),
               Output('orders_change','figure'),
               Output('ordergraph','figure'),
               Output('reorder_card','children'),
               Output('reorder_change','figure'),
               Output('avg_order_card','children'),
               Output('avg_order_change','figure'),
               Output('avg_cust_card','children'),
               Output('avg_cust_change','figure'),
               Output('new_customers','children'),
               Output('new_customers_change','figure'),
               Output('reorder_graph','figure'),
               Output('avg_order_graph','figure'),
               Output('avg_cust_graph','figure'),
               Output('customer_growth','figure'),],

             [Input('change_graphs','value'),
             Input('interval_comp', 'n_intervals')])

def render_content(period,interval):
    salescopy = cleanedsales_df.copy()
    expensecopy = cleanedexpense_df.copy()
    merged_dfcopy = merged_df.copy()

    buy = salescopy.groupby(period)['Total'].sum()#.reset_index()
    burgers = salescopy.groupby(period)['total burgers'].sum()
    sell = expensecopy.groupby(period)['expense amount'].sum()#.reset_index()
    orders = salescopy.groupby(period)['Total'].count()
    
    buy = pd.DataFrame(buy)
    buy = buy.reset_index()

    burgers = pd.DataFrame(burgers)
    burgers = burgers.reset_index()

    sell = pd.DataFrame(sell)
    sell = sell.reset_index()

    orders = pd.DataFrame(orders)
    orders = orders.reset_index()


    

    
    prevburgertab = burgers['total burgers'].iloc[-2]
    burger_tab = burgers['total burgers'].iloc[-1]

    prevsaletab = buy['Total'].iloc[-2]
    salestab = buy['Total'].iloc[-1]

    prevexp = sell['expense amount'].iloc[-2]
    exp = sell['expense amount'].iloc[-1]

    prevorders = orders['Total'].iloc[-2]
    orderstab = orders['Total'].iloc[-1]

    

    total_sales = buy['Total'].sum()
    total_exp = sell['expense amount'].sum()
    total_burgers = burgers['total burgers'].sum()

    burgerfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = burger_tab,
            delta = {'reference':prevburgertab,'relative':True}
        )
    )
    burgerfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    burgerfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})



    salefig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = salestab,
            delta = {'reference':prevsaletab,'relative':True}
        ))
    salefig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    salefig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})



    expfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = exp,
            delta = {'reference':prevexp,'relative':True}
        )
    )
    expfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    expfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})



    ordersfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = orderstab,
            delta = {'reference':prevorders,'relative':True}
        )
    )
    ordersfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    ordersfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})


    salesgraph = px.bar(buy,x = period,y = 'Total')
    salesgraph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})

    expgraph = px.bar(sell, x = period,y = 'expense amount')
    expgraph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})

    burgergraph = px.bar(burgers, x = period,y = 'total burgers')
    burgergraph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})

    ordergraph = px.bar(orders, x = period,y = 'Total')
    ordergraph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})


    prevreorder_rate = merged_dfcopy['reorder rate'].iloc[-2]
    reorder_rate = merged_dfcopy['reorder rate'].iloc[-1]
    reorderfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = reorder_rate,
            delta = {'reference':prevreorder_rate}
        )
    )
    reorderfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    reorderfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})

    prevavg_order = merged_dfcopy['avgsale_per_order'].iloc[-2]
    avg_order = merged_dfcopy['avgsale_per_order'].iloc[-1]
    avg_orderfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = avg_order,
            delta = {'reference':prevavg_order,'relative':True}
        )
    )
    avg_orderfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    avg_orderfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})

    prevavg_cust = merged_dfcopy['avgsale_per_cust'].iloc[-2]
    avg_cust = merged_dfcopy['avgsale_per_cust'].iloc[-1]
    avgcustfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = avg_cust,
            delta = {'reference':prevavg_cust,'relative':True}
        )
    )
    avgcustfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    avgcustfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})

    prevrecust_growth = merged_dfcopy['new customers'].iloc[-2]
    cust_growth = merged_dfcopy['new customers'].iloc[-1]
    custgrowthfig = go.Figure(
        go.Indicator(
            mode = 'delta',
            value = cust_growth,
            delta = {'reference':prevrecust_growth,'relative':True}
        )
    )
    custgrowthfig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0))
    custgrowthfig.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56'})

    reordergraph = px.bar(merged_dfcopy,x = 'month',y = 'reorder rate')
    reordergraph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})

    avg_order_graph = px.bar(merged_dfcopy,x = 'month',y = 'avgsale_per_order')
    avg_order_graph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})

    avg_cust_graph = px.bar(merged_dfcopy,x = 'month',y = 'avgsale_per_cust')
    avg_cust_graph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})

    cust_growth_graph = px.bar(merged_dfcopy,x = 'month',y = 'cust count')
    cust_growth_graph.update_layout({'plot_bgcolor':'#1f2c56','paper_bgcolor':'#1f2c56','font':{'color':'white'}})    

    return salestab,exp,burger_tab,burgergraph,salesgraph,expgraph,burgerfig,salefig,expfig,total_sales,total_exp,total_burgers,orderstab,ordersfig,ordergraph,reorder_rate,reorderfig,avg_order,avg_orderfig,avg_cust,avgcustfig,cust_growth,custgrowthfig,reordergraph,avg_order_graph,avg_cust_graph,cust_growth_graph



if __name__ == '__main__':
    app.run_server(debug=True)