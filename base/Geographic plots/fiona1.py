#%%
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import geopandas as gpd
data1 = gpd.read_file('bcim_2016_21_11_2018.gpkg', layer='lim_unidade_federacao_a',driver='GPKG')
data1.plot()
# %%
