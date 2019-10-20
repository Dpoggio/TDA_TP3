from Arguments import *
import Constant as p
import matplotlib.pyplot as plt
import csv

def getMbr(point_list):
    n = len(point_list)
    if n == 1:
        x = float(point_list[0][0])
        y = float(point_list[0][1])
        return [x,y,x,y]

    mid = round(n/2)
    [xmin1, ymin1, xmax1, ymax1] = getMbr(point_list[0:mid])
    [xmin2, ymin2, xmax2, ymax2] = getMbr(point_list[mid:n])
    xmin = min(xmin1,xmin2)
    xmax = max(xmax1,xmax2)
    ymin = min(ymin1,ymin2)
    ymax = max(ymax1,ymax2)
    
    return [xmin, ymin, xmax, ymax]

def main():
    archivo_coordenadas = Arguments().getArgs()

    csv_reader = csv.reader(archivo_coordenadas, delimiter=',')
    p_list = list(csv_reader)

    [xmin, ymin, xmax, ymax] = getMbr(p_list)

    print(xmin, ymin, xmax, ymax)
    return

#---------------------------
main()