import numpy as np
import matplotlib.pyplot as plt
import sys
import os
def main():
    data=np.genfromtxt(os.path.join(sys.path[0],"Vandermonde.txt"),comments='#',dtype=np.float64)
    x=data[:,0]
    y=data[:,1]

    #defining matrix 
    matrix = np.array([np.array([element**i for i in range(1,len(x)+1)]) for element in x])

    # Initialize alpha and beta matrices
    alpha = np.zeros((len(x), len(x)))
    beta = np.zeros((len(x), len(x)))

    # Fill beta matrix
    for j in range(len(x)):
        beta[0][j] = matrix[0][j]

    # Perform LU decomposition
    for i in range(len(x)):
        for j in range(len(x)):
            if i <= j:
                add1 = 0
                for k in range(i):
                    add1 += alpha[i][k]*beta[k][j]
                beta[i][j] = matrix[i][j] - add1
                
            if i > j:
                add2 = 0
                for k in range(j):
                    add2 += alpha[i][k]*beta[k][j]
                alpha[i][j] = (matrix[i][j]-add2)/beta[j][j]

    #forward substitution
    y_vec = np.zeros(len(x))
    y_vec[0] = y[0] 
    for i in range(1,len(x)):
        val = 0
        for j in range(i): 
            val += alpha[i][j]*y_vec[j] 
        y_vec[i] = y[i] - val

    # Backward substitution
    x_vec = np.zeros(len(x))
    x_vec[len(x)-1] = y_vec[len(x)-1]*beta[len(x)-1][len(x)-1]  
    for i in range(len(x)-1,-1,-1):
        val = 0
        for j in range(i+1,len(x)):
            val += beta[i][j]*x_vec[j]
        x_vec[i] = (y_vec[i] -val)/beta[i][i]

    #print out the values for c
    #print(x_vec)
    np.savetxt('c_values.txt',x_vec, delimiter=',')

    #plot the full 19th degree polynomial along with the points to show that it goes through them 
    # Calculate fitted polynomial values
    xx = np.linspace(x[0],x[-1],1001)
    yy = np.zeros(1001)

    for i in range(len(x)):
        yy += x_vec[i] * xx ** (i + 1)
        
    np.save('2a_LU.npy', yy)

    #plot the abolute difference between the given points and the result:
    yyx = x.copy()
    yyy = np.zeros(len(x))

    for i in range(len(x)):
        yyy += x_vec[i] * yyx ** (i + 1)
        
    delta = abs(yyy-y)
    np.save('2a_delta.npy', delta)

    np.save('matrix.npy', matrix)
    np.save('alpha.npy', alpha)
    np.save('beta.npy', beta)


if __name__ == '__main__':
    main()
