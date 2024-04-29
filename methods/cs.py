import numpy as np
import cvxpy as cvx
import scipy.fftpack as spfft

class Compressed_Sensing():
    def __init__(self, CR, y):
        self.__CR = CR
        self.__y = np.array(y)

    
    def choice_sample(self):
        N = len(self.__y)
        M = int(self.__CR * N * 0.01)
        ri = np.random.choice(N, M, replace=False)

        mtx = mtx[ri]
        y2 = self.__y[ri]

        return (mtx, y2) 

    def compress_signal(self, mtx, N):
        vx = cvx.Variable(N)
        #samples = np.random.choice(N, M, replace=False)
        #[print(i) for i in samples]

        #ri = self.choice_sample()
        # print(mtx.shape)

        # print(vx.shape, mtx.shape)
        # A = mtx @ vx
        objective = cvx.Minimize(cvx.norm(vx, 1))
        print(vx.value)
        constraints = [mtx*vx == y2]
        prob = cvx.Problem(objective, constraints)
        result = prob.solve(verbose=True)
        
        rec = np.array(vx.value)
        rec = np.squeeze(rec)
        return spfft.ifft(rec, norm='ortho')

    def reconst_sig(self, res, bas):
        return 0