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
        n = 2 ** np.ceil(np.log2(n))
        if n > 2:
            h = haarMatrix(n / 2)
        else:
            return np.array([[1, 1], [1, -1]])

        # calculate upper haar part
        h_n = np.kron(h, [1, 1])
        # calculate lower haar part 
        if normalized:
            h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)), [1, -1])
        else:
            h_i = np.kron(np.eye(len(h)), [1, -1])
        # combine parts
        h = np.vstack((h_n, h_i))
        return h
