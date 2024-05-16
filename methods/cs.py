import numpy as np
import cvxpy as cvx
import scipy.fftpack as spfft

import matplotlib.pyplot as plt


class Compressed_Sensing():    
    def choice_sample(self, N, M):
        ri = np.random.choice(N, M, replace=False)
        return ri


    def compress_signal(self, mtx, N, y2):
        vx = cvx.Variable(N)

        objective = cvx.Minimize(cvx.norm(vx, 1))
        print("Bef: ", vx.value)
        constraints = [mtx*vx == y2]
        prob = cvx.Problem(objective, constraints)
        result = prob.solve(verbose=True)
        
        rec = np.array(vx.value)
        print("After: ", rec)
        rec = np.squeeze(rec)

        return rec

    def reconst_sig(self, res, bas):
        return 0