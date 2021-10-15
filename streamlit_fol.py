import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
"# Lokasi Uji Coba Pertanian"

##Data Peta Ujicoba
iddesa_ex=['3201280003','3603140007']
data_grid=gpd.read_file('merged_ujicoba.gpkg').to_crs('EPSG:4326').query('iddesa not in@iddesa_ex ')

region = st.selectbox("Wilayah Uji Coba", sorted(data_grid.nmkab.unique()), index=0)
data_grid2=data_grid.query('nmkab==@region')
centroid=data_grid2.dissolve().centroid
nmdesa=data_grid2.nmdesa.unique()[0]
iddesa=data_grid2.iddesa.unique()[0]
m = folium.Map(location=[centroid.y,centroid.x], zoom_start=16,tiles = 'http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}',
              attr = 'Google')
for _, r in data_grid2.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry'])
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j,
                           style_function=lambda x: {'fillColor': 'orange'})
    geo_j.add_to(m)
    
st.write("NAMA DESA: ",nmdesa," [",iddesa,"]")
folium_static(m)  