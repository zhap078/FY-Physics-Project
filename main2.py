import numpy as np
import matplotlib.pyplot as plt
import math

f=open("Galaxy1.txt","r")
f.readline()
Radius=[]
dR=[]
Velocity=[]
dV=[]
Mass=[]
G=4.3*(10**-6)
predictV=[]
p=100*(10**6)
r=1.87
MassDM=[]

for line in f:
  Mass.append(float(line.split("\t")[4]))
  MassDM.append(4*pi*p*(r**2)*((float(line.split("\t")[0]))-(r*atan((float(line.split("\t")[0]))/r)))

x=np.array(Radius)
y=np.array(Velocity)
z=np.array(predictV)
plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('Radius (km/h)')
plt.ylabel('Velocity (kpc)')
plt.show()