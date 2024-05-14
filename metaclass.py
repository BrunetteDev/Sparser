import numpy as np

from methods.data import Data
from methods.cs import Compressed_Sensing
from methods.basis import Basis

class Program(Basis, Compressed_Sensing, Data):
    def __init__(self, N: int, CR: float,  base: int, multidata: bool, slc_init: int, slc_end: int, path: str) -> None:
        self.__N = N
        self.__CR = CR
        self.__base = base
        self.__path = path 

        self.__M = int(self.__CR * self.__N * 0.01)
        self.__slc_init = slc_init
        self.__slc_end = slc_end

    def run(self):
        data = Data(self.__path, self.__slc_end, self.__slc_init)
        bas = Basis()
        cs = Compressed_Sensing()
        
        func = data.load_data(" ")


        if self.__base == 0:
            mtx = bas.build_fft_mtx(self.__N)
            inv_mtx = bas.inv_bas(mtx)
        elif self.__base == 1:
            mtx = bas.build_haar_mtx(self.__N, True) 
            inv_mtx = bas.inv_bas(mtx)
            mtx = bas.truncate_mtx(mtx, self.__N)
            inv_mtx = bas.truncate_mtx(inv_mtx, self.__N)
        elif self.__base == 2:
            mtx = bas.idct_mtx(self.__N)

        for i in range(len(func['y'])):
            func['y'][i] = data.re_scale_axis(func['y'][i])
        
        ri = cs.choice_sample(self.__N, self.__M)
        mtx = mtx[ri]
        
        # measurment = [np.array(np.zeros(len(func['y']))) for i in range(self.__M)]
        col = func['y']


        for i in range(len(col)):
            aux = []
            for counter in range(self.__N):
                if counter not in ri:
                    aux.append(col[i][counter])
            col[i] = np.array(aux)

        
        #col[i] = [val for val in col[i] if counter not in ri]
        for i in range(len(col)):
            print("\n\n\n\n Matrix: ", col[i].shape)
            print(cs.compress_signal(mtx, self.__N, col[i]))
        # print(mtx.shape)
        # print(len(col[0]))
        # print(len(ri))