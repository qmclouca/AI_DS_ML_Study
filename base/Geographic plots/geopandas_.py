#%%
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import geopandas as gpd

data1 = gpd.read_file('bcim_2016_21_11_2018.gpkg', layer='adm_edif_pub_militar_a',driver='GPKG')
print("adm_edif_pub_militar_a:")
data1.plot()
data2 = gpd.read_file('bcim_2016_21_11_2018.gpkg', layer='adm_edif_pub_militar_p',driver='GPKG')
print("adm_edif_pub_militar_p:")
data2.plot()
data3 = gpd.read_file('bcim_2016_21_11_2018.gpkg', layer='adm_posto_fiscal_p',driver='GPKG')
print("adm_posto_fiscal_p:")
data3.plot()
data4 = gpd.read_file('bcim_2016_21_11_2018.gpkg', layer='eco_edif_agropec_ext_vegetal_pesca_p',driver='GPKG')
print("eco_edif_agropec_ext_vegetal_pesca_p:")
data4.plot()
data5 = gpd.read_file('bcim_2016_21_11_2018.gpkg', layer='eco_ext_mineral_p',driver='GPKG')
print(data5)
data5.plot()
# %%
