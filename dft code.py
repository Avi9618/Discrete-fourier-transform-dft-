import numpy as np
import matplotlib.pyplot as plt
n=np.arange(0,4,1)
y=np.arange(0,4,1)
x=np.arange(0,4,1)
print('enter the values')
for i in range (0,4):
    n[i]=input()
lenx=len(n)
k=np.zeros(lenx,complex)
w=2*np.pi*-1
z=np.complex(0,w)
for i in range(0,lenx):
    k[i]=(n[0]+(n[1]*np.exp((z*i*1)/lenx))+(n[2]*np.exp((z*i*2)/lenx))+(n[3]*np.exp((z*i*3)/lenx)))
for j in range(0,lenx):
    print k[j]
plt.stem(n,k)
plt.xlabel('n')
plt.ylabel('k[o]')    
print('dft')
print('idft')
w2=2*np.pi*1 
print('now doing the idft')
N=4
for m in range(0,lenx):
    n[m]=(k[0]+(k[1]*np.exp((w2*m*1)/lenx))+(k[2]*np.exp((w2*m*2)/lenx))+(k[3]*np.exp((w2*m*3)/lenx)))
    y[m]=n[m]/N
for r in range(0,lenx):
    print y[r]
