import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
import os
import plotly.graph_objs as go
import dash_dangerously_set_inner_html

#pip install dash-dangerously-set-inner-html


df = pd.read_csv('userAndEdge_trends_30days.csv')
edgesTrend = pd.read_csv('edgesTrend.csv')
communitiesNumberTrend = pd.read_csv('communitiesNumberTrend.csv')
communitiesDissolvedTrend = pd.read_csv('communitiesDissolvedTrend.csv')
communitiesCreationTrend = pd.read_csv('communitiesCreationTrend.csv')

averageDegreeAttack=pd.read_csv('AverageDegree/AttackGraphData.csv')
averageDegreeMessage=pd.read_csv('AverageDegree/MessageGraphData.csv')
averageDegreeTrade=pd.read_csv('AverageDegree/TradeGraphData.csv')

inDegreeDistribution=pd.read_csv('InDegreeDistribution/GraphData.csv')

AverageShortestPathAttack=pd.read_csv('AverageShortestPath/AttackGraphData.csv')
AverageShortestPathMessage=pd.read_csv('AverageShortestPath/MessageGraphData.csv')
AverageShortestPathTrade=pd.read_csv('AverageShortestPath/TradeGraphData.csv')

DensityM_NS=pd.read_csv('Density/DE_densityN_MData.csv')
DensityT_NS=pd.read_csv('Density/DE_densityN_TData.csv')

DensityM_S=pd.read_csv('Density/DE_densityS_MData.csv')
DensityT_S=pd.read_csv('Density/DE_densityS_TData.csv')

DiameterValueA=pd.read_csv('DiameterValue/AttackGraphData.csv')
DiameterValueM=pd.read_csv('DiameterValue/MessageGraphData.csv')
DiameterValueT=pd.read_csv('DiameterValue/TradeGraphData.csv')

ReciprocityM_S=pd.read_csv('Reciprocity/RE_reciprocityS_MData.csv')
ReciprocityT_S=pd.read_csv('Reciprocity/RE_reciprocityS_TData.csv')

ReciprocityM_NS=pd.read_csv('Reciprocity/RE_reciprocityN_MData.csv')
ReciprocityT_NS=pd.read_csv('Reciprocity/RE_reciprocityN_TData.csv')

Diplomatics = pd.read_csv('SingleCommunityStudy/DiplomatsVsNoDiplomats/data.csv')

Trickster = pd.read_csv('TricksterDetection/tricksterActivityDay.csv', sep=';')
TricksterData = pd.read_csv('TricksterDetection/tricksterData.csv', sep=';')

InTotalDegreeD_T =  pd.read_csv('InDegreeDistribution/TotalTradeData.csv')

#Coefficiente di clustering
CCoeffM_S = pd.read_csv('ClusteringCoefficient/CC_clusteringS_MCoefficientData.csv')
CCoeffT_S = pd.read_csv('ClusteringCoefficient/CC_clusteringS_TCoefficientData.csv')
CCoeffM_NS = pd.read_csv('ClusteringCoefficient/CC_clusteringN_MCoefficientData.csv')
CCoeffT_NS = pd.read_csv('ClusteringCoefficient/CC_clusteringN_TCoefficientData.csv')

#Numero di archi
ADM_S = pd.read_csv('EdgesInAllianceGraph/SameMessage_NEdges.csv')
ADT_S = pd.read_csv('EdgesInAllianceGraph/SameTrade_NEdges.csv')
ADM_NS = pd.read_csv('EdgesInAllianceGraph/NoSameMessage_NEdges.csv')
ADT_NS = pd.read_csv('EdgesInAllianceGraph/NoSameTrade_NEdges.csv')


#diametro
DM_S = pd.read_csv('AllianceGraph/D_diameterS_MData.csv')
DT_S = pd.read_csv('AllianceGraph/D_diameterS_TData.csv')
DM_NS = pd.read_csv('AllianceGraph/D_diameterN_MData.csv')
DT_NS = pd.read_csv('AllianceGraph/D_diameterN_TData.csv')

#Shortest Path
SPM_S = pd.read_csv('AllianceGraph/AP_averageS_MPathLengthData.csv', sep=';')
SPT_S = pd.read_csv('AllianceGraph/AP_averageS_TPathLengthData.csv', sep=';')
SPM_NS = pd.read_csv('AllianceGraph/AP_averageN_MPathLengthData.csv', sep=';')
SPT_NS = pd.read_csv('AllianceGraph/AP_averageN_TPathLengthData.csv', sep=';')

