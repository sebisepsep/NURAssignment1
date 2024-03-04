import numpy as np
import matplotlib.pyplot as plt
import sys
import os

data=np.genfromtxt(os.path.join(sys.path[0],"Vandermonde.txt"),comments='#',dtype=np.float64)
x_org=data[:,0]
y_org=data[:,1]

xx = np.linspace(x_org[0],x_org[-1],1001)

#data for 2a
lu = np.load('2a_LU.npy') #with xx
lu_delta = np.load('2a_delta.npy') #with x

#plots:
plt.scatter(xx,lu ,marker =".", s = 2, color ="red", label ="LU fit")

plt.scatter(x_org,y_org, label ="Dataset")

plt.title("LU decomposition")
plt.ylim(-400,400)
plt.xlim(-1,101)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("lu.jpg")
plt.clf()

#plots for 2b
nev = np.load("2b.npy") #with xx
nev_delta = np.load("2b_delta.npy")
#plots:
plt.scatter(xx, nev ,marker =".", s = 2, color ="red", label ="Neville's Algorithm")

plt.scatter(x_org,y_org, label ="Dataset")

plt.title("Neville's Algorithm")
plt.ylim(-400,400)
plt.xlim(-1,101)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("neville.jpg")
plt.clf()

#plots for 2c
one = np.load("2c_1.npy")
one_delta = np.load('2c_delta_1.npy')
ten = np.load("2c_10.npy")
ten_delta = np.load('2c_delta10.npy')

#plots:
plt.scatter(xx, one ,marker =".", s = 2, color ="red", label ="LU one iteration")

plt.scatter(x_org,y_org, label ="Dataset")

plt.title("LU decomposition with one iteration")
plt.ylim(-400,400)
plt.xlim(-1,101)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("one.jpg")
plt.clf()

#plots:
plt.scatter(xx, ten ,marker =".", s = 2, color ="red", label ="LU ten iteration")

plt.scatter(x_org,y_org, label ="Dataset")

plt.title("LU decomposition with ten iteration")
plt.ylim(-400,400)
plt.xlim(-1,101)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("ten.jpg")
plt.clf()

#errors


plt.scatter(x_org,lu_delta ,marker =".",s = 6, color ="red",label ="LU")
plt.scatter(x_org,nev_delta ,marker =".",s = 6, color ="green",label ="Neville's Algorithm")
plt.scatter(x_org,one_delta ,marker =".",s = 6, color ="orange",label ="One Iteration")
plt.scatter(x_org,ten_delta ,marker =".", s = 6, color ="blue",label ="Ten Iterations")

plt.title("Absolute difference $|y(x_i) - y_i|$")
plt.ylim(1e-16,1e1)
plt.yscale('log')
plt.xlim(-1,101)
plt.xlabel("x")
plt.ylabel('$|y-y_i|$')
plt.legend()
plt.savefig("error.jpg")
plt.clf()
