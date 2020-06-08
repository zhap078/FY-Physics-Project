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
MaddDM=[]
Radius2=[]
dR2=[]
Velocity2=[]
dV2=[]
Mass2=[]
predictV2=[]
MassDM2=[]
MaddDM2=[]

for line in f:
  Mass.append(float(line.split("\t")[4]))
  MassDM.append(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r))))
  MaddDM.append((float(line.split("\t")[4]))+(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r)))))

for line in g:
  Mass2.append(float(line.split("\t")[4]))
  MassDM2.append(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r))))
  MaddDM2.append((float(line.split("\t")[4]))+(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r)))))

x=np.array(Mass)
y=np.array(MassDM)
z=np.array(MaddDM)
x2=np.array(Mass2)
y2=np.array(MassDM2)
z2=np.array(MaddDM2)
plt.plot(x,y, label="Measured Mass 1")
plt.plot(x,z, label="Total Mass 1")
plt.plot(x2,y2, label="Measured Mass 2")
plt.plot(x2,z2, label="Total Mass 2")
plt.xlabel('Mass (Solar Masses)')
plt.ylabel('Dark Matter (Solar Masses)')
plt.legend()
plt.show()