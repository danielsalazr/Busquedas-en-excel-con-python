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

BUSQUEDA = 'puls'
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
            df = df.dropna(how='all')
            #print(df)
            pff = pff.append(df, ignore_index=True, sort=True)

        #print(pff)
        except:
            #print("Formato incorrecto en: ", filename )
            pass
    count += 1

for lineas, cant in zip(pff[4],pff[6]):
    res =re.match(pattern, str(lineas) )
    if res:
        lista.append([lineas, str(cant)])
        print(filename)
        #cantidad.append(cant)
        #print(res.string)

pd.set_option("max_row", None)

def writer_xls(fd):
    writer = ExcelWriter('articulos.xlsx')
    fd.to_excel(writer, 'Hoja de datos', index=False)
    writer.save()

"""
    #if filename.endswith(".asm") or filename.endswith(".py"):
    # print(os.path.join(directory, filename))
        continue
    else:
        continue
"""

#Imprimir Busqueda personalizada
#print('\n'.join('{}' for _ in range(len(lista))).format(*lista))

#Imprimir busqueda personalizada con numero de elementos
"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""

#print(barra_carga.contador)


#Imprimir la lista completa de todos los articulos
print(pff)
#writer_xls(pff)