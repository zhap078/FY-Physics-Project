import numpy as np
import matplotlib.pyplot as plt

f=open("Galaxy1.txt","r")
f.readline()
g=open("Galaxy2.txt","r")
g.readline()

Radius=[]
dR=[]
Velocity=[]
dV=[]
Mass=[]
G=4.3*(10**-6)
predictV=[]
Radius2=[]
dR2=[]
Velocity2=[]
dV2=[]
Mass2=[]
G=4.3*(10**-6)
predictV2=[]

for line in f:
   Radius.append(float(line.split("\t")[0]))
   dR.append(float(line.split("\t")[2]))
   Velocity.append(float(line.split("\t")[1]))
   dV.append(float(line.split("\t")[3]))
   Mass.append(float(line.split("\t")[4]))
   predictV.append(((float(G))*(float(line.split("\t")[4]))/(float(line.split("\t")[0])))**(0.5))

for line in g:
   Radius2.append(float(line.split("\t")[0]))
   dR2.append(float(line.split("\t")[2]))
   Velocity2.append(float(line.split("\t")[1]))
   dV2.append(float(line.split("\t")[3]))
   Mass2.append(float(line.split("\t")[4]))
   predictV2.append(((float(G))*(float(line.split("\t")[4]))/(float(line.split("\t")[0])))**(0.5))

x=np.array(Radius)
y=np.array(Velocity)
z=np.array(predictV)
x2=np.array(Radius2)
y2=np.array(Velocity2)
z2=np.array(predictV2)
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x2,y2)
plt.plot(x2,z2)
plt.xlabel('Radius (km/h)')
plt.ylabel('Velocity (kpc)')
plt.show()