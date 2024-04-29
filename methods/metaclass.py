from basis import Basis
from cs import Compressed_Sensing
from data import Data

class Program(Basis, Compressed_Sensing, Data):
    def __init__(self, M: int, N: int, CR: float,  base: int, multidata: bool, slc_col: range, path: str) -> None:
        self.__M = M
        self.__N = N
        self.__CR = CR
        self.__base = base
        self.__path = path 

        self.__slc = (1)

    

