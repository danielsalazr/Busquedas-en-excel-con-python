# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tabla.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import psycopg2

import os
import pandas as pd
import re
from tabulate import tabulate
import barra_carga
import sys
from pandas import ExcelWriter


count = 0
pff = pd.DataFrame()

BUSQUEDA = 'break'
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
            #df = df.dropna(how='all')
            #print(df)
            pff = pff.append(df, ignore_index=True, sort=True)

        #print(pff)
        except:
            #print("Formato incorrecto en: ", filename )
            pass
    count += 1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 1060, 381))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(( "Linea", "Grupo", " Elemento ", "Descripcion", "Unidad", "Cantidad"))
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 560, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 70, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.click)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Consultar"))
        self.label.setText(_translate("MainWindow", "Tabla de consultas a base de datos"))

    def click(self):
        print("printado")
        tup1 = ('physics', 'chemistry', 1997, 2000,200,125,365);
        self.consulta()


    def consulta(self):
        global pff
        contador= 0
        for fila, row in pff.iterrows():
            #print(row)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(contador,0,QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(contador,1,QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(contador,2,QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(contador,3,QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(contador,4,QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(contador,5,QTableWidgetItem(str(row[5])))
            contador+=1
        header = self.tableWidget.horizontalHeader()       
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            #print(type(fila))

        #print(type(cursor1))



barra_carga.done = True
sys.stdout.write('\n')
pff.columns =['Codigo', 'Linea', 'Grupo', 'Elemento','Descripcion', 'Unidad', 'Cantidad', 'basura2','basura3', 'basura4']
pff.dropna(subset =['Descripcion'], inplace=True,axis=0) # aqui elimino todas las filas que contienen nan en la columna descripcion
pff.drop(pff.columns[[0,7,8,9]], axis='columns' , inplace=True) #aqui elimino las columnas que no obtienen nada
#print(tabulate(lista , header))
print(pff)
#import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
