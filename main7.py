import numpy as np
import matplotlib.pyplot as plt
import math

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
p=100*(10**6)
r=1.87
MassDM=[]
Radius2=[]
dR2=[]
Velocity2=[]
dV2=[]
Mass2=[]
predictV2=[]
MassDM2=[]

for line in f:
  Mass.append(float(line.split("\t")[4]))
  MassDM.append(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r))))
  predictV.append(((float(G))*(float(line.split("\t")[4]))/(float(line.split("\t")[0])))**(0.5))

for line in g:
  Mass2.append(float(line.split("\t")[4]))
  MassDM2.append(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r))))
  predictV2.append(((float(G))*(float(line.split("\t")[4]))/(float(line.split("\t")[0])))**(0.5))

x=np.array(Mass)
z=np.array(MassDM)
y=np.array(predictV)
x2=np.array(Mass2)
y2=np.array(MassDM)
z2=np.array(predictV2)
plt.plot(x,y)
plt.plot(z,y)
plt.plot(x2,y2)
plt.plot(z2,y2)
plt.xlabel('Mass (Solar Masses)')
plt.ylabel('Predicted Velocity (km/s)')
plt.show()