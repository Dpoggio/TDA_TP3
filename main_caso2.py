from Arguments import *
import Constant as p
import matplotlib.pyplot as plt
import numpy as np
import csv
import math


# Funcion que retorna un X o un Y minimo o maximo:
#     get_min:
#         - True: Retorna un minimo
#         - False: Retorna un maximo
#     xy:
#         - 0 : Retorna X
#         - 1 : Retorna Y
#     Ejemplo:
#         getXY(...., True, 1) -> Retorna Y minimo

def getXY(point_list, ini, end, get_min, xy):
    n = end - ini + 1
    mid = math.floor((end+ini+1)/2)

    if n == 2:
        if get_min == True:
            cond = point_list[ini][xy] < point_list[end][xy]
        else:
            cond = point_list[ini][xy] > point_list[end][xy]

        if cond:
            return point_list[ini][xy]
        else:
            return point_list[end][xy]
    else:
        if get_min == True:
            cond = point_list[mid][xy] < point_list[mid+1][xy]
        else:
            cond = point_list[mid][xy] > point_list[mid+1][xy]

        if cond:
            return getXY(point_list, ini, mid, get_min, xy)
        else:
            return getXY(point_list, mid, end, get_min, xy)
    
# Programa Principal
def main():
    archivo_coordenadas = Arguments().getArgs()
    
    csv_reader = csv.reader(archivo_coordenadas, delimiter=',')
    p_list = [[float(i[0]), float(i[1])] for i in list(csv_reader)]

    xmin = getXY(p_list,0, len(p_list) - 1, True, 0) 
    ymin = getXY(p_list,0, len(p_list) - 1, True, 1) 
    xmax = getXY(p_list,0, len(p_list) - 1, False, 0) 
    ymax = getXY(p_list,0, len(p_list) - 1, False, 1)

    print('[',xmin, ymin, xmax, ymax,']')

    # Impresion de resultados en forma grafica
    Xsq = [xmin, xmin, xmax, xmax, xmin]
    Ysq = [ymin, ymax, ymax, ymin, ymin]
    
    ft_list = np.array(p_list)
        
    fig, ax = plt.subplots()
    ax.plot(Xsq, Ysq)
    ax.plot(ft_list[:,0], ft_list[:,1])
    fig.suptitle('Algoritmo Caso 2')
    plt.show()    
    return 
    
#---------------------------
main()