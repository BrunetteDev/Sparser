import matplotlib.pyplot as plt
from methods.data import Data
from methods.basis import Basis
import numpy as np

def main():
    data = Data("/media/darketo/31fcec1d-d7c9-4d4f-9770-1e1d235bda6f/randy/Investigation/Sparsing/Projects/SparseData/Data/Randy_Data/Experimental/gar_001.xy")
    bas = Basis()
    
    func = data.load_data("        ")
    func['x'] = data.re_scale_axis(func, 'x')
    func['y'] = data.re_scale_axis(func, 'y')
    data.export_json(func, './1')

    fr_mtx = bas.build_fft_mtx(len(func['y']))
    haar = bas.build_haar_mtx(len(func['y'], False))
    print(haar)
    # plt.plot(func['x'], fr_mtx @ np.array(func['y']))
    # plt.show()

if __name__ == '__main__':
    main()