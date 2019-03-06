from geopandas import GeoSeries, GeoDataFrame, gpd
import matplotlib.pyplot as plt
import pandas as pd

#read from KML file
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


fp1 = "/Users/tutu/Downloads/1.kml"

poly1 = gpd.read_file(fp1, driver='KML')

#these are my polygons which are now GEOPANDAS DATAFRAME

polys = gpd.GeoDataFrame( pd.concat( [poly1,poly2,poly3,poly4,poly5, poly6, poly7, poly8], ignore_index=True) )

polys = polys.sort_values(by=['Name'])

