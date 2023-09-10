import numpy
from numpy import *


def calculate(array_arg:list) -> dict:
    # Validar tamaño de la lista
    try:
        if len(array_arg) != 9:
            raise ValueError
        else:
            nump_array = ndarray(shape=(3,3), dtype=int, buffer=array(array_arg))    # Convertir la lista en un numpy array
            return {
                'mean': [nump_array.mean(0), nump_array.mean(1), nump_array.mean()],
                'variance': [nump_array.var(0), nump_array.var(1), nump_array.var()],
                'standard deviation': [nump_array.std(0), nump_array.std(1), nump_array.std()],
                'max': [nump_array.max(0), nump_array.max(1), nump_array.max()],
                'min': [nump_array.min(0), nump_array.min(1), nump_array.min()],
                'sum': [nump_array.sum(0), nump_array.sum(1), nump_array.sum()]
            }
    except ValueError as ve:
        print("List must contain nine numbers.")
    pass
