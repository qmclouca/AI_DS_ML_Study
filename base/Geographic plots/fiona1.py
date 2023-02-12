#%%
import fiona as fio
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from descartes import PolygonPatch
from shapely.geometry import Polygon, MultiPolygon,shape

import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import geopandas as gpd
data = fio.open('bcim_2016_21_11_2018.gpkg', layer='lim_unidade_federacao_a')
for feature in data:
    print(feature['properties']['nome'])
    for e in feature['geometry']['coordinates']:
        print(e)
        mp = Polygon([shape(e)])
        print(mp)
    
  
cm = plt.get_cmap('Set1')
num_col = len(mp)

fig = plt.figure()
ax = fig.add_subplot(111)
minx, miny, maxx, maxy = mp.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2 * w, maxx + 0.2 * w)
ax.set_ylim(miny - 0.2 * h, maxy + 0.2 * h)
ax.set_aspect(1)

patches = []
for idx, p in enumerate(mp):
    color = cm(1. * idx / num_col)
    patches.append(PolygonPatch(p, fc=color, ec=color, alpha=0.5, zorder=1))
ax.add_collection(PatchCollection(patches, match_original=True))
ax.set_xticks([])
ax.set_yticks([])
plt.title('Brazilian States')
plt.show()
# %%
