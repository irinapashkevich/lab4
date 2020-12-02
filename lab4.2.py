from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

f=open(input())
N=int(f.readline()[0])
AA=[]
for i in range(N):
    AA.append(f.readline().split())

A=np.array(AA)
b=np.array(f.readline().split())
x = linalg.solve(A, b)
n=np.arange(N)
plt.bar(n,x)
plt.grid()
plt.show()