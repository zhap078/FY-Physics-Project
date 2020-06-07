import numpy as np
import matplotlib.pyplot as plt

x=np.array([5,10,15,20,25])
y=np.array([0.2,0.5,0.8,1.0,1.3])
yerror=np.array([0.05,0.05,0.05,0.05,0.05])
count=0
minchi2=10000
minslope=0.0
start=0
stop=1
step=0.001
trend=[]
print("Your estimate was 0.05\n")

for slope in np.arange(start, stop, step):
  count=0
  for i in x:
    trend.append(((float(y[count])-(slope*i))**2)-(yerror[count])**2)
    count+=1
  chi2=np.sum(trend)
  trend=[]
  if(chi2<minchi2):
    minchi2=chi2
    minslope=slope
print("trend:",minslope,"\n")

fx1=minslope*x
fx=0.05*x

print("The difference between your estimate and the trend is",(minslope-0.05),"\n")
print("The trend is green. Your estimate is red") 

plt.errorbar(x,y,yerror,fmt='bo')
plt.plot(x,fx,'r-')
plt.plot(x,fx1,'g-')
plt.show()