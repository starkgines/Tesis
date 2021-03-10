from matplotlib import pyplot as plt
import uproot
import numpy as np
from matplotlib import pyplot as plt
import cv2 

# Funcion para la lectura de una hoja en especifico
def read_root(path, leaf):
    file = uproot.open(path)
    keys_f = file['muonCCD1'].keys()

    mounCCD1 = file['muonCCD1']

    DiffX = np.array(mounCCD1["DiffX"].array())
    DiffY = np.array(mounCCD1["DiffY"].array())

    return [DiffX, DiffY]


if __name__ == '__main__':
    path = "../data/dose-rank000.root"
    [x, y] = read_root(path, "empanada")
    print("this is x: ",x)
    print("this is a y",y)
    # En siguiente paso es encontrar tanto los puntos de x e y en pixeles
    plt.figure(figsize=[10,10])
    [h,x,y,image]=plt.hist2d(x,y,bins=[3000,3000])
    plt.show()
    #plt.plot(x,y,'ro')
    print("this is the h img: ",h)
    #cv2.imshow('test',h)
    #cv2.waitKey(0)