#%%
import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

data = dict(type = 'choropleth', 
            locations = ['AZ', 'CA', 'NY'],
            locationmode = 'USA-states',
            colorscale = 'Portland',
            text = ['text1', 'text2', 'text3'],
            z = [1.0, 2.0, 3.0],
            colorbar = {'title':'Colorbar Title Goes Here'})

layout = dict(geo = {'scope':'usa'})

choromap = go.Figure(data = [data], layout = layout)

iplot(choromap)
df = pd.read_csv('2011_US_AGRI_Exports')
df.head()
data = dict(type = 'choropleth',
            colorscale = 'balance',
            locations = df['code'],
            locationmode = 'USA-states',
            marker = dict(line = dict(color = 'rgb(255,255,255)', width = 1)),
            z = df['total exports'],
            text = df['text'],            
            colorbar = {'title':"Millions USD"}
            )
print(data)
layout = dict(title = '2011 US Agriculture',
                geo = dict(scope='usa', showlakes = True, lakecolor = 'rgb(85,173,240)'))
print(layout)
choromap2 = go.Figure(data = [data], layout = layout)
iplot(choromap2)
# %%
