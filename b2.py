import numpy as np
import matplotlib.pyplot as plt
import sys
import os

def main():
    array = np.linspace(0,100,1001)
    data=np.genfromtxt(os.path.join(sys.path[0],"Vandermonde.txt"),comments='#',dtype=np.float64)
    #initial points 
    t=data[:,0]
    iy=data[:,1]

    M = len(t)
    # set p_i = y_i
    p = iy.copy()
    zero = np.zeros(1001)
    val = 0
    for x in array:
        count = 0
        p = iy.copy()
        for k in range(1,M): 
            for i in range(M-k):
                j = i + k
                l = j - count
                #upgrade the p_i value for the interval overwriting previous orders
                p[i] = ((t[j] - x)*p[i] + (x-t[i])*p[l])/(t[j]-t[i])
            count += 1
        
        zero[val] = p[0]
        val += 1
        
    np.save('2b.npy', zero)


    array = t.copy()
    zero = np.zeros(len(iy))
    val = 0
    for x in array:
        count = 0
        p = iy.copy()
        for k in range(1,M): 
            for i in range(M-k):
                j = i + k
                l = j - count
                p[i] = ((t[j] - x)*p[i] + (x-t[i])*p[l])/(t[j]-t[i])
            count += 1
        
        zero[val] = p[0]
        val += 1
        
    delta = abs(zero - iy)
    np.save('2b_delta.npy', delta)
if __name__ == '__main__':
    main()
