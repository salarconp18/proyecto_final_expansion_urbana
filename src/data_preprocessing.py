#Función recorte municipio de interés
import geopandas as gpd
import os

def clip_vector(vector, aoi, ruta_salida=None):
    """
    Recorta una capa vectorial usando un polígono (aoi).

    Parámetros:
    - vector: GeoDataFrame a recortar
    - aoi: GeoDataFrame del área de interés
    - ruta_salida: ruta opcional para guardar el resultado

    Retorna:
    - GeoDataFrame recortado
    
    """
    # Asegura el mismo sistema de referencia
    if vector.crs != aoi.crs:
        aoi = aoi.to_crs(vector.crs)
        
    # Recorte
    recorte = gpd.clip(vector, aoi)
    
    # Filtrar solo polígonos
    solo_poligonos = recorte[recorte.geometry.type.isin(['Polygon', 'MultiPolygon'])]

    # Guardar si se solicita
    if ruta_salida:
        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        solo_poligonos.to_file(ruta_salida)
        print(f"Archivo guardado en: {ruta_salida}")

    return solo_poligonos
    
#Función área influencia ronda hidrica


