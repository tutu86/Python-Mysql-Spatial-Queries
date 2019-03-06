from geo_input import polys
from get_DB_data import orders
from shapely.geometry import Point
from geopandas import GeoSeries, GeoDataFrame
import matplotlib.pyplot as plt

#create point data format (lat, lon)

orders['Coordinates'] = list(zip(orders.food_request_origin_location_x, orders.food_request_origin_location_y))

#make my points as beign recognised as points (coordinates)
orders['Coordinates'] = orders['Coordinates'].apply(Point)

gdf = GeoDataFrame(orders, geometry='Coordinates')

#clean dataset

POINT = gdf['Coordinates']
POLYGONS = polys['geometry']

#One Liner Location Query I love you PYTHON❤️

print(POINT.within(POLYGONS))

#Visualise the data

southern = polys.loc[polys['Name']=='Avcılar']

southern.reset_index(drop=True, inplace=True)

fig, ax = plt.subplots()

polys.plot(ax=ax, facecolor='gray')

southern.plot(ax=ax, facecolor='red')

POINT.plot(ax=ax, color='blue', markersize=5)

plt.tight_layout()

plt.show()
