import matplotlib.pyplot as plt
from methods.data import Data
from methods.cs import Compressed_Sensing
from methods.basis import Basis
import numpy as np

def main():
    data = Data("/media/darketo/31fcec1d-d7c9-4d4f-9770-1e1d235bda6f/randy/Investigation/Sparsing/Projects/SparseData/Data/Randy_Data/Experimental/gar_001.xy")
    bas = Basis()

    #func = data.load_data("        ")
    func = data.load_data(" ")
    print(func)
    # func['x'] = data.re_scale_axis(func, 'x')
    # func['y'] = data.re_scale_axis(func, 'y')
    #data.export_json(func, './1')
    # y = func['y']
    # x = func['y']

    # x = x[0:(len(x)//6)]
    # y = y[0:len(y)//6]
    # cs = Compressed_Sensing(70, y)
    # N = len(y)
    # fr_mtx = bas.build_fft_mtx(N)
    #haar = bas.build_haar_mtx(y_len, False)
    #haar = bas.truncate_mtx(haar, y_len)
    #plt.plot(func['x'], fr_mtx @ np.array(func['y']))
    #plt.plot(func['x'], haar.T @ np.array(func['y']))
    #print(haar.shape)
    # print(len(func['y']))
    #plt.show()

    # res = cs.compress_signal(fr_mtx, N)
    # print(res)
    # plt.plot(x, res)
    # plt.show()
    # print(cs.reconst_sig(res, fr_mtx))
    

if __name__ == '__main__':
    main()