#averageDegree
ADegreeM_S = pd.read_csv('AllianceGraph/averageS_MDegree.csv')
ADegreeT_S = pd.read_csv('AllianceGraph/averageS_TDegree.csv')
ADegreeM_NS = pd.read_csv('AllianceGraph/averageN_MDegree.csv')
ADegreeT_NS = pd.read_csv('AllianceGraph/averageN_TDegree.csv')




available_indicators = Trickster['Suspect'].unique()
available_trickster = TricksterData['Suspect'].unique()



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

      dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
       <center><img src='https://i.ibb.co/2tVxf15/image.png' alt="slide 1" width="300"> </center>
        <center>See our <a href="https://github.com/Villone96/Data-Analytics-Project">GitHub Repo</a></center>

    '''),



    dcc.Tabs(id="tabs", children=[

        dcc.Tab(label='Introduzione', children=[

            dcc.Tabs(id="introtabs", children=[
            dcc.Tab(label='Titolo', children=[

                dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                <center><img src="https://i.ibb.co/SxVDtzH/image.png" alt="slide 1" width="1100"> </center>
                '''),
           
         
            ]),

            dcc.Tab(label='Giochi MMOG', children=[
                    
            dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/cJBWLch/image.png" alt="slide 1" width="1100"> </center>
            '''),

            ]),

            dcc.Tab(label='Il dataset', children=[
                    
            ]),
            dcc.Tab(label='Pre-Processing', children=[
                    
            ]),

            dcc.Tab(label='Obiettivi di Analisi', children=[

                dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
            <h4>Le nostre analisi preventivate di analisi</h4>
            <ul>
            <li>Analisi numerosità  e numero medio di player.</li>
            <li>Analisi numerosità  e numero medio per ogni tipologia di arco. </li>
            <li>Cercare i nodi con outdegree (di qualsiasi tipo) uguale a 0 e indegree > 0 per gli attacchi (valutare anche altri possibili indegree); questo per identificare i villaggi abbandonati.</li>
            <li>Cercare i nodi con indegree (di qualsiasi tipo) uguale a 0 e outdegree > 0 per i trades (valutare che siano un unico outdegree); in questo modo si identificano quei villaggi che vengono utilizzati dallo stesso player (con nomi diversi) per rifornire il villaggio principale (valutare quindi che tutti gli archi siano in direzione di un solo player).</li>
            <li>Analisi delle community più grosse (top 3) nell'arco dei 30 giorni e determinare le cause.</li>
            <li>Ricerca della community che cresce (e decresce) di più (e di meno) nei 30 giorni. (Forse meglio valutare numerosità  nell'arco dei 30 giorni date tutte le community > 1)</li>
            <li>Valutare la edge betweenness date le community per ogni tipologia (attacco, commercio, messaggi); per i messaggi andiamo a identificare i capi diplomatici per ogni community.</li>
            <li>Valutare date le community più grosse la presenza di guerre (grande commercio e grande scambio di messaggi).</li>
            <li>Valutare l'evoluzione delle community in assenza di elementi centrali.</li>
            <li>Ricerca di nodi pozzo/sorgente per ogni tipo di relazioni e fare ipotesi sul perchè e per come.</li>
            <li>Fare confronto tra le diverse metodologie di community detection e valutare quale da risultati piÃÂ¹ simili a quelle fornite.</li>
            <li>Modifiche delle community in seguito agli attacchi.</li>
            <li></li>
            </ul>
        '''),
                    
            ]),

            ]),
            ]),

         dcc.Tab(label='La rete', children=[

            dcc.Tabs(id="retetab", children=[
                dcc.Tab(label='Trend Nodi e Archi', children=[
                
                dcc.Graph(
                id='life-exp-vs-gdp',
                figure={
                    'data': [
                        go.Scatter(
                            x=df[df['type'] == i]['day'],
                            y=df[df['type'] == i]['quantity'],
                            text=df[df['type'] == i]['type'],
                            mode='markers+lines',
                            opacity=0.7,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name=i
                        ) for i in df.type.unique()
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'Giorni'},
                        yaxis={'title': 'Quantità', 'type':'log'},
                        #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        #legend={'x': 0, 'y': 1},+
                        #hovermode='closest'
                    )
                }
            ),

            #GRafico a torta

            dcc.Graph(id="my-graph"),

            dcc.Slider(
                id='day-selected',
                min=1,
                max=30,
                step=1,
                value=15,
                marks={
                    1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
                    11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21',
                    22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30'
            },
            ),
            html.Div(id='slider-output-container'),

            dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <br><br><br><br><br><br>
            '''),

         
            ]),

             dcc.Tab(label='Communities Trend', children=[

                 dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/C2LjcmY/image.png" alt="slide 1" width="1400"> </center>
            '''),

                      dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = communitiesNumberTrend.day,
                                    y = communitiesNumberTrend.quantity,
                                    mode = 'markers+lines',
                                    name = 'Numero di Comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = communitiesDissolvedTrend.day,
                                    y = communitiesDissolvedTrend.quantity,
                                    mode = 'lines+markers',
                                    name = 'Comunità dissolte'
                                ),
                                go.Scatter(
                                    x = communitiesCreationTrend.day,
                                    y = communitiesCreationTrend.quantity,
                                    mode = 'lines+markers',
                                    name = 'Comunità Create'
                                ),

                            ],
                            layout=go.Layout(
                                title='Communities Trends',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='commtrend'
                    ),
                    dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': communitiesNumberTrend.day, 'y': communitiesNumberTrend.quantity, 'type': 'bar', 'name': 'communities Number'},
                            {'x': communitiesDissolvedTrend.day, 'y': communitiesDissolvedTrend.quantity, 'type': 'bar', 'name': 'communities Dissolved'},
                            {'x': communitiesCreationTrend.day, 'y': communitiesCreationTrend.quantity, 'type': 'bar', 'name': 'communities Creation'},

                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Giorni'},
                            yaxis={'title': 'Quantità'},
                            #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                            #legend={'x': 0, 'y': 1},
                            #hovermode='closest'
                        )
                    }
                ),
        ]),
            dcc.Tab(label='Average Degree', children=[
                dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/hRyyDsL/image.png" alt="slide 1" width="1150"> </center>
            '''),

                dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = averageDegreeAttack.Day,
                                    y = averageDegreeAttack.AverageDegree,
                                    mode = 'markers+lines',
                                    name = 'Grado medio Attacchi',
                                    
                          
                                ),
                                go.Scatter(
                                    x = averageDegreeMessage.Day,
                                    y = averageDegreeMessage.AverageDegree,
                                    mode = 'lines+markers',
                                    name = 'Grado medio Messaggi'
                                ),
                                go.Scatter(
                                    x = averageDegreeTrade.Day,
                                    y = averageDegreeTrade.AverageDegree,
                                    mode = 'lines+markers',
                                    name = 'Grado medio Trade'
                                ),

                            ],
                            layout=go.Layout(
                                title='Grado medio per tipo di arco',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageDedree'
                    ),
                
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': averageDegreeAttack.Day, 'y': averageDegreeAttack.AverageDegree,
                                'type': 'bar', 'name': 'Attack'},
                             {'x': averageDegreeMessage.Day, 'y': averageDegreeMessage.AverageDegree,
                                'type': 'bar', 'name': 'Message'},
                                 {'x': averageDegreeTrade.Day, 'y': averageDegreeTrade.AverageDegree,
                                'type': 'bar', 'name': 'Trade'},
                        ]
                    }
                )
        ]),
              dcc.Tab(label='In/Out Degree Distribution', children=[


                  dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = InTotalDegreeD_T.Range,
                                    y = InTotalDegreeD_T.Value,
                                    mode = 'markers',
                                    name = 'In Degree medio Trade',
                                    
                          
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='In Degree medio Trade',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageInDegreeT'
                    ),

                  

                dcc.Graph(id="DegreeDistributionGraph"),
                dcc.Slider(
                    id='day-selected2',
                    min=1,
                    max=30,
                    step=1,
                    value=15,
                    marks={
                        1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
                        11: '11', 12: '12', 13: '13', 14: '14', 15: '15', 16: '16', 17: '17', 18: '18', 19: '19', 20: '20', 21: '21',
                        22: '22', 23: '23', 24: '24', 25: '25', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30'
                },
                ),
                html.Div(id='SelectionDegreeDistributionGraph'),

                ]),
             dcc.Tab(label='Average Shortest Path', children=[
                 dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
         <center><img src="https://i.ibb.co/2YLLRzL/image.png" alt="slide 1" width="1100"> </center>
            '''),

                dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = AverageShortestPathAttack.Day,
                                    y = AverageShortestPathAttack.AverageShortestPath,
                                    mode = 'markers+lines',
                                    name = 'SP medio Attacchi',
                                    
                          
                                ),
                                go.Scatter(
                                    x = AverageShortestPathMessage.Day,
                                    y = AverageShortestPathMessage.AverageShortestPath,
                                    mode = 'lines+markers',
                                    name = 'SP medio Messaggi'
                                ),
                                go.Scatter(
                                    x = AverageShortestPathTrade.Day,
                                    y = AverageShortestPathTrade.AverageShortestPath,
                                    mode = 'lines+markers',
                                    name = 'SP medio Trade'
                                ),

                            ],
                            layout=go.Layout(
                                title='Shortest Path medio per tipo di arco',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageSHP'
                    ),
                 
                dcc.Graph(
                    id='AverageShortestPath',
                    figure={
                        'data': [
                            {'x': AverageShortestPathAttack.Day, 'y': AverageShortestPathAttack.AverageShortestPath,
                                'type': 'bar', 'name': 'Attack'},
                             {'x': AverageShortestPathMessage.Day, 'y': AverageShortestPathMessage.AverageShortestPath,
                                'type': 'bar', 'name': 'Message'},
                                 {'x': AverageShortestPathTrade.Day, 'y': AverageShortestPathTrade.AverageShortestPath,
                                'type': 'bar', 'name': 'Trade'},
                                
                        ],
                    }
                )
        ]),

        dcc.Tab(label='Diameter Value', children=[
                 dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = DiameterValueA.Day,
                                    y = DiameterValueA.Diameter,
                                    mode = 'markers+lines',
                                    name = 'Diametro medio Attacchi',
                                    
                          
                                ),
                                go.Scatter(
                                    x = DiameterValueM.Day,
                                    y = DiameterValueM.Diameter,
                                    mode = 'lines+markers',
                                    name = 'Diametro medio Messaggi'
                                ),
                                go.Scatter(
                                    x = DiameterValueT.Day,
                                    y = DiameterValueT.Diameter,
                                    mode = 'lines+markers',
                                    name = 'Diametro medio Trade'
                                ),

                            ],
                            layout=go.Layout(
                                title='Diametro medio per tipo di arco',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='averageDiameter'
                    ),
                dcc.Graph(
                    id='DenDiameterValues',
                    figure={
                        'data': [
                            {'x': DiameterValueA.Day, 'y': DiameterValueA.Diameter,
                                'type': 'bar', 'name': 'Attack'},
                             {'x': DiameterValueM.Day, 'y': DiameterValueM.Diameter,
                                'type': 'bar', 'name': 'Message'},
                                 {'x': DiameterValueT.Day, 'y': DiameterValueT.Diameter,
                                'type': 'bar', 'name': 'Trade'},
                        ]
                    }
                )
            ]),
            ]),
            ]),
            
            dcc.Tab(label='Trickster Detection', children=[
                
                dcc.Tabs(id="Trickster tabs", children=[
                    dcc.Tab(label='Introduzione', children=[
         
                    ]),

                    dcc.Tab(label='Logica di funzionamento', children=[
         
                    ]),

                    dcc.Tab(label='Risultati', children=[

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/LhS6nrJ/image.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                    

                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<br><h4>Seleziona il cheater:</h4>'''), 
                    html.Div([                      #menu per selezionare il cheater
                        dcc.Dropdown(
                            id='xaxis-column',
                            options=[{'label': i, 'value': i} for i in available_indicators],
                            value=7855
                        ),
                        
                    ]
                    #style={'width': '15%', 'float': 'right', 'display': 'inline-block'}
                    ),
                    dcc.Graph(id='cheat-graphic'), #grafico

                    #Secondo plot -----------------------------------------------------------------------------
                    dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''<br><h4>Seleziona il cheater:</h4>'''), 
                    html.Div([                      #menu per selezionare il cheater
                        dcc.Dropdown(
                            id='suspect-column',
                            options=[{'label': i, 'value': i} for i in available_trickster],
                            value=7855
                        ),
                        
                    ]
                    #style={'width': '15%', 'float': 'right', 'display': 'inline-block'}
                    ),
                    dcc.Graph(id='cheat-data'), #grafico

                    ]),
         
                ]),
            ]),

            dcc.Tab(label='Commercio e Messaggi', children=[
                dcc.Tabs(id="commerciotradetabs", children=[

                    dcc.Tab(label='Reciprocità', children=[

                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/dLtsgg9/image.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = ReciprocityM_S.day,
                                    y = ReciprocityM_S.Reciprocity,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = ReciprocityM_NS.day,
                                    y = ReciprocityM_NS.Reciprocity,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto Reciprocità Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messagereciprocity'
                    ),
                

                        dcc.Graph(
                            id='ReciprocyNotSame',
                            figure={
                                'data': [
                                    {'x': ReciprocityM_S.day, 'y': ReciprocityM_S.Reciprocity,
                                        'type': 'bar', 'name': 'Messaggi Comnunità Uguale'},
                                    {'x': ReciprocityM_NS.day, 'y': ReciprocityM_NS.Reciprocity,
                                        'type': 'bar', 'name': 'Messaggi Comnuità Diverse'},],
                                'layout': {
                            'title': 'Confronto Reciprocità Messaggi dentro e fuori la Comunità'
                                }
                            }
                        ),
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/T85KKNL/image.png
                    " alt="slide 1" width="1100"> </center>
                    '''),

                     dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = ReciprocityT_S.day,
                                    y = ReciprocityT_S.Reciprocity,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = ReciprocityT_NS.day,
                                    y = ReciprocityT_NS.Reciprocity,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto Reciprocità Trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='Tradesreciprocity'
                    ),
                        
                        dcc.Graph(
                            id='ReciprocySame',
                            figure={
                                'data': [
                                    {'x': ReciprocityT_S.day, 'y': ReciprocityT_S.Reciprocity,
                                        'type': 'bar', 'name': 'Trade Comnunità Uguale'},
                                    {'x': ReciprocityT_NS.day, 'y': ReciprocityT_NS.Reciprocity,
                                        'type': 'bar', 'name': 'Trade Comnuità Diverse'},],
                                'layout': {
                            'title': 'Confronto Reciprocità Trade dentro e fuori la Comunità'
                                }
                            }
                        ),
                        ]),

                    dcc.Tab(label='Densità', children=[
                        dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
                    <center><img src="https://i.ibb.co/H2zSw5q/image.png
                    " alt="slide 1" width="1100"> </center>
                    '''),
                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = DensityM_S.day,
                                    y = DensityM_S.density,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = DensityM_NS.day,
                                    y = DensityM_NS.density,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto Densità Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messagedensity'
                    ),

                        dcc.Graph(
                            id='DensitySame',
                            figure={
                                'data': [
                                    {'x': DensityM_S.day, 'y': DensityM_S.density,
                                        'type': 'bar', 'name': 'Messaggio Comunità Uguale'},
                                    {'x': DensityM_NS.day, 'y': DensityM_NS.density,
                                        'type': 'bar', 'name': 'Messaggio Comunità Diversa'},
                                ],
                                'layout': {
                            'title': 'Confronto densità Messaggi dentro e fuori la comunità'
                                }
                            }
                        ),
                        dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = DensityT_S.day,
                                    y = DensityT_S.density,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = DensityT_NS.day,
                                    y = DensityT_NS.density,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto Densità Trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='tardesdensity'
                    ),
                        dcc.Graph(
                            id='DensityNotSame',
                            figure={
                                'data': [
                                
                                    {'x': DensityT_S.day, 'y': DensityT_S.density,
                                        'type': 'bar', 'name': 'Trade Comunità Uguale'},
                                    {'x': DensityT_NS.day, 'y': DensityT_NS.density,
                                        'type': 'bar', 'name': 'Trade Comunità Diversa'},
                                ],
                                'layout': {
                            'title': 'Confronto densità Trade dentro e fuori la comunità'
                                }
                            }
                        )
                
                    ]),

                    dcc.Tab(label='Clustering Coefficient', children=[
                        dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = CCoeffM_S.day,
                                    y = CCoeffM_S.clusteringCoefficient,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = CCoeffM_NS.day,
                                    y = CCoeffM_NS.clusteringCoefficient,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto coefficiente di clustering Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messaggeCoeff'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = CCoeffT_S.day,
                                    y = CCoeffT_S.clusteringCoefficient,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = CCoeffT_NS.day,
                                    y = CCoeffT_NS.clusteringCoefficient,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto coefficiente di clustering trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='tradeCoeff'
                    ),
                    ]),


                    dcc.Tab(label='Numero di Archi', children=[
                    
                        dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = ADM_S.day,
                                    y = ADM_S.nEdges,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = ADM_NS.day,
                                    y = ADM_NS.nEdges,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto numero di archi Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messaggena'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = ADT_S.day,
                                    y = ADT_S.nEdges,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = ADT_NS.day,
                                    y = ADT_NS.nEdges,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto numero di archi di trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='tradena'
                    ),
         
                    ]),
                    dcc.Tab(label='Diametro e Average Shortest', children=[

                        dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = DM_S.day,
                                    y = DM_S.diameter,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = DM_NS.day,
                                    y = DM_NS.diameter,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto diametro Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messaggediam'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = DT_S.day,
                                    y = DT_S.diameter,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = DT_NS.day,
                                    y = DT_NS.diameter,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto diametro trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='tradediam'
                    ),

                    #SHORTEST PATH
                     dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = SPM_S.day,
                                    y = SPM_S.averagePathLength,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = SPM_NS.day,
                                    y = SPM_NS.averagePathLength,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto shortest path medio Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messaggesp'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = SPT_S.day,
                                    y = SPT_S.averagePathLength,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = SPT_NS.day,
                                    y = SPT_NS.averagePathLength,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto shortest path medio trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                             
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='tradesp'
                    ),
         
                    ]),

                    #AVERAGE DEGREE
                    dcc.Tab(label='Average Degree & In/Out Degree', children=[

                
                        dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = ADegreeM_S.day,
                                    y = ADegreeM_S.averageDegree,
                                    mode = 'markers+lines',
                                    name = 'Messaggi intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = ADegreeM_NS.day,
                                    y = ADegreeM_NS.averageDegree,
                                    mode = 'lines+markers',
                                    name = 'Messaggi extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto grado medio Messaggi dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='messaggeadegree'
                    ),

                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Scatter(
                                    x = ADegreeT_S.day,
                                    y = ADegreeT_S.averageDegree,
                                    mode = 'markers+lines',
                                    name = 'Trade intra comunità',
                                    
                          
                                ),
                                go.Scatter(
                                    x = ADegreeT_NS.day,
                                    y = ADegreeT_NS.averageDegree,
                                    mode = 'lines+markers',
                                    name = 'Trade extra comunità'
                                ),
                                

                            ],
                            layout=go.Layout(
                                title='Confronto grado medio trade dentro e fuori la Comunità',
                                showlegend=True,
                                legend=go.layout.Legend(
                                    x=0,
                                    y=1.0
                                ),
                             
                                margin=go.layout.Margin(l=40, r=0, t=40, b=30)
                            )
                        ),
                        style={'height': 300},
                        id='tradeadegree'
                    ),
         
                    ]),
         
                ]),
            ]),

            
             dcc.Tab(label='Studio Singola Community Detection', children=[
               dcc.Tabs(id="communitystudytabs", children=[
                    dcc.Tab(label='Introduzione', children=[
         
                    ]),

                    dcc.Tab(label='Perchè?', children=[
         
                    ]),

                    dcc.Tab(label='User and Edge Trend', children=[
         
                    ]),

                dcc.Tab(label='Analisi Strutturale 1', children=[
                    
                        dcc.Graph(
                            id='ReciprocyNotSameStr',
                            figure={
                                'data': [
                                    {'x': ReciprocityM_S.day, 'y': ReciprocityM_S.Reciprocity,
                                        'type': 'bar', 'name': 'Messaggi Comnunità Uguale'},
                                    {'x': ReciprocityM_NS.day, 'y': ReciprocityM_NS.Reciprocity,
                                        'type': 'bar', 'name': 'Messaggi Comnuità Diverse'},],
                                'layout': {
                            'title': 'Confronto Reciprocità Messaggi dentro e fuori la Comunità'
                                }
                            }
                        ),
                        dcc.Graph(
                            id='ReciprocySameStr',
                            figure={
                                'data': [
                                    {'x': ReciprocityT_S.day, 'y': ReciprocityT_S.Reciprocity,
                                        'type': 'bar', 'name': 'Trade Comnunità Uguale'},
                                    {'x': ReciprocityT_NS.day, 'y': ReciprocityT_NS.Reciprocity,
                                        'type': 'bar', 'name': 'Trade Comnuità Diverse'},],
                                'layout': {
                            'title': 'Confronto Reciprocità Trade dentro e fuori la Comunità'
                                }
                            }
                        ),
                        

                   
                        dcc.Graph(
                            id='DensitySameStr',
                            figure={
                                'data': [
                                    {'x': DensityM_S.day, 'y': DensityM_S.density,
                                        'type': 'bar', 'name': 'Messaggio Comunità Uguale'},
                                    {'x': DensityM_NS.day, 'y': DensityM_NS.density,
                                        'type': 'bar', 'name': 'Messaggio Comunità Diversa'},
                                ],
                                'layout': {
                            'title': 'Confronto densità Messaggi dentro e fuori la comunità'
                                }
                            }
                        ),
                        dcc.Graph(
                            id='DensityNotSameStr',
                            figure={
                                'data': [
                                
                                    {'x': DensityT_S.day, 'y': DensityT_S.density,
                                        'type': 'bar', 'name': 'Trade Comunità Uguale'},
                                    {'x': DensityT_NS.day, 'y': DensityT_NS.density,
                                        'type': 'bar', 'name': 'Trade Comunità Diversa'},
                                ],
                                'layout': {
                            'title': 'Confronto densità Trade dentro e fuori la comunità'
                                }
                            }
                        ),
                
               
           
           dash_dangerously_set_inner_html.DangerouslySetInnerHTML('''
           <center><iframe src="https://albumizr.com/a/tBAv" scrolling="no" frameborder="0" allowfullscreen width="800" height="600"></iframe></iframe></center>
    '''),
         
        ]),

        dcc.Tab(label='Analisi Strutturale 2', children=[
                    dcc.Tab(label='Numero di Archi', children=[
         
                    ]),
                    dcc.Tab(label='Diametro e Average Shortest', children=[
         
                    ]),

                    dcc.Tab(label='Average Degree & In/Out Degree', children=[
         
                    ]),
        ]),
        

        
         dcc.Tab(label='Leader', children=[
            
                    dcc.Tab(label='Come e perchè?', children=[
         
                    ]),

                   
                    dcc.Tab(label='Relazioni con i diplomatici', children=[
         
                    ]),
           
               
        ]), 
        dcc.Tab(label='Relazioni con i diplomatici', children=[
            
                dcc.Graph(
                    id='DiplomaticiNotDiplomatici',
                    figure={
                        'data': [
                            {'x': 'Diplomatici', 'y': Diplomatics.DiplomatsLeaderMessage,
                                'type': 'bar', 'name': 'Messaggi Diplomatici'},
                             {'x': 'Non Diplomatici', 'y': Diplomatics.NormalUserLeaderMessage,
                                'type': 'bar', 'name': 'Messaggi utenti comuni'},],
                        'layout': {
                    'title': 'Confronto tra media messaggi di diplomatici e utenti comuni'
                        }
                    }
                ),
           
               
        ]),
          


                ]),



            ]),

        dcc.Tab(label='Conclusioni', children=[
         
        ]),
            
        

    ])
])

