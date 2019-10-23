from Arguments import *
import Constant as p
import matplotlib.pyplot as plt
import numpy as np
import csv

archivo_coordenadas = Arguments().getArgs()

csv_reader = csv.reader(archivo_coordenadas, delimiter=',')
xy_0 = csv_reader.__next__()
Xmin = float(xy_0[0])
Xmax = float(xy_0[0])
Ymin = float(xy_0[1])
Ymax = float(xy_0[1])

Xprnt = []
Yprnt = []

for row in csv_reader:
	x = float(row[0])
	y = float(row[1])
	Xprnt.append(x)
	Yprnt.append(y)
		
	if x < Xmin:
		Xmin = x
		
	if x > Xmax:
		Xmax = x
		
	if y < Ymin:
		Ymin = y
		
	if y > Ymax:
		Ymax = y

print('[',Xmin, Ymin, Xmax, Ymax,']')

# Impresion de resultados en forma grafica

Xprnt.append(Xprnt[0])
Yprnt.append(Yprnt[0])

Xsq = [Xmin, Xmin, Xmax, Xmax, Xmin]
Ysq = [Ymin, Ymax, Ymax, Ymin, Ymin]

# ft_list = np.array([[float(i[0]), float(i[1])] for i in list(csv_reader)])
    
fig, ax = plt.subplots()
ax.plot(Xsq, Ysq)
ax.plot(Xprnt, Yprnt)
fig.suptitle('Algoritmo Caso 1')
plt.show()    
