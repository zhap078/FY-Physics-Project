import numpy as np
import matplotlib.pyplot as plt
import math

f=open("Galaxy2.txt","r")
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
MaddDM=[]

for line in f:
  Mass.append(float(line.split("\t")[4]))
  MassDM.append(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r))))
  MaddDM.append((float(line.split("\t")[4]))+(4*math.pi*p*(r**2)*((float(line.split("\t")[0]))-(r*math.atan((float(line.split("\t")[0]))/r)))))

x=np.array(Mass)
y=np.array(MassDM)
z=np.array(MaddDN)
plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('Mass (Solar Masses)')
plt.ylabel('Dark Matter (Solar Masses)')
plt.show()