@app.callback(
    dash.dependencies.Output("DegreeDistributionGraph", "figure"),
    [dash.dependencies.Input("day-selected2", "value")])
    
def update_output(day):

    print(inDegreeDistribution[inDegreeDistribution['Type']=='Attack'][inDegreeDistribution['Day'] == 1]['Value'])
    
    return {
        'data': [
            go.Bar(
                        #print(inDegreeDistribution[inDegreeDistribution['Type'] == d][inDegreeDistribution['Day'] == day]['Value']),
                        x=inDegreeDistribution[inDegreeDistribution['Type'] == d]["Range"],

                        y=inDegreeDistribution[inDegreeDistribution['Type'] == d][inDegreeDistribution['Day'] == day]['Value'],
                        text=inDegreeDistribution[inDegreeDistribution['Type'] == d]['Type'],
                        
                        name=d,
                        
                )for d in inDegreeDistribution.Type.unique()],
            
                

            'layout': go.Layout(
                xaxis={'title': 'Range'},
                yaxis={'title': 'Valori'},
            )}

                            
@app.callback(
    dash.dependencies.Output("my-graph", "figure"),
    [dash.dependencies.Input("day-selected", "value")])

    
def update_output2(value):
    return {
        "data": [go.Pie(
            labels=edgesTrend["type"].unique().tolist(), 
            values=edgesTrend[edgesTrend["day"] == value]["quantity"].tolist(),
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']}, 
            textinfo='label')],
        "layout": go.Layout(title=f"Trend report daily", margin={"l": 200, "r": 200, },
                            legend={"x": 1, "y": 0.7})}

