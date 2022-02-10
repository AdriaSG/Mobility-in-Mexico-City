#Import libraries
import pandas as pd
import geopandas as gpd
from shapely import wkt

#Get file
url = "/Users/adrsanchez/PycharmProjects/Mobility-in-Mexico-City/datasets/mexico_city_agebs.json"
def get_file(url):
    """This function will get the json file, and return a dataframe object named df_mapa"""
    if url.lower().endswith(('.json')):
        mapa = gpd.read_file(url)
        print("File loaded successfully")
        print(mapa.crs)
        df_mapa = pd.DataFrame(mapa)
        if df_mapa.shape == (0, 0):
            print("File is empty")
        else:
            print(df_mapa.shape)
    else:
        print("File must be .json")
    return(df_mapa)

df_mapa = (get_file(url))

def calculate_centroids(df_mapa):
    """
    This function gets a geojson file without centroids and returns a dataframe with long and lat centroid coordinates.
    The file must contain polygon data named 'geometry' in order to calculate centroid.
    """
    # Create a list of strings (each is a polygon)
    df_mapa_centroids = df_mapa
    polygons = df_mapa_centroids['geometry'].astype(str)
    # Calculate centroids of each polygon and save them in to a list
    centroid = list()
    for i in polygons:
        temp_pol = wkt.loads(i)
        centroid.append(temp_pol.centroid.wkt)
    df_mapa_centroids['Centroid'] = centroid
    # Clean file
    df_mapa_centroids= df_mapa_centroids.drop(['CVE_AGEB', 'CVE_MUN', 'CVE_LOC', 'CVE_ENT', 'DISPLAY_NAME'], axis=1)
    # Add centroids in lat and long format
    lat = list()
    lon = list()
    for c in centroid:
        cen = c.split(" ")
        lon_temp = cen[1].replace('(', '')
        lat_temp = cen[2].replace(')', '')
        lat_temp = float(lat_temp)
        lon_temp = float(lon_temp)
        lat.append(round(lat_temp, 5))
        lon.append(round(lon_temp, 5))
    df_mapa_centroids['Centroid Lat'] = lat
    df_mapa_centroids['Centroid Lon'] = lon
    print ("Your file had been processed successfully. Your new dataset looks like:")
    print (df_mapa_centroids.head(5))
    return (df_mapa_centroids)

calculate_centroids(df_mapa)

