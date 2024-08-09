import geopandas as gpd
import psycopg2


def conecta_db():
    con = psycopg2.connect(host='0.0.0.0', 
                         database='gis',
                         user='docker',
                         password = 'docker',
                         port = 5432)
    return con

def inserir_db(sql,params):
    con = conecta_db()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    cur.close()


gdf = gpd.read_file("amostras.geojson")
gdf['geometry'] = gdf['geometry'].apply(lambda x: str(x)[9:-1].replace('(','').replace(')',''))

for i in gdf.index:
    sql = """
    INSERT into public.amostras (idlulcn,coordenadas,geom) 
    values(%s,%s,ST_GeomFromText(%s, 4326));
    """
    params = [int(gdf['LULC'][i]),gdf['geometry'][i],'POLYGON(({}))'.format(gdf['geometry'][i])]
    inserir_db(sql,params)