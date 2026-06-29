import numpy as np
import pandas as pd

def main():
    float_arr = np.array([1,2,3,4], dtype="float")
    int_arr = np.array([1.0,2.0,3.0,4.0], dtype="int64")

    # Dimensions
    oneD_arr = np.array([1,2,3,4])
    twoD_arr = np.array([[1,2,3,4], [1,2,3,4]])
    threeD_arr = np.array([[[], [], []]]) # [ [ [], [], [0] 3] 1]

    b = np.array(9) # this shit is a scalar
    
    return print(f"{b} {b.shape} {b.ndim}")

if __name__=="__main__":
    main()
