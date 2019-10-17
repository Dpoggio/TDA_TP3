from Arguments import *
import Constant as p
import matplotlib.pyplot as plt
import csv

archivo_coordenadas = Arguments().getArgs()

csv_reader = csv.reader(archivo_coordenadas, delimiter=',')
xy_0 = csv_reader.__next__()
Xmin = float(xy_0[0])
Xmax = float(xy_0[0])
Ymin = float(xy_0[1])
Ymax = float(xy_0[1])

for row in csv_reader:
	x = float(row[0])
	y = float(row[1])
		
	if x < Xmin:
		Xmin = x
		
	if x > Xmax:
		Xmax = x
		
	if y < Ymin:
		Ymin = y
		
	if y > Ymax:
		Ymax = y
		
print(Xmin, Ymin, Xmax, Ymax)