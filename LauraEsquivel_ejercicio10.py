import urllib
from io import StringIO
from io import BytesIO
import csv
import numpy as np
from datetime import datetime
import matplotlib.pylab as plt
import pandas as pd
import scipy.signal as signal
## ABRIR LOS DATOS
## 2008
'
datos8=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt')

## 2009
datos9=pd.read_csv('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt=')
datos9["date [AST]"]=pd.to_datetime(datos["date [AST]"],format='%Y%m%d %H:%M:%S')
datos9.set_index(["date [AST]"],inplace=True)

## 2010 
datos10=pd.read_csv('https://hub.mybinder.org/user/computociencias-fisi2029-201910-n0bnrb14/edit/Seccion_1/Fourier/Datos/transacciones2010.txt")
datos10["date [AST]"]=pd.to_datetime(datos["date [AST]"],format='%Y%m%d %H:%M:%S')
datos10.set_index(["date [AST]"],inplace=True)

response=urllib.request.urlopen('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt')
leer=response.read()
data = StringIO(leer.decode())
r = csv.DictReader(data,dialect=csv.Sniffer().sniff(data.read(1000)))
data.seek(0)


response=urllib.request.urlopen('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt')
leer=response.read()
data = StringIO(leer.decode())
r = csv.DictReader(data,dialect=csv.Sniffer().sniff(data.read(1000)))
data.seek(0)


response=urllib.request.urlopen('https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt')
leer=response.read()
data = StringIO(leer.decode())
r = csv.DictReader(data,dialect=csv.Sniffer().sniff(data.read(1000)))
data.seek(0)

