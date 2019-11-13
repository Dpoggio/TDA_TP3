from Arguments import *
import Constant as p
import matplotlib.pyplot as plt
import numpy as np
import csv
import math


# Funcion que retorna un X o un Y minimo:
#     xy:
#         - 0 : Retorna X
#         - 1 : Retorna Y
#     Ejemplo:
#         get_minimo(...., 1) -> Retorna Y minimo

def get_minimo(pl, ini, end, xy):
    n = end - ini + 1
    mid = math.floor((end+ini+1)/2)

    if n == 2:
        if pl[ini][xy] < pl[end][xy] :
            return pl[ini][xy]
        else:
            return pl[end][xy]
    else:
        if (pl[end][xy] > pl[ini][xy] and pl[mid][xy] < pl[mid+1][xy]) \
            or (pl[end][xy] < pl[ini][xy] and pl[mid][xy] < pl[mid+1][xy] and pl[ini][xy] >= pl[mid][xy]) \
            or (pl[end][xy] > pl[ini][xy] and pl[mid][xy] > pl[mid+1][xy] and pl[ini][xy] <= pl[mid][xy]):
            return get_minimo(pl, ini, mid, xy)
        else:
            return get_minimo(pl, mid, end, xy)
    

# Funcion que retorna un X o un Y maximo:
#     xy:
#         - 0 : Retorna X
#         - 1 : Retorna Y
#     Ejemplo:
#         get_maximo(...., 1) -> Retorna Y maximo

def get_maximo(pl, ini, end, xy):
    n = end - ini + 1
    mid = math.floor((end+ini+1)/2)
    
    if n == 2:
        if pl[ini][xy] > pl[end][xy] :
            return pl[ini][xy]
        else:
            return pl[end][xy]
    else:
        if (pl[end][xy] < pl[ini][xy] and pl[mid][xy] > pl[mid+1][xy]) \
            or (pl[end][xy] > pl[ini][xy] and pl[mid][xy] > pl[mid+1][xy] and pl[ini][xy] <= pl[mid][xy]) \
            or (pl[end][xy] < pl[ini][xy] and pl[mid][xy] < pl[mid+1][xy] and pl[ini][xy] >= pl[mid][xy]):
            return get_maximo(pl, ini, mid, xy)
        else:
            return get_maximo(pl, mid, end, xy)
    
# Programa Principal
def main():
    archivo_coordenadas = Arguments().getArgs()
    
    csv_reader = csv.reader(archivo_coordenadas, delimiter=',')
    p_list = [[float(i[0]), float(i[1])] for i in list(csv_reader)]

    xmin = get_minimo(p_list,0, len(p_list) - 1, 0) 
    ymin = get_minimo(p_list,0, len(p_list) - 1, 1) 
    xmax = get_maximo(p_list,0, len(p_list) - 1, 0) 
    ymax = get_maximo(p_list,0, len(p_list) - 1, 1)  

    print('[',xmin, ymin, xmax, ymax,']')

    # Impresion de resultados en forma grafica
    Xsq = [xmin, xmin, xmax, xmax, xmin]
    Ysq = [ymin, ymax, ymax, ymin, ymin]
    
    ft_list = np.array(p_list)
        
    fig, ax = plt.subplots()
    ax.plot(Xsq, Ysq)
    ax.plot(ft_list[:,0] , ft_list[:,1])
    fig.suptitle('Algoritmo Caso 2')
    plt.show()    
    return 
    
#---------------------------
main()