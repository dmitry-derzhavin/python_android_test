import numpy as np
import pandas as pd

def test_func_1(a, b):
    s = pd.Series([a, b])
    return s.sum()

if __name__ == "__main__":
    sum = test_func_1(3,4)
    print(sum)
    print(type(sum))
