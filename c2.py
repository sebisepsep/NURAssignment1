import numpy as np
import sys
import os
import matplotlib.pyplot as plt

def main():

    #original
    data=np.genfromtxt(os.path.join(sys.path[0],"Vandermonde.txt"),comments='#',dtype=np.float64)
    x_org=data[:,0]
    y_org=data[:,1]

    #import the values from 2a) so I don't need to calculate them again
    #most recent solution
    c = np.loadtxt('c_values.txt', delimiter=',')
    matrix = np.load('matrix.npy')
    alpha = np.load('alpha.npy')
    beta = np.load('beta.npy')

    #defining the iteration
    def iteration(c):
        add = np.zeros(len(matrix))
        for i in range(len(matrix)):
            val = 0
            for j in range(len(matrix)):
                val += matrix[i][j]*c[j]
            add[i] = val
            
        #delta y
        delta_y = add - y_org

        #forward substitution
        y_vec = np.zeros(len(x_org))
        y_vec[0] = delta_y[0] 
        for i in range(1,len(x_org)):
            val = 0
            for j in range(i): 
                val += alpha[i][j]*y_vec[j] 
            y_vec[i] = delta_y[i] - val
        
        #backward substitution
        x_vec = np.zeros(len(x_org))
        x_vec[len(x_org)-1] = y_vec[len(x_org)-1]*beta[len(x_org)-1][len(x_org)-1]  
        for i in range(len(x_org)-1,-1,-1):
            val = 0
            for j in range(i+1,len(x_org)):
                val += beta[i][j]*x_vec[j]
            x_vec[i] = (y_vec[i] -val)/beta[i][i]
        cdd = c - x_vec
        return cdd

    #performing one iteration
    cdd = iteration(c)

    x_new = np.linspace(x_org[0],x_org[-1],1001)
    y_new = np.zeros(1001)

    for i in range(len(x_org)):
        y_new += cdd[i] * x_new ** (i + 1)
        
    np.save('2c_1.npy', y_new)

    #calculation the delta
    yyx = x_org.copy()
    yyy = np.zeros(len(x_org))

    for i in range(len(x_org)):
        yyy += cdd[i] * yyx ** (i + 1)
        
    delta = abs(yyy-y_org)
    np.save('2c_delta_1.npy', delta)


    #performing 10 iterations
    c = np.loadtxt('c_values.txt', delimiter=',')
    for _ in range(10):
        cdd = iteration(c)
        c = cdd 
        
    x_new = np.linspace(x_org[0],x_org[-1],1001)
    y_new = np.zeros(1001)

    for i in range(len(x_org)):
        y_new += cdd[i] * x_new ** (i + 1)
        
    np.save('2c_10.npy', y_new)

    #calculation the delta
    yyx = x_org.copy()
    yyy = np.zeros(len(x_org))

    for i in range(len(x_org)):
        yyy += cdd[i] * yyx ** (i + 1)
        
    delta = abs(yyy-y_org)
    np.save('2c_delta10.npy', delta)

if __name__ == '__main__':
    main()