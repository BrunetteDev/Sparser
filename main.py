import matplotlib.pyplot as plt
from methods.data import Data
from methods.cs import Compressed_Sensing
from methods.basis import Basis
from metaclass import Program
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Compressed Sensing 1-D \n [Example] python main.py -n 11968 -cr 0.5 -b 0 -mc 1 -ic 1 -lc 2 -p <path> -ps <path save>')
parser.add_argument('--rowmtx', '-m', help='\nNumber of Row of Compresion Matrix')
parser.add_argument('--colmtx', '-n', help='\nNumber of Columns of the Compresion Matrix', type=int)
parser.add_argument('--compresionratio', '-cr', help='\nCompresion Ratio (0-1)\n', type=float)
parser.add_argument('--multicol', '-mc', help="\nUse the multicol of the file (0-False 1-True)", type=int)
parser.add_argument('--base', '-b', help="\nThe base of the data representation \n (0 - Fourier, 1 - Haar Wavelet, 2 - Discrete Cosine)", type=int)
parser.add_argument('--startcol', '-ic', help="\nInitial value of the silde of the column of the data for to process", type=int)
parser.add_argument('--lastcol', '-lc', help="\nLast value of the silde of the column of the data for to process", type=int)
parser.add_argument('--path', '-p', help="\nPath of the file", type=str)
parser.add_argument('--pathsave', '-ps', help="\n Path to save the result", type=str)


args = parser.parse_args()

def main():
    path = "/media/darketo/31fcec1d-d7c9-4d4f-9770-1e1d235bda6f/randy/Investigation/Sparsing/Projects/SparseData/Data/Randy_Data/Experimental/gar_001.xy"
    path = "../Sparser/Files/formated.txt"

    
#    for i in range(0, 100, 10):
    program = Program(args.colmtx // 12,args.compresionratio,args.base,args.multicol, args.startcol, args.lastcol, args.path, args.pathsave)
    program.run()

if __name__ == '__main__':
    main()