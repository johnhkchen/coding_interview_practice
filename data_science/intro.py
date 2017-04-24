# This is John's first attempt at using NumPy, pandas, and so on...

# NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

import numpy as np

a = np.arange(15).reshape(3,5)
print(a)

import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])
print(s) 

import matplotlib.pyplot as plt