import numpy as np
import pandas as pd

def test_func_3(a):
    s = pd.Series(a)
    return s.sum()

if __name__ == "__main__":
    np_array = np.array([10, 20, 30, 40, 50])
    sum = test_func_3(np_array)
    print(sum)
    print(type(sum))