#Callback trickster
@app.callback( 
     dash.dependencies.Output('cheat-graphic', 'figure'),
     [dash.dependencies.Input('xaxis-column', 'value')])

def update_graph(xaxis_column_name):
    dff = Trickster[Trickster['Suspect'] == xaxis_column_name]
    #print(dff.head())

    return {
        'data': [go.Bar(
            #print(dff[dff['Type'] == d]['Present']),
            x=dff[dff['Type'] == d]['Day'],
            y=dff[dff['Type'] == d]['Present'],
            text=d,
            name=d,        
        ) for d in dff.Type.unique()],

        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear',
                'tickmode':'linear'
            },
            yaxis={
                'range':[0,1.5],
                'title': 'Activity',
                'type': 'linear',},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest',
            
        )
    }

   #Callback trickster
@app.callback( 
     dash.dependencies.Output('cheat-data', 'figure'),
     [dash.dependencies.Input('suspect-column', 'value')])

def update_pie(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    print(dff.head())
   
    x = [dff['TradeIn'], dff['TradeOut']]
    print(x)

    return {
        'data': [go.Pie(
            
            labels=['AttackIn', 'MessageIn', 'TradeIn'], 
            values=[dff['AttackIn'].item(), dff['MessageIn'].item(), dff['TradeIn'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']}, 
            textinfo='label')],
       
       

        'layout': go.Layout(
            title=f"IN", 
            margin={"l": 200, "r": 200, },
            legend={"x": 1, "y": 0.7})}

''' 
@app.callback( 
     dash.dependencies.Output('cheat-data', 'figure'),
     [dash.dependencies.Input('suspect-column', 'value')])

def update_pie(xaxis_column_name):
    dff = TricksterData[TricksterData['Suspect'] == xaxis_column_name]
    print(dff.head())
   
    x = [dff['TradeIn'], dff['TradeOut']]
    print(x)


    traceIN =  [go.Pie(
            labels=['AttackIn', 'MessageIn', 'TradeIn'], 
            values=[dff['AttackIn'].item(), dff['MessageIn'].item(), dff['TradeIn'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']}, 
            textinfo='label')],

    traceOUT =  [go.Pie(
            labels=['AttackOut', 'MessageOut', 'TradeOut'], 
            values=[dff['AttackOut'].item(), dff['MessageOut'].item(), dff['TradeOut'].item()],
            marker={'colors': ['#1f77b4', '#ff7f0e', '#2ca02c']}, 
            textinfo='label')],

    trace = traceIN + traceOUT,
    return {
        'data': trace,
       
       

        'layout': go.Layout(
            title=f"IN")}'''

'''app.layout = html.Div(children=[

    html.H1(children='MPROG Analysis'),
    html.H4(children='User trend in 30 days'),
    html.P('IL trend degli utenti nei 30 giorni è tendenzialmende descrescente'),
    html.P('La media degli utenti nei 30 giorni è di 2901'),

    dcc.Markdown(),
    dcc.Graph(
        id='life-exp-vs-gdp',
         figure={
            'data': [
                go.Scatter(
                    x=df[df['type'] == i]['day'],
                    y=df[df['type'] == i]['quantity'],
                    text=df[df['type'] == i]['type'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.type.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Giorni'},
                yaxis={'title': 'Quantità', 'type':'log'},
                #margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                #hovermode='closest'
            )
        }
    ),



    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

])'''

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
# )


if __name__ == '__main__':
    app.run_server(debug=True)

# dcc.Tab(label='Trickster Detection', children=[
#               dcc.Tabs(id="Trickster tabs", children=[
#                    dcc.Tab(label='Introduzione', children=[
#         
#                    ]),
#                ]),
#            ]),
