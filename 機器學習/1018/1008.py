import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('regression.csv')
x=data.iloc[:,0].values
y=data.iloc[:,1].values
data.corr()

theta=[0,0]

def computeCost(x,y):
    E=(1/2)*sum((theta[0]+x*theta[1]-y))**2
    return E
E=computeCost(x,y)

eta=0.01
diff=1

count=200
temp=[0,0]
for iter in range(1,count+1,1):
    temp0=theta[0]-eta*sum((theta[0]+x*theta[1]-y))  
    temp1=theta[1]-eta*sum(((theta[0]+x*theta[1]-y)*x))

    theta[0]=temp0
    theta[1]=temp1
    E=computeCost(x,y)
    #print(E)


print(temp0)
print(temp1)

t=temp0+x*temp1
plt.plot(x,t,"-")
plt.scatter(x,y)
plt.show()

    




