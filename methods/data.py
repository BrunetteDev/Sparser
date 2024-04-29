import json
import numpy as np
from enum import Enum

class Axis_Column(Enum):
    """ Enum Class for to read each columun for a no formated data """
    x = 0
    y = 1

class Data_Methods():

    def find_min(self, arr): 
        return min(arr)

class Data(Data_Methods):
    def __init__(self, path, slc_end, slc_init = 1):
        self.__path = path # Original Path of the file
        self.__slc_init = slc_init
        self.__slc_end = slc_end

    def load_data(self, delimiter):
        """ Read and Save the data in a dict """

        with open(self.__path, 'r') as f:
            func = {'x': [], 'y': []}
            for line in f.readlines():
                if '#' in line:
                    continue
                func[Axis_Column.x.name].append(float(line.split(delimiter)[Axis_Column.x.value])) # Split each line by delimiter and add the respective float value                
                aux_y = [float(line.split(delimiter)[i]) for i in range(self.__slc_init, self.__slc_end + 1)]
                func[Axis_Column.y.name].append(aux_y)
                aux_y = []
            f.close
        return func

    def re_scale_axis(self, func, axis : str):
        """ Centering the data for each axis """
        axis_to_rescale = func[axis]
        axis_min = self.find_min(axis_to_rescale)
        return list(np.array(axis_to_rescale) - axis_min)

    def export_json(self, func, path_save):
        with open(f'{path_save}', 'w', encoding="utf-8") as f:
            json.dump(func, f)
            f.close
