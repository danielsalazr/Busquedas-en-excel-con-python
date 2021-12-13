import os
import pandas as pd
import re
from tabulate import tabulate
import barra_carga
import sys
from pandas import ExcelWriter
import tabla

count = 0
pff = pd.DataFrame()


BUSQUEDA = 'Marqu'
pa = '^[\d]?.*'+BUSQUEDA+'*.*$'
po = '^[\d].*BREAK*.*$'
#pattern  = re.compile(r'^[\d].*BREAK*.*$')
pattern  = re.compile(pa, re.I)

#print(repr(pa))

header = ["Articulo", "Cantidad"]

lista = []
cantidad = []

direccion = 'C:/Users/dsalazar/Desktop/Friogan Villavicencio Daniel S/Solicitudes de material'
#direccion =  'C:/Users/dsalazar/Desktop/solicitudes arrancador william'

barra_carga.t.start()
#for filename in os.listdir('C:/Users/danie/Desktop/Solicitudes_de_material'):
for filename in os.listdir(direccion):
    #print(filename)

    if count < 50:
        #print(filename)
        df= pd.DataFrame()
        try:
            #df= pd.read_excel('C:/Users/danie/Desktop/Solicitudes_de_material/'+filename,sheet_name='VER. 4' ,header= None)
            df= pd.read_excel(direccion+ '/'+filename,sheet_name='VER. 4' ,header= None)
            df.drop(df.index[:10], inplace= True)
            df.drop(df.index[len(df)-2:], inplace= True)
            #df = df.dropna(subset =['4'], how='all', inplace=True)
            #print(df)
            pff = pff.append(df, ignore_index=True, sort=True)

        #print(pff)
        except:
            #print("Formato incorrecto en: ", filename )
            pass
    count += 1

#print(type(pff))

pff.columns =['Codigo', 'Linea', 'Grupo', 'Elemento','Descripcion', 'Unidad', 'basura', 'basura','basura', 'basura']
pff.dropna(subset =['Descripcion'], inplace=True)
barra_carga.done = True
sys.stdout.write('\n')
print(pff)