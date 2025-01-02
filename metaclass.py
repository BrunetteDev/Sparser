import numpy as np

from methods.data import Data
from methods.cs import Compressed_Sensing
from methods.basis import Basis
import scipy.fftpack as spfft
import matplotlib.pyplot as plt
import pandas as pd

class Program(Basis, Compressed_Sensing, Data):
    def __init__(self, N: int, CR: float,  base: int, multidata: bool, slc_init: int, slc_end: int, path: str, path_save_json: str) -> None:
        self.__N = N
        self.__CR = CR
        self.__base = base
        self.__path = path 
        self.__path_save_json = path_save_json

        self.__M = int(self.__CR * self.__N)
        self.__slc_init = slc_init
        self.__slc_end = slc_end

    def run(self):
        data = Data(self.__path, self.__slc_end, self.__slc_init)
        bas = Basis()
        cs = Compressed_Sensing()
        
        func = data.load_data(" ")

        for i in range(len(func['y'])):
            func['y'][i] = data.re_scale_axis(func['y'][i])
        
        if self.__base == 0:
            mtx = bas.build_fft_mtx(self.__N, func['y'][0])
            inv_mtx = bas.inv_bas(mtx)
        elif self.__base == 1:
            mtx = bas.build_haar_mtx(self.__N, True) 
            inv_mtx = bas.inv_bas(mtx)
            mtx = bas.truncate_mtx(mtx, self.__N)
            inv_mtx = bas.truncate_mtx(inv_mtx, self.__N)
        elif self.__base == 2:
            mtx = bas.idct_mtx(self.__N)
            inv_mtx = spfft.idct(mtx, norm="ortho", axis=0)

        ri = cs.choice_sample(self.__N, self.__M)
        cp_ri = np.sort(ri)

        #This work but i'm try a another fast sol
        # for i in range(len(cp_ri)):
        #     print(i)
        #     mtx = np.delete(mtx, cp_ri[i], 0)
        #     cp_ri -= cp_ri[i]
        mtx_df = pd.DataFrame(mtx)
        mtx_df = mtx_df.drop(mtx_df.columns[ri], axis=0)
        mtx = mtx_df.to_numpy()

        col = func['y']

        for i in range(len(col)):
            aux = []
            for counter in range(self.__N):
                if counter not in ri:
                    aux.append(col[i][counter])
            col[i] = np.array(aux)
        
        for i in range(len(col)):
            #aux = [list(i) for i in mtx]
                #"base": aux,
            data.export_json({
                'N': self.__N,
                "cr": self.__CR,
                "slc_init": self.__slc_init,
                "slc_end":self.__slc_end
            }, f"{self.__path_save_json}_[{i}]_metadata.json" )
            
            
            
            inv = cs.compress_signal(mtx, self.__N, col[i])
            aux2 = [float(i).__round__(4) for i in inv ]
            data.export_json({'y': aux2}, f"{self.__path_save_json}_[{i}].json")


            #Problema Inverso
            # if self.__base == 2:
            #     inv = spfft.idct(inv, norm='ortho', axis=0)
            # else:
            #     inv = cs.compress_signal(mtx @ inv_mtx, self.__N, col[i])

            # figures, ax = plt.subplots(2)
            # ax[0].plot(np.linspace(0,1, len(col[i])), col[i])
            # ax[1].plot(np.linspace(0,1, len(inv)), inv)
            # plt.show()
