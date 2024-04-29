import numpy as np
import scipy as sp
from math import sqrt

class Basis():

    def build_fft_mtx(self, N):
        i, j = np.meshgrid(np.arange(N), np.arange(N))
        omega = np.exp( - 2 * np.pi * 1J / N )
        W = np.power( omega, i * j ) / sqrt(N)
        return W
    
    def build_haar_mtx(self, N, normalized=False):
        # Allow only size n of power 2
        N = 2 ** np.ceil(np.log2(N))
        if N > 2:
            h = self.build_haar_mtx(N / 2, normalized)
        else:
            return np.array([[1, 1], [1, -1]])

        # calculate upper haar part
        h_n = np.kron(h, [1, 1])
        # calculate lower haar part 
        if normalized:
            h_i = np.sqrt(N/2)*np.kron(np.eye(len(h)), [1, -1])
        else:
            h_i = np.kron(np.eye(len(h)), [1, -1])
        # combine parts
        h = np.vstack((h_n, h_i))

        return h

    def truncate_mtx(self, h, N):
        upper_tr = (len(h[1]) - N) // 2
        lower_tr = upper_tr + N if N % 2 == 0 else upper_tr + N - 1

        print(upper_tr, lower_tr - N)
        h = np.delete(h, slice(0, upper_tr), 0)
        h = np.delete(h, slice(N, lower_tr), 0)

        h = np.delete(h, slice(0, upper_tr), 1)
        h = np.delete(h, slice(N, lower_tr), 1)

        return h

    def inv_bas(self, mtx):
        return np.linalg.inv(mtx)