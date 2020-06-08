import numpy as np
import matplotlib.pyplot as plt

f=open("Galaxy2.txt","r")
f.readline()
Radius=[]
dR=[]
Velocity=[]
dV=[]
Mass=[]
G=4.3*(10**-6)
predictV=[]

for line in f:
   Radius.append(float(line.split("\t")[0]))
   dR.append(float(line.split("\t")[2]))
   Velocity.append(float(line.split("\t")[1]))
   dV.append(float(line.split("\t")[3]))
   Mass.append(float(line.split("\t")[4]))
   predictV.append(((float(G))*(float(line.split("\t")[4]))/(float(line.split("\t")[0])))**(0.5))

x=np.array(Radius)
y=np.array(Velocity)
z=np.array(predictV)
plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('Radius (km/h)')
plt.ylabel('Velocity (kpc)')
plt.show()