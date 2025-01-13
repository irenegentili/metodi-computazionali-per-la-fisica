import numpy as np
import ctypes

_libfibonacci = np.ctypeslib.load_library('libfibonacci','../../MCF/E11/libfibonacci.so' )

_libfibonacci.fib.argtypes=[ctypes.c_int]
_libfibonacci.fib.restype= ctypes.c_double

def fib(n):
    return _libfibonacci.fib(int(n))


