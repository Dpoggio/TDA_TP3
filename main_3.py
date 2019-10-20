from Arguments import *
import Constant as p
import matplotlib.pyplot as plt
import csv
import math

def getXY(point_list, ini, end, get_min, xy):
    n = end - ini + 1
    mid = math.floor((end+ini+1)/2)
    # print(ini, end, mid)
    # print (point_list, point_list[mid])
    if n == 2:
        if get_min == True:
            cond = float(point_list[ini][xy]) < float(point_list[end][xy])
        else:
            cond = float(point_list[ini][xy]) > float(point_list[end][xy])

        if cond:
            return float(point_list[ini][xy])
        else:
            return float(point_list[end][xy])
    else:
        if get_min == True:
            cond = float(point_list[mid][xy]) < float(point_list[mid+1][xy])
        else:
            cond = float(point_list[mid][xy]) > float(point_list[mid+1][xy])

        if cond:
            return getXY(point_list, ini, mid, get_min, xy)
        else:
            return getXY(point_list, mid, end, get_min, xy)
    
def main():
    archivo_coordenadas = Arguments().getArgs()

    csv_reader = csv.reader(archivo_coordenadas, delimiter=',')
    p_list = list(csv_reader)

    # [xmin, ymin, xmax, ymax] = getMbr(p_list)
    xmin = getXY(p_list,0, len(p_list) - 1, True, 0) 
    ymin = getXY(p_list,0, len(p_list) - 1, True, 1) 
    xmax = getXY(p_list,0, len(p_list) - 1, False, 0) 
    ymax = getXY(p_list,0, len(p_list) - 1, False, 1)

    print(xmin, ymin, xmax, ymax)
    return

#---------------------------
main()