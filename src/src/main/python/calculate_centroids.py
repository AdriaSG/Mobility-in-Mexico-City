#Import libraries
import pandas as pd
import geopandas as gpd
from shapely import wkt


#Get file
url = "/Users/adrsanchez/PycharmProjects/Mobility-in-Mexico-City/datasets/mexico_city_agebs.json"
def get_json_file(url):
    """This function will get the json file, and return a dataframe object named df_mapa"""
    if url.lower().endswith(('.json')):
        mapa = gpd.read_file(url)
        print("File loaded successfully")
        df_mapa = pd.DataFrame(mapa)
        if df_mapa.shape == (0, 0):
            print("File is empty")
        else:
            print(df_mapa.shape)
    else:
        print("File must be .json")
    return (mapa)

def get_centroids(df):
    """
    This function gets a geojson file without centroids and returns a dataframe with long and lat centroid coordinates.
    The file must contain polygon data named 'geometry' in order to calculate centroid.
    """
    df_mapa_centroids = pd.DataFrame(df)
    polygons = df_mapa_centroids['geometry'].astype(str)
    centroid = list()
    for i in polygons:
        temp_pol = wkt.loads(i)
        centroid.append(temp_pol.centroid.wkt)
    df_mapa_centroids['Centroid'] = centroid
    df_mapa_centroids = df_mapa_centroids.drop(['CVE_AGEB', 'CVE_MUN', 'CVE_LOC', 'CVE_ENT', 'DISPLAY_NAME'], axis=1)
    lat = list()
    lon = list()
    for c in centroid:
        cen = c.split(" ")
        lat.append((lambda lat_temp: round(float(lat_temp), 5))(lat_temp=cen[1].replace('(', '')))
        lon.append((lambda lon_temp: round(float(lon_temp), 5))(lon_temp=cen[1].replace('(', '')))
    df_mapa_centroids['cen_lat'] = lat
    df_mapa_centroids['cen_lon'] = lon
    print("Your file had been processed successfully. Your new dataset looks like:")
    print(df_mapa_centroids.head(5))

get_centroids(get_json_file(url))

#
# Functional Programming:
# 1. Only final data structures are used: Here in the function get_json_file, the initial object named "mapa", instead of being overwritten, it gets copied in to a new
# variable named "df_mapa". This variable also transform object into a pandas DataFrame type. I avoided re-assignation to ensure only final data structures. Same case
# is presented in the second function while introducing the new variable "df_mapa_centroids".
#
# 2. Using anonymous functions: In the second function get_centroids, the correction of format variables (being float numbers with just 5 decimals) has been done using
# a lambda function. Lambda functions are specially useful when they are needed just for a short period of time, as benefit the code gets shorter and readable.